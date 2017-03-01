import pygame as pg
import random
import math

def draw(win, group):
    for c in group:
        pg.draw.circle(win, c['color'], (int(c['x']), int(c['y'])), c['r'], 2)

def move(group):
    for c in group:
        c['x'] += c['hSpd']
        c['y'] += c['vSpd']

def collide(group):
    for c in group:
        rB = c['x'] + c['r']
        lB = c['x'] - c['r']
        uB = c['y'] - c['r']
        dB = c['y'] + c['r']
        if rB >= 800:
            c['x'] = 800 - c['r']
            c['hSpd'] *= -1
        elif lB <= 0:
            c['x'] = c['r']
            c['hSpd'] *= -1

        if uB <= 0:
            c['y'] = c['r']
            c['vSpd'] *= -1
        elif dB >= 600:
            c['y'] = 600 - c['r']
            c['vSpd'] *= -1

def colorizor(group, count):
    if count == 60:
        for c in group:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            c['color'] = (r, g, b)
        

pg.init()

window = pg.display.set_mode((800, 600))

pg.display.set_caption('Circles')

clock = pg.time.Clock()

group = []

for i in range(251):
    r = random.randint(10, 50)
    x = random.randint(r, 800 - r)
    y = random.randint(r, 600 - r)
    spd = random.randint(2, 6)
    a = random.randint(0, 360)
    group.append({'x': x,
                  'y': y,
                  'r': r,
                  'hSpd': spd * math.cos(math.radians(a)),
                  'vSpd': spd * math.sin(math.radians(a)),
                  'color': (50, 50, 255)})

game_on = True

count = 0

while game_on:
    window.fill((255, 255, 255))

    count += 1
    if count > 60:
        count = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False

    colorizor(group, count)

    move(group)

    collide(group)
    
    draw(window, group)

    pg.display.flip()
    clock.tick(60)
