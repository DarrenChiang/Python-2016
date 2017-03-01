import pygame as pg
import sys
sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')

from Sprite import Character
from Environments import Group_Plus

def keyInput():
    keys = pg.key.get_pressed()
    state = None
    
    if keys[pg.K_w]:
        state = 'u'
    elif keys[pg.K_s]:
        state = 'd'
    elif keys[pg.K_d]:
        state = 'r'
    elif keys[pg.K_a]:
        state = 'l'

    return state


def walk(sprite, state, spd, count):
    vSpd = 0
    hSpd = 0
    if state == 'u':
        vSpd = -spd
        #use image set x
    elif state == 'd':
        vSpd = spd
        #use image set x
    elif state == 'r':
        hSpd = spd
        #use image set x
    elif state == 'l':
        hSpd = -spd
        #use image set x

    sprite.setVerticalSpeed(vSpd)
    sprite.setHorizontalSpeed(hSpd)

def alternate(count):
    count += 1
    if count > 4:
        count = 1

pg.init()

window = pg.display.set_mode((800, 600))

pg.display.set_caption('2D Game')

clock = pg.time.Clock()

sprites = Group_Plus()

char_info = {'name': 'Bob',
             'dimensions': (35, 45),
             'max hp': 100,
             'color': (0, 0, 0)}

char1 = Character(char_info)

char1.setCoordinate((400 - char1.getWidth() / 2, 300 - char1.getHeight() / 2))

sprites.add(char1)

game_on = True

count = 0

while game_on:
    window.fill((255, 255, 255))

    alternate(count)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False

    state = keyInput()

    if state != None:
        count = 0

    walk(char1, state, 3, count)

    sprites.update()

    sprites.draw(window)

    pg.display.flip()
    clock.tick(60)
