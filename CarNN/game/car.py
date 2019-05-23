import math as m
import pygame as pyg
import os
from .util import line_intersection, point_distance

class Car(pyg.sprite.Sprite):

    #initialize variables

    def __init__(self, x, y, tuples, angle = 270):

        #current pos
        self.x = x
        self.y = y
        self.width = 20
        self.height = 40
        #current x, y speed
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
        self.frictionVar = 0.025
        self.mass = 7 # Saints Number
        self.gravity = 10
        self.basefriction = 1
        self.tuples = tuples

        pyg.sprite.Sprite.__init__(self)
        self.image = None
        self.imgclean = pyg.image.load(os.path.join('game', 'car.png')).convert()
        self.imgclean.set_colorkey((34, 177, 76))
        self.rect = self.imgclean.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
            self.image = pyg.transform.rotate(self.imgclean, self.angle)
            self.rect = self.image.get_rect(center = (self.x, self.y))

    #turning function
    """
    def turn(self, angularspeed):
        if turnout == 0:
            self.angle += angularspeed
        elif turnout == 1:
            self.angle -= angularspeed
    """

        #accelerationAngle = self.angle
        #while accelerationAngle > 90:
        #   accelerationAngle -= 90
        #return m.radians(accelerationAngle)

    #drive, movement function

    def drive(self, acceleration, turnout):
        #turn
        if turnout == 0:
            self.angle += self.angularSpeed
        elif turnout == 1:
            self.angle -= self.angularSpeed
        # get new Acceleration vector

        xAcceleration = -m.sin(m.radians(self.angle)) * acceleration
        yAcceleration = -m.cos(m.radians(self.angle)) * acceleration
        #self.rAcceleration += m.sqrt(self.xAcceleration**2 + self.yAcceleration**2)
        #meil pole ju vaja resultanti??

        # find new speed
        #print(acceleration, xAcceleration, yAcceleration)
        self.xSpeed += xAcceleration
        self.ySpeed += yAcceleration


        # speedAngle = m.atan(self.xSpeed / self.ySpeed)

        # apply friction
        try:
            if self.xSpeed > 0.01 or self.xSpeed < -0.01:
                self.xSpeed = self.xSpeed - self.xSpeed * self.frictionVar
            else:
                self.xSpeed = 0
        except:
            None
        try:
            if self.ySpeed > 0.01 or self.ySpeed < -0.01:
                self.ySpeed = self.ySpeed - self.ySpeed * self.frictionVar
            else:
                self.ySpeed = 0
        except:
            None
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

        self.haveCrashed()


    # checking if we've crashed

    def haveCrashed(self):
        #hopefully we havent
        #TODO
        #return False

        # implementing rays
        front_ray = None
        front_right_ray = None
        right_ray = None
        back_right_ray = None
        back_ray = None
        back_left_ray = None
        left_ray = None
        front_left_ray = None

        closestValue = [0, 0, 0, 0, 0, 0, 0, 0]

        for i, line in enumerate(self.tuples):
            pointLoc = []
            pointLoc.append(line_intersection(line, front_ray))
            pointLoc.append(line_intersection(line, front_right_ray))
            pointLoc.append(line_intersection(line, right_ray))
            pointLoc.append(line_intersection(line, back_right_ray))
            pointLoc.append(line_intersection(line, back_ray))
            pointLoc.append(line_intersection(line, back_left_ray))
            pointLoc.append(line_intersection(line, left_ray))
            pointLoc.append(line_intersection(line, front_left_ray))

            for j, point in enumerate(pointLoc):
                if closestValue[j][0] > point_distance(point, (self.x, self.y)):
                    closestValue[j] = [point_distance(point, (self.x, self.y)), i]
                    



