import pygame as pg
import sys
sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')

from Sprite import Character
from Environments import Group_Plus
from Animation import Animation

def keyInput():
    keys = pg.key.get_pressed()
    state = 'Default'    
    if keys[pg.K_w]:
        state = 'Up'
    elif keys[pg.K_s]:
        state = 'Down'
    elif keys[pg.K_d]:
        state = 'Right'
    elif keys[pg.K_a]:
        state = 'Left'
    return state


def walk(sprite, state, spd):
    vSpd = 0
    hSpd = 0
    if state == 'Up':
        vSpd = -spd
        sprite.animation_On(True)
        sprite.useAnimation(state)
    elif state == 'Down':
        vSpd = spd
        sprite.animation_On(True)
        sprite.useAnimation(state)
    elif state == 'Right':
        hSpd = spd
        #use image set x
    elif state == 'Left':
        hSpd = -spd
        #use image set x
    else:
        sprite.animation_On(False)

    sprite.setVerticalSpeed(vSpd)
    sprite.setHorizontalSpeed(hSpd)

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

d1 = pg.image.load('Images\\Down1.png')
d2 = pg.image.load('Images\\Down2.png')
d3 = pg.transform.flip(d2, True, False)

u1 = pg.image.load('Images\\Up1.png')
u2 = pg.image.load('Images\\Up2.png')
u3 = pg.transform.flip(u2, True, False)

an1 = Animation('Down', 30, [d2, d3])
an1.adjustImages(char1)

an2 = Animation('Up', 30, [u2, u3])
an2.adjustImages(char1)

char1.createAnimationSet([an1, an2])

char1.center(window)

sprites.add(char1)

game_on = True

while game_on:
    window.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False

    state = keyInput()

    walk(char1, state, 3)

    sprites.update()

    sprites.draw(window)

    pg.display.flip()
    clock.tick(60)
