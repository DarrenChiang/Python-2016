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
        sprite.setListImage(1)
        sprite.animation_On(True)
        sprite.useAnimation(state)
    elif state == 'Down':
        vSpd = spd
        sprite.setListImage(0)
        sprite.animation_On(True)
        sprite.useAnimation(state)
    elif state == 'Right':
        hSpd = spd
        sprite.setListImage(3)
        sprite.animation_On(True)
        sprite.useAnimation(state)
    elif state == 'Left':
        hSpd = -spd
        sprite.setListImage(2)
        sprite.animation_On(True)
        sprite.useAnimation(state)
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

d1 = pg.image.load('Images\\Down1.png').convert_alpha()
d2 = pg.image.load('Images\\Down2.png').convert_alpha()
d3 = pg.image.load('Images\\Down3.png').convert_alpha()
u1 = pg.image.load('Images\\Up1.png').convert_alpha()
u2 = pg.image.load('Images\\Up2.png').convert_alpha()
u3 = pg.transform.flip(u2, True, False)

l1 = pg.image.load('Images\\Left1.png').convert_alpha()
l2 = pg.image.load('Images\\Left2.png').convert_alpha()
l3 = pg.image.load('IMages\\Left3.png').convert_alpha()

r1 = pg.image.load('Images\\Right1.png').convert_alpha()
r2 = pg.image.load('Images\\Right2.png').convert_alpha()
r3 = pg.image.load('Images\\Right3.png').convert_alpha()

an1 = Animation('Down', 40, [d2, d1, d3, d1])
an1.adjustImages(char1)

an2 = Animation('Up', 40, [u2, u1, u3, u1])
an2.adjustImages(char1)

an3 = Animation('Left', 40, [l2, l1, l3, l1])
an3.adjustImages(char1)

an4 = Animation('Right', 40, [r2, r1, r3, r1])
an4.adjustImages(char1)

char1.addImage(d1)
char1.addImage(u1)
char1.addImage(l1)
char1.addImage(r1)
char1.adjustImages()
char1.setListImage(0)

char1.createAnimationSet([an1, an2, an3, an4])

char1.center(window)

sprites.add(char1)

game_on = True

while game_on:
    window.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False

    state = keyInput()

    walk(char1, state, 1)

    sprites.update()

    sprites.draw(window)

    pg.display.flip()
    clock.tick(60)
