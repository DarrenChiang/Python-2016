import pygame as pg
import math
import random
from Sprite import *

class Enemy:
    def __init__(self, sprite, e_type):
        self.type = e_type
        self.sprite = sprite
        self.counter = 0
        self.choices = {'timer': random.randint(0, 30),
                        'action': random.randint(0, 100)}

    def target(self, player):
        self.sprite.target(player)       

    def attack(self):
        self.sprite.attack()
        self.sprite.stop()

    def move_target(self):
        self.sprite.vector.set_angle(self.sprite.target_angle + 90)
        self.sprite.vector.set_magnitude(3)

    def move_strafe(self):
        d = random.randint(0, 1)
        self.sprite.vector.set_magnitude(3)
        if d == 0:
            self.sprite.vector.set_angle(self.sprite.target_angle)
        else:
            self.sprite.vector.set_angle(self.sprite.target_angle + 180)

    def set_type(self, e_type):
        self.type = e_type

    def decision(self):
        if self.choices['timer'] == None:
            self.choices['timer'] = random.randint(1, 30)
            self.choices['action'] = random.randint(0, 100)

        if self.counter == self.choices['timer']:
            self.sprite.stop()
            if self.choices['action'] <= 60:
                self.attack()
            elif self.choices['action'] <= 80:
                self.move_target()
            else:
                self.move_strafe()
            self.choices['timer'] = None

    def boundary(self, m):
        if self.sprite.getLeft() < m.getLeft() or self.sprite.getRight() > m.getRight():
            self.sprite.setHorizontalSpeed(self.sprite.getHorizontalSpeed() * -1)
        if self.sprite.getTop() < m.getTop() or self.sprite.getBottom() > m.getBottom():
            self.sprite.setVerticalSpeed(self.sprite.getVerticalSpeed() * -1)
    
    def update(self):
        if self.counter > 30:
            self.counter = 0
        self.counter += 1

        self.decision()

class Boss(Enemy):
    def __init__(self, info, e_type):
        Enemy.__init__(self, info, e_type)
        self.burst = False
        
    def update(self):
        if self.counter > 180:
            self.counter = 0
        self.counter += 1
        
        if self.counter > 60:
            self.attack()
        
class Enemy_Group():
    def __init__(self, target, m):
        self.list = []
        self.target = target
        self.map = m

    def set_target(self, target):
        self.target = target

    def add(self, sprite):
        self.list.append(sprite)

    def kill(self):
        i = 0
        while i < len(self.list):
            if self.list[i].sprite.getHp() <= 0:
                self.list.remove(self.list[i])
                i -= 1
            i += 1

    def update(self):
        for s in self.list:
            s.sprite.projectile_limit(self.map)
            if s.type == 'grunt':
                s.target(self.target)
            s.boundary(self.map)
            s.update()

        self.kill()
