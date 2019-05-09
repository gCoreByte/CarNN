import pygame as pyg
from game import Car


pyg.display.init()
screen = pyg.display.set_mode((1440, 900))
pyg.display.set_caption("Simulation")

all_sprites = pyg.sprite.Group()
car = Car(500, 500, pyg.display)
all_sprites.add(car)

run = True
while run:
    all_sprites.update()
    all_sprites.draw(screen)
    pyg.display.update()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()


