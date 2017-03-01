import pygame as pg

import sys

sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')
from Sprite import Character
from Environments import Platformer

pg.init()

window_size = (1000, 1000)

window = pg.display.set_mode(window_size)

pg.display.set_caption('Template')

clock = pg.time.Clock()

game_on = True

allSprites = Platformer({'gravity': 10})

info = {'dimensions': (50, 50),
        'coordinate': (500, 500),
        'color': (0, 0, 0),
        'name': 'Bobby Bob',
        'max hp': 100}

block = Character(info)

allSprites.add(block)

pg.key.set_repeat(5, 5)

while game_on:
    window.fill((255, 255, 255))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                block.changeY(-2)
            elif event.key == pg.K_s:
                block.changeY(2)
            elif event.key == pg.K_d:
                block.changeX(2)
            elif event.key == pg.K_a:
                block.changeX(-2)
        elif event.type == pg.KEYUP:
            pass
                
    allSprites.update()
    allSprites.draw(window)

    pg.display.flip()
    clock.tick(60)
