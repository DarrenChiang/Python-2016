import pygame as pg
import math
import sys
sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')

from Sprite import Sprite_Plus
from Environments import Group_Plus

def updateMovement(mousePos, sprite):
    spd = 2
    mX, mY = mousePos
    sX = sprite.getX() + sprite.getWidth() / 2
    sY = sprite.getY() + sprite.getHeight() / 2
    dx = mX - sX
    dy = mY - sY
    angle = math.atan2(dy, dx)
    sprite.setVerticalSpeed(math.sin(angle) * spd)
    sprite.setHorizontalSpeed(math.cos(angle) * spd)

pg.init()

window = pg.display.set_mode((800, 600))

pg.display.set_caption('Mouse Follower')

clock = pg.time.Clock()

spriteList = Group_Plus()

spr_info = {'dimensions': (50, 50),
            'color': (255, 0, 0)}
            
follower = Sprite_Plus(spr_info)

follower.center(window)

spriteList.add(follower)

game_on = True

m_click = False

while game_on:
    window.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            m_Coord = pg.mouse.get_pos()
            m_click = True
        elif event.type == pg.MOUSEBUTTONUP:
            m_click = False

    if m_click:
        updateMovement(m_Coord, follower)

    spriteList.update()

    spriteList.draw(window)

    pg.display.flip()
    clock.tick(60)
