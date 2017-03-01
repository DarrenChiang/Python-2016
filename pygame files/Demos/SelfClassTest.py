import pygame as pg
import sys

sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes\\Self')
from Sprite import Character

def display(win, system): 
    for spr in system:
        pg.draw.rect(win, spr.getColor(), spr.getCoordinate() + spr.getDimensions(), 0)

def updateSprite(sprite):
    d = sprite.getDirection()
    if d == 'u':
        sprite.setColor(sprite.green)
    elif d == 'd':
        sprite.setColor(sprite.black)
    elif d == 'r':
        sprite.setColor(sprite.red)
    elif d == 'l':
        sprite.setColor(sprite.blue)
    
        
pg.init()

window_size = (800, 700)

window = pg.display.set_mode(window_size)

pg.display.set_caption('Class Test')

clock = pg.time.Clock()

character_info = {'coordinate': (window_size[0] / 2 - 100, window_size[1] / 2 - 100),
                  'dimensions': (100, 100),
                  'name': 'Bobby Bob',
                  'max hp': 100,
                  'direction': 'r'}

spriteList = []

spriteList.append(Character(character_info))

game_on = True

while game_on:
    window.fill((255, 255, 255))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w and spriteList[0].getDirection() != 'u':
                spriteList[0].setDirection('u')
            elif event.key == pg.K_s and spriteList[0].getDirection() != 'd':
                spriteList[0].setDirection('d')
            elif event.key == pg.K_d and spriteList[0].getDirection() != 'r':
                spriteList[0].setDirection('r')
            elif event.key == pg.K_a and spriteList[0].getDirection() != 'l':
                spriteList[0].setDirection('l')
        elif event.type == pg.KEYUP:
            pass

    updateSprite(spriteList[0])
        
    display(window, spriteList)

    pg.display.flip()
    clock.tick(20)
                
                  
