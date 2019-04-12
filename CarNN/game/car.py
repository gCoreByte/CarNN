import math as m

class Car:

    #initialize variables

    def __init__(self, x, y, angle):

        #current pos
        self.x = x
        self.y = y
        #current x, y speed
        self.xSpeed = 0
        self.ySpeed = 0
        #current x, y acceleration
        self.xAcceleration = 0
        self.yAcceleration = 0
        #max, min for acceleration, speed
        self.maxAcceleration = 10
        self.maxSpeed = 42069
        self.minSpeed = -1
        #current acceleration
        #self.rAcceleration = 0
        self.accelerationAngle = 0
        #angles
        self.angle = angle
        self.angularSpeed = 0
        self.maxAngularSpeed = 1


    #drive, movement function

    def drive(self, acceleration, angular):

        #turn
        self.turn(angular)

        # get new rAcceleration vector

        self.xAcceleration += m.sin(self.accelerationAngle) * acceleration
        self.yAcceleration += m.cos(self.accelerationAngle) * acceleration
        #self.rAcceleration += m.sqrt(self.xAcceleration**2 + self.yAcceleration**2)
        #meil pole ju vaja resultanti??

        # find new speed

        self.xSpeed += self.xAcceleration
        self.ySpeed += self.yAcceleration

        # find new location

        self.x += self.xSpeed
        self.y += self.ySpeed

        # check crash, TODO

        self.haveCrashed()

    #turning, handles angular speed, accelerationAngle

    def turn(self, angular):
        self.angle += angular
        self.accelerationAngle = 360
        while self.accelerationAngle > 90:
            self.accelerationAngle -= 90

        """
        angularSpeed = self.angle - desiredAngle
        if self.angularSpeed > self.maxAngularSpeed:
            self.angularSpeed = self.maxAngularSpeed
        elif abs(self.angularSpeed) > self.maxAngularSpeed:
            self.angularSpeed = -self.maxAngularSpeed
        self.angle += angularSpeed
        """

    # checking if we've crashed

    def haveCrashed(self):
        #hopefully we havent
        #TODO
        return False
