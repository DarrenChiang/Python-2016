import pygame as pg
import random
import math

class Particle:
    gravity_constant = 1
    
    def __init__(self, min_size, max_size, min_speed, max_speed):
        w, h = window.get_size()
        self.r = random.randint(min_size, max_size)
        self.x = random.randint(0 + self.r, w - self.r)
        self.y = random.randint(0 + self.r, h - self.r)
        self.c = (50, 50, 255)
        self.m = self.r * 1
        
        a = random.randint(0, 360)
        spd = random.randint(min_speed, max_speed)
        self.vSpd = spd * math.sin(math.radians(a))
        self.hSpd = spd * math.cos(math.radians(a))

        self.vAcc = 0
        self.hAcc = 0

        self.cWith = []
        
    def draw(self, window):
        pg.draw.circle(window, self.c, (self.x, self.y), self.r, 2)

    def move(self):
        self.hSpd += self.hAcc
        self.x += self.hSpd
        self.x = int(self.x)
        self.vSpd += self.vAcc
        self.y += self.vSpd
        self.y = int(self.y)

    def bounce(self, window, elastic):
        w, h = window.get_size()
        if self.x + self.r >= w:
            self.x = w - self.r
            if elastic == False:
                self.hSpd *= 0.9
            self.hSpd *= -1
        elif self.x - self.r <= 0:
            self.x = self.r
            if elastic == False:
                self.hSpd *= 0.9
            self.hSpd *= -1
        elif self.y + self.r >= h:
            self.y = h - self.r
            if elastic == False:
                self.vSpd *= 0.9
            self.vSpd *= -1
        elif self.y - self.r <= 0:
            if elastic == False:
                self.y = self.r
            self.vSpd *= -1

    def gravity(self, other):
        dx = other.x - self.y
        dy = other.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return self.gravity_constant * other.m / (distance ** 2)

    def interact(self, other):
        if other not in self.cWith:
            dx = other.x - self.x
            dy = other.y - self.y
            angle = 0
            if dx != 0:
                angle = math.atan(dy / dx)
            else:
                if dy > 0:
                    angle = math.pi / 2
                else:
                    angle = math.pi / -2
            distance = (dx ** 2 + dy ** 2) ** 0.5
            total_mass = self.m + other.m
            acceleration = other.m * self.gravity_constant / (distance ** 2)
            if distance < self.r + other.r and self.cWith != other:
                mass_ratio = other.m / total_mass
                new_distance = distance * mass_ratio
                self.x += int(new_distance * math.cos(angle))
                self.y += int(new_distance * math.sin(angle))
                #self.r = int((self.r ** 3 + other.r ** 3) ** (1 / 3))
                self.cWith.append(other)
            else:  
                self.vAcc = acceleration * math.sin(angle)
                self.hAcc = acceleration * math.cos(angle)
        else:
            other.x = self.x
            other.y = self.y
            other.hAcc = self.hAcc
            other.vAcc = self.vAcc
            other.hSpd = self.hSpd
            other.vSpd = self.vSpd
        
    def random_color(self, count):
        if count >= 60:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.c = (r, g, b)

    def reset_color(self):
        self.c = (50, 50, 255)

class Group:
    def __init__(self, window, particles = []):
        self.list = particles
        self.win = window

    def add(self, particle):
        self.list.append(particle)

    def update(self):
        for p in self.list:
            p.move()
            self.gravity(p)
            #p.bounce(self.win, False)
            p.draw(self.win)

    def gravity(self, p1):
        others = [p for p in self.list if p != p1]
        for p2 in others:
            if p2 not in p1.cWith:
                dx = p2.x - p1.x
                dy = p2.y - p2.y
                angle = 0
                if dx == 0:
                    if dy >= 0:
                        angle = math.pi / 2
                    else:
                        angle = -1 * math.pi / 2
                else:
                    angle = math.atan(dy / dx)
                distance = (dx ** 2 + dy ** 2) ** 0.5
                if distance <= p1.r + p2.r:
                    p1.cWith.append(p2)
                    p2.cWith.append(p1)
                    p1.vAcc -= p2.vAcc
                    p1.hAcc -= p2.hAcc
                else:                   
                    acceleration = p2.m * Particle.gravity_constant / (distance ** 2)
                    p1.vAcc += acceleration * math.sin(angle)
                    p1.hAcc += acceleration * math.cos(angle)
            else:
                p2.x = p1.x
                p2.y = p1.y
                p2.vSpd = p1.vSpd
                p2.vAcc = p1.vAcc
                p2.hSpd = p1.hSpd
                p2.hAcc = p1.hAcc

    def get(self):
        return self.list

pg.init()

window = pg.display.set_mode((800, 600))

pg.display.set_caption('Circles')

clock = pg.time.Clock()

g = Group(window, [Particle(5, 10, 0, 2) for i in range(2)])

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

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE]:
        for p in g.get():
            p.random_color(count)
    else:
        for p in g.get():
            p.reset_color()

    g.update()

    pg.display.flip()
    clock.tick(60)
