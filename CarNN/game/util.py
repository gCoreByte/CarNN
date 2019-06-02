from math import sqrt, sin, cos, radians
import pygame as pyg
from enum import IntEnum

class Direction(IntEnum):
    UP = 1
    LEFT = 2
    DOWN = -1
    RIGHT = -2

class DirectionSpecific(IntEnum):
    UpDown = 0
    LeftRight = 1
    BottomLeftTopRight = 2
    BottomRightTopLeft = 3

def turn_func(state, index):
    if abs(state[index]) == 1 and abs(state[index - 1] == 1):
        return DirectionSpecific.UpDown
    if abs(state[index]) == 2 and abs(state[index - 1]) == 2:
        return DirectionSpecific.LeftRight
    if abs(state[index] + state[index - 1]) == 1:
        return DirectionSpecific.BottomLeftTopRight
    if abs(state[index] + state[index - 1]) == 3:
        return DirectionSpecific.BottomRightTopLeft

def intersection3(rect1, rect2, index, state, screen):
    if not rect1.colliderect(rect2):
        return False


    lineSegments = 500
    verticalDelta = 0.0
    horizontalDelta = 0.0
    startX = rect1.bottomleft[0]
    startY = rect1.bottomleft[1]
    bg = screen.get_at(rect1.center)
    currentDir = None

    if rect1.width == 5:
        currentDir = DirectionSpecific.UpDown
    elif rect1.height == 5:
        currentDir = DirectionSpecific.LeftRight
    elif screen.get_at((startX, startY)) != bg:
        currentDir = DirectionSpecific.BottomRightTopLeft
    elif screen.get_at((startX, startY)) == bg:
        currentDir = DirectionSpecific.BottomLeftTopRight

    if currentDir == DirectionSpecific.UpDown:
        verticalDelta = rect1.height / lineSegments
    elif currentDir == DirectionSpecific.LeftRight:
        horizontalDelta = rect1.width / lineSegments
    elif currentDir == DirectionSpecific.BottomLeftTopRight:
        horizontalDelta = rect1.width / lineSegments
        verticalDelta = rect1.height / lineSegments
    else:
        horizontalDelta = -rect1.width / lineSegments
        verticalDelta = rect1.height / lineSegments
        startX = rect1.bottomright[0]
        startY = rect1.bottomright[1]
    for i in range(lineSegments):
        posX = startX + i * horizontalDelta
        posY = startY - i * verticalDelta

        if rect2.collidepoint(posX, posY):
            print(currentDir)
            return True
    return False


# ((x1, y1), (x2, y2)) joone formaat
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return False
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

# leiab kahe punkti kauguse
def point_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#leiab punkti läbi siinusteoreemi
def point_generator(angle, hypo_length, x, y):
    return (hypo_length * sin(radians(angle)) + x, hypo_length * cos(radians(angle)) + y)

# leiab võrrandi sirgele
def equation_generator(point1, point2):
    dif_x_1 = point2[0] - point1[0]
    dif_y_1 = point2[1] - point1[1]
    if dif_x_1 == 0:
        return [0, point1[0]]
    if dif_y_1 == 0:
        return [point1[1], 0]
    try:
        equation_a = (point2[1] - point1[1]) / (point2[0] - point1[0])
        equation_c = (point2[1] - point1[1]) * point1[0] / (point2[0] - point1[0])
        return [equation_a, equation_c]
    except:
        print(point1)
        print(point2)
    #return [equation_a, equation_c]


# leiab sirgete ristumiskoha
def intersection(equation_a_a, equation_a_c, equation_b_a, equation_b_c):
    try:
        x = (-equation_a_c + equation_b_c) / (equation_a_a - equation_b_a)
        y = equation_a_a * x + equation_a_c
    except:
        return (9999999, 999999)
    return (x, y)


#1 - road 2
#2 - soft turn counterclockwise 2
#3 - soft turn clockwise 2
#4 - hard turn counterclockwise 4
#5 - half road 2
#6 - hard turn clockwise 4

def turn_func(state, index):
    return abs(state[index] + state[index - 1])


def intersection2(rect1, rect2, index, state):
    if index == 2 or index == 3:
        delta = rect1.width / 300
        turnState = turn_func(state, index)
        if turnState == 1:
            bottom = rect1.bottomleft
            for i in range(1, 301):
                if rect2.collidepoint(bottom[0] + delta * i, bottom[1] - delta * i):
                    return True
        else:
            bottom = rect1.bottomright
            for i in range(1, 301):
                if rect2.collidepoint(bottom[0] - delta * i, bottom[1] - delta * i):
                    return True
        return False
    return rect1.colliderect(rect2)


# leiab ristumiskoha kauguse
def intersect_check(line, start, intersect):
    if (line[0][0] < intersect[0] < line[1][0]) or (line[0][0] > intersect[0] > line[1][0]):
        if (line[0][1] < intersect[1] < line[1][1]) or (line[0][1] > intersect[1] > line[1][1]):
            return point_distance(start, intersect)
    return 999999999999999
