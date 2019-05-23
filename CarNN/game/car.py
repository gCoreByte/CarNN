import math as m
import pygame as pyg
import os

class Car(pyg.sprite.Sprite):

    #initialize variables

    def __init__(self, x, y, surface, angle = 270):

        #current pos
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
        self.maxSpeed = 42069
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

    def drive(self, acceleration, turnout,  Map):
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
        print(self.speed)
        try:
            if self.speed > 0.01 or self.speed < -0.01:
                self.speed = self.speed - self.speed * self.wafriction
            else:
                self.speed = 0
        except:
            None

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

        self.haveCrashed(Map)


    # checking if we've crashed

    def haveCrashed(self, Map):
        #hopefully we havent
        #TODO
        return False

        # implementing rays

        #for func in Map.genfunc:



