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
        self.xSpeed = 0
        self.ySpeed = 0
        #max, min for acceleration, speed
        self.maxAcceleration = 10
        self.maxSpeed = 42069
        #angles
        self.preangle = 0 #what angle the car has before rotation
        self.angle = angle
        self.angularSpeed = 1
        self.maxAngularSpeed = 1 #???
        #physics
        self.frictionVar = 0.8
        self.mass = 7 # Saints Number
        self.gravity = 10
        self.basefriction = 1

        pyg.sprite.Sprite.__init__(self)
        self.image = pyg.image.load(os.path.join('game', 'car.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.image = pyg.transform.rotate(self.image, self.angle - self.preangle)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.preangle = self.angle

    #turning function

    def turn(self, angularspeed):
        if turnout == 0:
            self.angle += angularspeed
        elif turnout == 1:
            self.angle -= angularspeed


        #accelerationAngle = self.angle
        #while accelerationAngle > 90:
        #   accelerationAngle -= 90
        #return m.radians(accelerationAngle)

    #drive, movement function

    def drive(self, acceleration, Map):

        #turn
        turn(self.angularSpeed)

        # get new Acceleration vector

        xAcceleration = m.sin(self.angle) * acceleration
        yAcceleration = m.cos(self.angle) * acceleration
        #self.rAcceleration += m.sqrt(self.xAcceleration**2 + self.yAcceleration**2)
        #meil pole ju vaja resultanti??

        # find new speed

        self.xSpeed += xAcceleration
        self.ySpeed += yAcceleration

        speedAngle = m.atan(self.xSpeed / self.ySpeed)

        # apply friction

        friction = self.mass * self.gravity * self.frictionVar
        xFriction = -m.sin(speedAngle) * friction - self.basefriction
        yFriction = -m.cos(speedAngle) * friction - self.basefriction

        self.xSpeed += xFriction
        self.ySpeed += yFriction

        # find new location

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



