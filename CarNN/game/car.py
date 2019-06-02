import math as m
import pygame as pyg
import os
from .util import intersection3, intersect_check, point_generator, equation_generator

class Car(pyg.sprite.Sprite):

    #initialize variables

    def __init__(self, x, y, tuples, equations, rects, mapguide, state, screen, angle = 270):

        #current pos
        self.startX = x
        self.startY = y
        self.x = x
        self.y = y
        self.width = 20
        self.height = 40
        #current x, y speed
        self.speed = 0
        self.xSpeed = 0
        self.ySpeed = 0
        #max, min for acceleration, speed
        self.maxAcceleration = 10
        self.maxSpeed = 50
        #angles
        self.angle = angle
        self.angularSpeed = 1
        self.maxAngularSpeed = 1 #???
        #physics
        self.wafriction = 0.04
        self.frictionVar = 0.05
        self.mass = 7 # Saints Number
        self.gravity = 10
        self.basefriction = 1
        self.tuples = tuples
        self.equations = equations

        pyg.sprite.Sprite.__init__(self)
        self.image = None
        self.imgclean = pyg.image.load(os.path.join('game', 'car.png')).convert()
        self.imgclean.set_colorkey((34, 177, 76))
        self.rect = self.imgclean.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rects = rects
        self.mapguide = mapguide
        self.state = state
        self.screen = screen

    def update(self):
            self.image = pyg.transform.rotate(self.imgclean, self.angle)
            self.rect = self.image.get_rect(center = (self.x, self.y))



    def drive(self, acceleration, turnout):
        #turn
        if turnout == 0:
            self.angle += self.angularSpeed
        elif turnout == 1:
            self.angle -= self.angularSpeed

        #meil pole ju vaja resultanti??

        # find new speed
        self.speed += acceleration
        self.xSpeed += -m.sin(m.radians(self.angle)) * self.speed
        self.ySpeed += -m.cos(m.radians(self.angle)) * self.speed


        # speedAngle = m.atan(self.xSpeed / self.ySpeed)

        # apply friction
        #print(self.speed)
        try:
            if self.speed > 0.01 or self.speed < -0.01:
                self.speed = self.speed - self.speed * self.wafriction
            else:
                self.speed = 0
        except:
            pass

        try:
            if self.xSpeed > 0.01 or self.xSpeed < -0.01:
                self.xSpeed = self.xSpeed - self.xSpeed * self.frictionVar
            else:
                self.xSpeed = 0
        except:
            pass
        try:
            if self.ySpeed > 0.01 or self.ySpeed < -0.01:
                self.ySpeed = self.ySpeed - self.ySpeed * self.frictionVar
            else:
                self.ySpeed = 0
        except:
            pass
        """
        friction = self.mass * self.gravity * self.frictionVar
        xFriction = -m.sin(speedAngle) * friction
        yFriction = -m.cos(speedAngle) * friction

        self.xSpeed += xFriction
        self.ySpeed += yFriction
        """
        # find new location
        #print(self.angle, self.x, self.y, self.xSpeed, self.ySpeed)
        self.x += self.xSpeed
        self.y += self.ySpeed

        # check crash, TODO

        if self.haveCrashed(self.mapguide, self.state, self.screen):
            self.x = self.startX
            self.y = self.startY
            self.speed = 0
            self.ySpeed = 0
            self.xSpeed = 0
            self.angle = 270
        #print("shit")



    # checking if we've crashed

    def haveCrashed(self, mapguide, state, screen):
        #hopefully we havent
        # map index



        rects = self.rects.copy()
        mapguide2 = mapguide.copy()
        i = 0
        while len(mapguide2) != 0:
            if mapguide[i] == 4 or mapguide[i] == 6:
                for j in range(4):
                    if intersection3(rects.pop(0), self.rect, i, state, screen):
                        print("CRASHED:", mapguide[i])
                        return True
                i += 1
            else:
                for j in range(2):
                    if intersection3(rects.pop(0), self.rect, i, state, screen):
                        print("CRASHED:", mapguide[i])
                        return True
                i += 1
            mapguide2.pop(0)
        return False

        """        
        index = 0
        for rect in self.rects:
            if intersection2(rect, self.rect, mapguide[index]):
                return True

        return False
        """

        #return False

"""
        # implementing
        # F
        # F_R
        # R
        # B_R
        # B
        # B_L
        # L
        # F_L
        angles = [
        self.angle,
        self.angle - 90 + 26.565,
        self.angle - 90,
        self.angle - 180 + 26.565,
        self.angle - 180,
        self.angle - 270 + 26.565,
        self.angle - 270,
        self.angle + 26.565
        ]
        front_ray = ((self.x, self.y), point_generator(angles[0], 20, self.x, self.y))
        front_right_ray = ((self.x, self.y), point_generator(angles[1], m.sqrt(20**2 + 10**2), self.x, self.y))
        right_ray = ((self.x, self.y), point_generator(angles[2], 10, self.x, self.y))
        back_right_ray = ((self.x, self.y), point_generator(angles[3], m.sqrt(20**2 + 10**2), self.x, self.y))
        back_ray = ((self.x, self.y), point_generator(angles[4], 20, self.x, self.y))
        back_left_ray = ((self.x, self.y), point_generator(angles[5], m.sqrt(20**2 + 10**2), self.x, self.y))
        left_ray = ((self.x, self.y), point_generator(angles[6], 10, self.x, self.y))
        front_left_ray = ((self.x, self.y), point_generator(angles[7], m.sqrt(20**2 + 10**2), self.x, self.y))

        corners = [point_generator(angles[1], m.sqrt(20**2 + 10**2), self.x, self.y), point_generator(angles[3], m.sqrt(20**2 + 10**2), self.x, self.y), point_generator(angles[5], m.sqrt(20**2 + 10**2), self.x, self.y), point_generator(angles[7], m.sqrt(20**2 + 10**2), self.x, self.y)]

        e_front_ray = equation_generator(front_ray[0], front_ray[1])
        e_front_right_ray = equation_generator(front_right_ray[0], front_left_ray[1])
        e_right_ray = equation_generator(right_ray[0], right_ray[1])
        e_back_right_ray = equation_generator(back_right_ray[0], back_right_ray[1])
        e_back_ray = equation_generator(back_ray[0], back_ray[1])
        e_back_left_ray = equation_generator(back_left_ray[0], back_left_ray[1])
        e_left_ray = equation_generator(left_ray[0], left_ray[1])
        e_front_left_ray = equation_generator(front_left_ray[0], front_left_ray[1])

        closestValue = [999999999999, 999999999999, 999999999999, 999999999999, 999999999999, 999999999999, 999999999999, 999999999999]

        print("--------------------------")
        for i, equation in enumerate(self.equations):
            pointLoc = []
            # leiame ristumispunktid
            pointLoc.append(intersection(e_front_ray[0], e_front_ray[1], equation[0], equation[1]))
            pointLoc.append(intersection(e_front_right_ray[0], e_front_right_ray[1], equation[0], equation[1]))
            pointLoc.append(intersection(e_right_ray[0], e_right_ray[1], equation[0], equation[1]))
            pointLoc.append(intersection(e_back_right_ray[0], e_back_right_ray[1], equation[0], equation[1]))
            pointLoc.append(intersection(e_back_ray[0], e_back_ray[1], equation[0], equation[1]))
            pointLoc.append(intersection(e_back_left_ray[0], e_back_left_ray[1], equation[0], equation[1]))
            pointLoc.append(intersection(e_left_ray[0], e_left_ray[1], equation[0], equation[1]))
            pointLoc.append(intersection(e_front_left_ray[0], e_front_left_ray[1], equation[0], equation[1]))

            # leiame ristumispunktide kaugused ning võtame neist lähima
            pointLocDist = []
            for intersect in pointLoc:
                #print(self.tuples[i])
                pointLocDist.append(intersect_check(self.tuples[i], (self.x, self.y), intersect))
            #print(pointLocDist)
            closest = min(pointLocDist, key=abs)
            closestIndex = pointLocDist.index(closest)

            if abs(closestValue[closestIndex]) > abs(closest):
                closestValue[closestIndex] = closest
            #print(pointLoc)
            print("Closest:" + str(closest))
            if closestIndex % 4 == 0:
                if abs(closest) < 20:
                    print("CRASHED mod 4")
            elif closestIndex % 2 == 0:
                if abs(closest) < 10:
                    print("CRASHED mod 2")
            else:
                if abs(closest) < m.sqrt(20**2 + 10**2):
                    print("CRASHED other")


"""

