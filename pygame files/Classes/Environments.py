import pygame as pg

class Group_Plus(pg.sprite.Group):
    def __init__(self, gameInfo = None):
        pg.sprite.Group.__init__(self)

    def update(self):
        pg.sprite.Group.update(self)

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
                
