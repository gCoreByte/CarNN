import random
import pygame as pg

class Map:
    def __init__(self, generateAuto=True, x=1024, y=1024, width=36):
        self.x = x
        self.y = y
        self.generateMap()
    def generateMap(self):
        mapChunks = self.generateChunks()

    def generateChunks(self, screen):
        def straightVertical(screen, start_x, start_y):
            pg.draw.line(screen, (start_x, start_y), (start_x, start_y + 256))
            pg.draw.line(screen, (start_x + 256, start_y), (start_x + 256, start_y + 256))
        def straightHorizontal(screen, start_x, start_y):
            pg.draw.line(screen, (start_x, start_y), (start_x + 256, start_y))
            pg.draw.line(screen, (start_x, start_y + 256), (start_x + 256, start_y))
        def turnRight(screen, start_x, start_y):
            pg.draw.line(screen, (start_x, start_y + 256), (start_x, start_y + 128))
            pg.draw.line(screen, (start_x, start_y + 128), (start_x + 128, start_y))
            pg.draw.line(screen, (start_x + 128, start_y), (start_x + 256, start_y))
        def turnBRight(screen, start_x, start_y):
            pg.draw.line(screen, (start_x, start_y), (start_x, start_y + 128))
            pg.draw.line(screen, (start_x, start_y + 128), (start_x + 128, start_y + 256))
            pg.draw.line(screen, (start_x + 128, start_y + 256), (start_x + 256, start_y + 256))
        def turnLeft(screen, start_x, start_y):
            pg.draw.line(screen, (start_x, start_y), (start_x + 128, start_y))
            pg.draw.line(screen, (start_x + 128, start_y), (start_x + 256, start_y + 128))
            pg.draw.line(screen, (start_x + 256, start_y + 128), (start_x + 256, start_y + 256))
        def turnBLeft(screen, start_x, start_y):
            pg.draw.line(screen, (start_x + 256, start_y), (start_x + 256, start_y + 128))
            pg.draw.line(screen, (start_x + 256, start_y + 128), (start_x + 128, start_y + 256))
            pg.draw.line(screen, (start_x + 128, start_y + 256), (start_x, start_y + 256))

        mapChunksPossible = [straightVertical, straightHorizontal, turnRight, turnLeft, turnBRight, turnBLeft]
        # meil on 6 osa - 2 sirget, 4 pööret
        # teades, et meie max suurus on 1024x1024, võtame ühe osa suuruseks 256, nii max 4 järjest.
        # alustame alati 1-0 (x-y, y = 0 üleval)
        x = 1
        y = 0

        mapChunksFinal = [[None] * 4, [None] * 4, [None] * 4, [None] * 4]
        # alustame alati sirgelt, mis liigub horisontaalselt
        mapChunksFinal[y[x]] = mapChunksPossible[1](screen, x, y)
        # liigume paremale
        x += 1
        # alustame suvalist generatsiooni
        trackUnfinished = True
        while trackUnfinished:
            if x == 1 and y == 0:
                trackUnfinished = False
                break
            if (x != 4 and y != 4 and x != 0 and y != 0):
                if

