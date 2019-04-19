import random as rnd


class Map:

    def __init__(self, generateAuto=True, x=50000, y=50000, width=36):
        self.x = x
        self.y = y
        self.points = rnd.randint(3, 8)
        self.map = [tuple(self.x, self.y)]

        ymax = self.y
        xmin = self.x
        counter = 0  # how many parts the y axis should be silced in to

        for myfatherisanalcoholic in self.points:  # generates points that will eventaully plot the map
            counter += 1
            if counter == self.corners:
                for i in self.map:
                    # TODO
                    # here cometh last
                    pass
            xpoint = rnd.randint(xmin, 100000)
            ypoint = rnd.randint((ymax - 36), (ymax - ymax / (self.point - counter)))
            self.map.append(tuple(ypoint, xpoint))

        ymax = ypoint