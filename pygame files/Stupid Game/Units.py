import pygame as pg
import math
from Sprite import *

class Projectile(Character):
    def __init__(self, info):
        Character.__init__(self, info)
        self.side = info['side']
        self.interact_list = info['interact groups']
        self.damage = info['damage']
        if 'image' in info:
            self.image = info['image']
            self.current_image = self.image

    def get_side(self):
        return self.side

    def destroy(self, m):
        if self.getRight() > m.getRight() or self.getLeft() < m.getLeft() or self.getTop() < m.getTop() or self.getBottom() > m.getBottom():
            self.kill()

        for g in self.interact_list:
            for s in g.sprites():
                if pg.sprite.collide_rect(self, s):
                    s.hit(self.damage * -1)
                    self.kill()
                    break

    def hit(self, damage):
        self.changeHp(damage)

class Homing_Projectile(Projectile):
    def __init__(self, info):
        Projectile.__init__(self, info)
        self.target = info['target']

    def set_homing(self, t):
        self.target = t

    def home(self):
        x, y = self.target.getCoordinate()
        dx = x - self.getX()
        dy = -1 * (y - self.getY())
        self.vector.set_angle(math.degrees(math.atan2(dy, dx)))

    def update(self):
        Projectile.update(self)
        self.home()

class Shooter(Character):
    def __init__(self, info):
        Character.__init__(self, info)
        self.projectile_info = {}
        self.counter = 0
        self.delay = 6
        self.target_angle = 90

    def set_projectiles(self, info, group):
        self.projectile_info = info
        self.projectiles = group

    def target(self, target):
        if target == 'mouse':
            x, y = pg.mouse.get_pos()
        else:
            x, y = target.getCoordinate()
        dx = x - self.getX()
        dy = -1* (y - self.getY())
        self.target_angle = math.degrees(math.atan2(dy, dx)) - 90
        self.setAngle(self.target_angle)
    
    def attack(self):
        if self.counter == self.delay:
            self.counter = 0
            
        if self.counter == 0:
            proj = Projectile(self.projectile_info)
            proj.setCoordinate(self.getCoordinate())
            proj.setAngle(self.target_angle)
            proj.vector.set_magnitude(self.projectile_info['projectile speed'])
            proj.vector.set_angle(self.target_angle + 90)

            self.projectiles.add(proj)
            
        self.counter += 1

    def projectile_limit(self, m):
        sprites = self.projectiles.sprites()
        for i in range(len(sprites)):
            sprites[i].destroy(m)

    def hit(self, damage):
        self.changeHp(damage)

class Special_Shooter(Shooter):
    def __init__(self, info):
        Shooter.__init__(self, info)

    def attack(self):
        if self.counter == self.delay:
            self.counter = 0
            
        if self.counter == 0:
            for i in range(4):
                angle = self.target_angle + 90 * i
                proj = Projectile(self.projectile_info)
                proj.setCoordinate(self.getCoordinate())
                proj.setAngle(angle)
                proj.vector.set_magnitude(self.projectile_info['projectile speed'])
                proj.vector.set_angle(angle)

                self.projectiles.add(proj)
            
        self.counter += 1

    def update(self):
        Shooter.update(self)
        self.target_angle += 1
        self.rotate(1)

    
        

