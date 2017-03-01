import pygame as pg
import sys

sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')

from Sprite import Character
from Environments import Platformer

pg.init()

window_size = (800, 600)

window = pg.display.set_mode(window_size)

pg.display.set_caption('Jumping Link')

clock = pg.time.Clock()

game_on = True

allSprites = Platformer({'gravity': 5})

char_info = {'name': 'Link',
             'dimensions': (100, 100),
             'max hp': 100}

sprite1 = Character(char_info)

sprite1.addImage(pg.image.load('Images\\Standing.png'))
sprite1.addImage(pg.image.load('Images\\Jumping.png'))
sprite1.addImage(pg.image.load('Images\\Ducking.png'))
sprite1.adjustImages()
    
sprite1.setCoordinate((400 - sprite1.getWidth(), 300 - sprite1.getHeight()))

allSprites.add(sprite1)

state = 'standing'
pause = 0

while game_on:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False
            
    window.fill((255, 255, 255))

    keys = pg.key.get_pressed()

    if pause < 30:
        pause += 1

    if keys[pg.K_s]:
        if state != 'jump1' and state != 'jump2':
            sprite1.setImage(2)
            state = 'ducking'
    elif keys[pg.K_w]:
        if state == 'standing':
            sprite1.setVerticalSpeed(-50)
            sprite1.setImage(1)
            state = 'jump1'
        elif state == 'jump1' and pause > 10:
            sprite1.setVerticalSpeed(-30)
            state = 'jump2'
        pause = 0

    if sprite1.getBottom() >= 600:
        state = 'standing'
        sprite1.setImage(0)
    
    allSprites.update()

    allSprites.draw(window)

    pg.display.flip()
    clock.tick(60)
