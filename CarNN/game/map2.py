import pygame as pyg

def track(screen):
    # Create the map. Todd Howard - "It just works."
    xmap = 770
    ymap = 800
    goingright = True
    goingleft = False
    goingup = False
    goingdown = False

    #1 - road
    #2 - soft turn counterclockwise
    #3 - soft turn clockwise
    #4 - hard turn counterclockwise
    #5 - half road
    #6 - hard turn clockwise



    mapguide = [1,5,4,1,5,2,2,1,6,6,1,2,5,2,1,5,4,1]
    tuples = []
    #mapguide2
    #mapguide3

    Maptime = True
    while Maptime == True:

        try:
            build = mapguide.pop(0)
        except:
            Maptime = False
            build = None

        done = False

    #Checks the direction the road is going and sets parameters accordingly

        if goingright:
            xmove = 270
            ymove = 0
            ywidth = 90
            xwidth = 0
        if goingup:
            xmove = 0
            ymove = -270
            ywidth = 0
            xwidth = 90
        if goingleft:
            xmove = -270
            ymove = 0
            ywidth = -90
            xwidth = 0
        if goingdown:
            xmove = 0
            ymove = 270
            ywidth = 0
            xwidth = -90

    #straight road
        if build == 1:
            pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + xmove, ymap + ymove), 5)
            pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth), 5)
            tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
            tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
            xmap = xmap + xmove
            ymap = ymap + ymove

    #straight halfroad
        if build == 5:
            pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + xmove/2, ymap + ymove/2), 5)
            pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xmove/2 + xwidth, ymap + ymove/2 + ywidth), 5)
            tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
            tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
            xmap = xmap + xmove/2
            ymap = ymap + ymove/2

    #turnleft
        if build == 2 and not done: #soft
            if goingright:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + 90, ymap - 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth + 180, ymap + ywidth - 180), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap + 90
                ymap = ymap - 90
                goingup = True
                goingright = False
                done = True

            if goingleft and not done:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap - 90, ymap + 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth - 180, ymap + ywidth + 180), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap - 90
                ymap = ymap + 90
                goingdown = True
                goingleft = False
                done = True

            if goingup and not done:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap - 90, ymap - 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth - 180, ymap + ywidth - 180), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap - 90
                ymap = ymap - 90
                goingleft = True
                goingup = False
                done = True

            if goingdown and not done:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + 90, ymap + 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth + 180, ymap + ywidth + 180), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap + 90
                ymap = ymap + 90
                goingdown = True
                goingright = False
                done = True

    #turnright
        if build == 3:  #soft
            if goingright:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + 180, ymap + 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth + 90, ymap + ywidth + 90), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap + 180
                ymap = ymap + 180
                goingdown = True
                goingright = False
                done = True

            if goingleft and not done:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap - 180, ymap - 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth - 90, ymap + ywidth - 90), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap - 180
                ymap = ymap - 180
                goingup = True
                goingleft = False
                done = True

            if goingup and not done:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + 180, ymap - 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth + 90, ymap + ywidth - 90), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap + 180
                ymap = ymap - 180
                goingright = True
                goingup = False
                done = True

            if goingdown and not done:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap - 180, ymap + 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth - 90, ymap + ywidth + 90), 5)
                tuples.append(((xmap, ymap), (xmap + xmove, ymap + ymove)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xmove + xwidth, ymap + ymove + ywidth)))
                xmap = xmap - 180
                ymap = ymap + 180
                goingup = True
                goingright = False
                done = True

    #turnlefthard
        if build == 4: #hard
            if goingright and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + 90, ymap), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + 90, ymap), (xmap + 90, ymap - 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth + 180, ymap + ywidth), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth + 180, ymap + ywidth), (xmap + xwidth + 180, ymap + ywidth - 180), 5)
                tuples.append(((xmap, ymap), (xmap + 90, ymap)))
                tuples.append(((xmap + 90, ymap), (xmap + 90, ymap - 90)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth + 180, ymap + ywidth)))
                tuples.append(((xmap + xwidth + 180, ymap + ywidth), (xmap + xwidth + 180, ymap + ywidth - 180)))
                ymap = ymap - 90
                xmap = xmap + 90
                goingup = True
                goingright = False
                done = True

            if goingleft and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap - 90, ymap), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap - 90, ymap), (xmap - 90, ymap + 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth - 180, ymap + ywidth), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth - 180, ymap + ywidth), (xmap + xwidth - 180, ymap + ywidth + 180), 5)
                tuples.append(((xmap, ymap), (xmap - 90, ymap)))
                tuples.append(((xmap - 90, ymap), (xmap - 90, ymap + 90)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth - 180, ymap + ywidth)))
                tuples.append(((xmap + xwidth - 180, ymap + ywidth), (xmap + xwidth - 180, ymap + ywidth + 180)))
                ymap = ymap + 90
                xmap = xmap - 90
                goingdown = True
                goingleft = False
                done = True

            if goingup and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap, ymap - 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap - 90), (xmap - 90, ymap - 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth - 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth - 180), (xmap + xwidth - 180, ymap + ywidth - 180), 5)
                tuples.append(((xmap, ymap), (xmap, ymap - 90)))
                tuples.append(((xmap, ymap - 90), (xmap - 90, ymap - 90)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth - 180)))
                tuples.append(((xmap + xwidth, ymap + ywidth - 180), (xmap + xwidth - 180, ymap + ywidth - 180)))
                ymap = ymap - 90
                xmap = xmap - 90
                goingleft = True
                goingup = False
                done = True

            if goingdown and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap, ymap + 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap + 90), (xmap + 90, ymap + 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth + 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth + 180), (xmap + xwidth + 180, ymap + ywidth + 180), 5)
                tuples.append(((xmap, ymap), (xmap, ymap + 90)))
                tuples.append(((xmap, ymap + 90), (xmap + 90, ymap + 90)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth + 180)))
                tuples.append(((xmap + xwidth, ymap + ywidth + 180), (xmap + xwidth + 180, ymap + ywidth + 180)))
                ymap = ymap + 90
                xmap = xmap + 90
                goingright = True
                goingdown = False
                done = True

    #turnrighthard
        if build == 6: #hard
            if goingright and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap + 180, ymap), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + 180, ymap), (xmap + 180, ymap + 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth + 90, ymap + ywidth), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth + 90, ymap + ywidth), (xmap + xwidth + 90, ymap + ywidth + 90), 5)
                tuples.append(((xmap, ymap), (xmap + 180, ymap)))
                tuples.append(((xmap + 180, ymap), (xmap + 180, ymap + 180)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth + 90, ymap + ywidth)))
                tuples.append(((xmap + xwidth + 90, ymap + ywidth), (xmap + xwidth + 90, ymap + ywidth + 90)))
                ymap = ymap + 180
                xmap = xmap + 180
                goingdown = True
                goingright = False
                done = True

            if goingleft and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap - 180, ymap), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap - 180, ymap), (xmap - 180, ymap - 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth - 90, ymap + ywidth), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth - 90, ymap + ywidth), (xmap + xwidth - 90, ymap + ywidth - 90), 5)
                tuples.append(((xmap, ymap), (xmap - 180, ymap)))
                tuples.append(((xmap - 180, ymap), (xmap - 180, ymap - 180)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth - 90, ymap + ywidth)))
                tuples.append(((xmap + xwidth - 90, ymap + ywidth), (xmap + xwidth - 90, ymap + ywidth - 90)))
                ymap = ymap - 180
                xmap = xmap - 180
                goingup = True
                goingleft = False
                done = True

            if goingup and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap, ymap - 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap - 180), (xmap + 180, ymap - 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth - 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth - 90), (xmap + xwidth + 90, ymap + ywidth - 90), 5)
                tuples.append(((xmap, ymap), (xmap, ymap - 180)))
                tuples.append(((xmap, ymap - 180), (xmap + 180, ymap - 180)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth - 90)))
                tuples.append(((xmap + xwidth, ymap + ywidth - 90), (xmap + xwidth + 90, ymap + ywidth - 90)))
                ymap = ymap - 180
                xmap = xmap + 180
                goingright = True
                goingup = False
                done = True

            if goingdown and done == False:
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap), (xmap, ymap + 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap, ymap + 180), (xmap - 180, ymap + 180), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth + 90), 5)
                pyg.draw.line(screen, (102, 102, 153), (xmap + xwidth, ymap + ywidth + 90), (xmap + xwidth - 90, ymap + ywidth + 90), 5)
                tuples.append(((xmap, ymap), (xmap, ymap + 180)))
                tuples.append(((xmap, ymap + 180), (xmap - 180, ymap + 180)))
                tuples.append(((xmap + xwidth, ymap + ywidth), (xmap + xwidth, ymap + ywidth + 90)))
                tuples.append(((xmap + xwidth, ymap + ywidth + 90), (xmap + xwidth - 90, ymap + ywidth + 90)))
                ymap = ymap + 180
                xmap = xmap - 180
                goingleft = True
                goingdown = False
                done = True
    return tuples