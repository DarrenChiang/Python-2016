import pygame as pg
import math
import sys
sys.path.insert(0, 'C:\\Users\\ASUS\\Documents\\Python Proj\\Pygame Files\\Classes')

from Sprite import Sprite_Plus
from Environments import Group_Plus

class Object(Sprite_Plus):
    def __init__(self, sprite_info):
        Sprite_Plus.__init__(self, sprite_info)
        self.x += self.w
        self.y += self.h
        self.r = self.h / 2
        self.mass = self.r ** 3

    def setX(self, xValue):
        self.x = xValue - self.w

    def getX(self):
        return self.x + self.w

    def setY(self, yValue):
        self.y = yValue - self.h

    def getY(self):
        return self.y + self.h

    def update(self):
        Sprite_Plus.update(self)
        self.x = int(self.x)
        self.y = int(self.y)

class Space(Group_Plus):
    def __init__(self, group_info):
        Group_Plus.__init__(self, group_info)
        self.g = group_info['gravity constant']

    def gravity(self, o1, o2):
        dx = o2.getX() - o1.getX()
        dy = o2.getY() - o1.getY()
        distance = (dx ** 2 + dy ** 2) ** 0.5 / 5
        angle = 0
        if dx == 0:
            if dy >= 0:
                angle = math.pi / 2
            else:
                angle = -math.pi / 2
        else:          
            angle = math.atan2(dy, dx)
        if distance > o1.r + o2.r:
            acceleration = o2.mass * self.g / (distance ** 2)
            o1.hSpd += acceleration * math.cos(angle)
            o1.vSpd += acceleration * math.sin(angle)

    def update(self):
        Group_Plus.update(self)
        for o1 in self.sprites():
            for o2 in self.sprites():
                if o2 != o1:
                    self.gravity(o1, o2)
        
        

    

pg.init()

window = pg.display.set_mode((1000, 800))

pg.display.set_caption('Particles')

clock = pg.time.Clock()

game_on = True

sim_info = {'gravity constant': 1}

sim = Space(sim_info)

obj1 = Object({'dimensions': (10, 10),
               'coordinate': (600, 100),
               'color': (255, 0, 0)})

obj2 = Object({'dimensions': (10, 10),
               'coordinate': (100, 300),
               'color': (0, 0, 255)})

obj3 = Object({'dimensions': (10, 10),
               'coordinate': (400, 600),
               'color': (0, 255, 0)})

sim.add(obj1)
sim.add(obj2)
#sim.add(obj3)

while game_on:
    window.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False

    sim.update()

    sim.draw(window)

    pg.display.flip()
    clock.tick(120)
