import pygame as pyg
from game import Car
from game import track

pyg.display.init()
screen = pyg.display.set_mode((1440, 900))
pyg.display.set_caption("Simulation")

all_sprites = pyg.sprite.Group()
tuples, equations = track(screen)
car = Car(400, 830, tuples, equations)
all_sprites.add(car)

run = True
while run:
    pyg.time.wait(6)
    acceleration = 0
    turnout = None
    screen.fill((0, 0, 0))
    track(screen)
    all_sprites.update()
    all_sprites.draw(screen)
    pyg.display.update()
    keys = pyg.key.get_pressed()
    if keys[pyg.K_RIGHT]:
        turnout = 1
    if keys[pyg.K_LEFT]:
        turnout = 0
    if keys[pyg.K_UP]:
        acceleration += 0.015
    if keys[pyg.K_DOWN]:
        acceleration -= 0.03
    car.drive(acceleration, turnout)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            break

pyg.quit()