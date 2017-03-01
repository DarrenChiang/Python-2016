import pygame as pg
import sys

sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')

from Sprite import Sprite_Plus

grey = (80, 80, 80)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

def drawLights(win, state):
    r = 100
    if state == 'start':
        pg.draw(win, grey, (400, 100), r)
        pg.draw(win, grey, (400, 300), r)
        pg.draw(win, grey, (400, 500), r)
    elif state == 'go':
        pg.draw(win, grey, (400, 100), r)
        pg.draw(win, grey, (400, 300), r)
        pg.draw(win, green, (400, 500), r)
    elif state == 'slow':
        pg.draw(win, grey, (400, 100), r)
        pg.draw(win, yellow, (400, 300), r)
        pg.draw(win, grey, (400, 500), r)
    elif state == 'stop':
        pg.draw(win, red, (400, 100), r)
        pg.draw(win, grey, (400, 300), r)
        pg.draw(win, grey, (400, 500), r)

pg.init()

window_size = (800, 600)

window = pg.display.set_mode(window_size)

pg.display.set_caption('Traffic Light')

clock = pg.time.Clock()

game_on = True

allSprites = pg.sprite.Group()

frame_info = {'dimensions': (200, 600),
              'color': (0, 0, 0),
              'coordinate': (300, 0)}

frame = Sprite_Plus(frame_info)

allSprites.add(frame)

time_elapsed = 0

state = 'start'

while game_on:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False
        elif event.type == pg.KEYDOWN:
            if event.key == 
            
    window.fill((255, 255, 255))

    allSprites.update()
    allSprites.draw(window)

    drawLights(win, state)

    pg.display.flip()
    clock.tick(60)
