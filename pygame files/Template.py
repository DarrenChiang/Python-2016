import pygame as pg
import sys
sys.insert.path(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')

pg.init()

window = pg.display.set_mode((800, 600))

pg.display.set_caption('template')

clock = pg.time.Clock()

game_on = True

while game_on:
    window.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False




    pg.display.flip()
    clock.tick(60)
