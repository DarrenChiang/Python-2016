import pygame as pg





pg.init()

window_size = (1000, 1000)

window = pg.display.set_mode(window_size)

pg.display.set_caption('Template')

clock = pg.time.Clock()

game_on = True

while game_on:
    window.fill((255, 255, 255))





    pg.display.flip()
    clock.tick(60)
