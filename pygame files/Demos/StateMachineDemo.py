import pygame as pg

pg.init()

winSize = (800, 700)
window = pg.display.set_mode(winSize)

pg.display.set_caption('State Machine')

clock = pg.time.Clock()

img1 = pg.image.load('example.jpg')

white = (255, 255, 255)

x = winSize[0] / 2
y = winSize[1] / 2
w = 50
h = 50

while True:
    window.fill(white)
    char_rect = pg.Rect(x, y, w, h)
    window.blit(img1, char_rect)
    
    pg.display.flip()

    clock.tick(10)
    
