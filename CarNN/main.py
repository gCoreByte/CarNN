import pygame as pyg
from CarNN.game import Car
from CarNN.game import track
import copy

pyg.display.init()
screen = pyg.display.set_mode((1440, 900))
pyg.display.set_caption("Simulation")

all_sprites = pyg.sprite.Group()
rects = track(screen)
car = Car(400, 830, rects, screen)
all_sprites.add(car)

run = True
while run:
    AIdrive = True
    enableKeys = True
    pyg.time.wait(6)
    acceleration = 0
    turnout = None
    screen.fill((0, 0, 0))
    track(screen)
    all_sprites.update()
    all_sprites.draw(screen)
    pyg.display.update()
    if enableKeys: 
            keys = pyg.key.get_pressed()
            if keys[pyg.K_RIGHT]:
                turnout = 1
            if keys[pyg.K_LEFT]:
                turnout = 0
            if keys[pyg.K_UP]:
                acceleration += 0.015
            if keys[pyg.K_DOWN]:
                acceleration -= 0.03
    if AIdrive: 
         turnout, acceleration = car.AI.act()
    car.drive(acceleration, turnout)
    car.AI.currentScore += acceleration
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            break

file = open("Parameetrid", "w")
maxIndex = car.AI.previousScores.index(max(car.AI.previousScores))
maxScore = max(car.AI.previousScores)
previousBestActions = copy.deepcopy(car.AI.previousActions[maxIndex])
file.write(str(maxScore))
file.write("\n" + str(previousBestActions))
file.close()
pyg.quit()
