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

def intersection(rect1, rect2, screen):
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
            return True
    return False

