import pygame as pg
from Vector import Vector

class Group_Plus(pg.sprite.Group):
    def __init__(self, gameInfo = None):
        pg.sprite.Group.__init__(self)

    def update(self):
        pg.sprite.Group.update(self)

    def draw(self, window):
        sprites = self.sprites()
        surface_blit = window.blit
        w, h = window.get_size()
        for spr in sprites:
            if ((spr.getLeft() >= 0 and spr.getLeft()) <= w or (spr.getRight() >= 0 and spr.getRight() <= w)) and ((spr.getTop() >= 0 or spr.getTop() <= h) and (spr.getBottom() >= 0 or spr.getBottom() <= 0)):
                self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []

class Platformer(Group_Plus):
    def __init__(self, gameInfo):
        Group_Plus.__init__(self)
        self.gravity = 5
        if 'gravity' in gameInfo:
            self.gravity = gameInfo['gravity']

    def update(self):
        Group_Plus.update(self)
        for s in self.sprites():
            if s.getBottom() < 600:
                s.changeVerticalSpeed(self.gravity)
            elif s.getBottom() > 600:
                s.setY(600 - s.getHeight())
                s.setVerticalSpeed(0)

class Track_Player:
    def __init__(self, player, map, threshold):
        self.groups = []
        self.player = player
        self.map = map
        self.threshold = threshold
        self.vector = Vector(0, 0)

    def add(self, group):
        self.groups.append(group)

    def move(self, magnitude, angle):
        self.vector.set_magnitude(magnitude)
        self.vector.set_angle(angle)
        
        h_boundary = False
        v_boundary = False
        if self.map.getRight() <= self.player.getRight() + self.threshold:
            h_boundary = True
        elif self.map.getLeft() >= self.player.getLeft() - self.threshold:
            h_boundary = True

        if self.map.getTop() > self.player.getTop() - self.threshold:
            v_boundary = True
        elif self.map.getBottom() < self.player.getBottom() + self.threshold:
            v_boundary = True

        self.move_player(v_boundary, h_boundary)
        
        self.move_others(v_boundary, h_boundary)    

    def move_player(self, v, h):
        if v:
            self.player.vector.set_vertical(self.vector.vertical())
        else:
            self.player.vector.set_vertical(0)
        if h:
            self.player.vector.set_horizontal(self.vector.horizontal())
        else:
            self.player.vector.set_horizontal(0)

    def move_others(self, v, h):
        if v == False:
            self.map.changeY(-1 * self.vector.vertical())
            for g in self.groups:
                for s in g.sprites():
                    if s != self.player:
                        s.changeY(-1 * self.vector.vertical())
        if h == False:
            self.map.changeX(-1 * self.vector.horizontal())
            for g in self.groups:
                for s in g.sprites():
                    if s != self.player:
                        s.changeX(-1 * self.vector.horizontal())
        
                
