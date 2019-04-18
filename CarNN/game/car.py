import math as m

class Car:

    #initialize variables

    def __init__(self, x, y, angle):

        #current pos
        self.x = x
        self.y = y
        self.width = 10
        self.height = 20
        #current x, y speed
        self.xSpeed = 0
        self.ySpeed = 0
        #max, min for acceleration, speed
        self.maxAcceleration = 10
        self.maxSpeed = 42069
        #angles
        self.angle = angle
        self.angularSpeed = 0
        self.maxAngularSpeed = 1
        #physics
        self.frictionVar = 0.8
        self.mass = 7 # Saints Number
        self.gravity = 10

    #drive, movement function

    def drive(self, acceleration, angular, Map):

        #turn
        accelerationAngle = self.turn(angular)

        # get new rAcceleration vector

        xAcceleration = m.sin(accelerationAngle) * acceleration
        yAcceleration = m.cos(accelerationAngle) * acceleration
        #self.rAcceleration += m.sqrt(self.xAcceleration**2 + self.yAcceleration**2)
        #meil pole ju vaja resultanti??

        # find new speed

        self.xSpeed += xAcceleration
        self.ySpeed += yAcceleration

        speedAngle = m.atan(self.xSpeed / self.ySpeed)

        # apply friction

        friction = self.mass * self.gravity * self.frictionVar
        xFriction = -m.sin(speedAngle) * friction
        yFriction = -m.cos(speedAngle) * friction

        self.xSpeed += xFriction
        self.ySpeed += yFriction

        # find new location

        self.x += self.xSpeed
        self.y += self.ySpeed

        # check crash, TODO

        self.haveCrashed(Map)

    #turning, handles angular speed, accelerationAngle

    def turn(self, angular):
        self.angle += angular

        accelerationAngle = self.angle

        while accelerationAngle > 90:
            accelerationAngle -= 90
        return m.radians(accelerationAngle)

    # checking if we've crashed

    def haveCrashed(self, Map):
        #hopefully we havent
        #TODO
        return False

        # implementing rays

        #for func in Map.genfunc:



