import pygame as pg

class Platformer(pg.sprite.Group):
    def __init__(self, gameInfo):
        pg.sprite.Group.__init__(self)
        self.gravity = 5
        if 'gravity' in gameInfo:
            self.gravity = gameInfo['gravity']

    def update(self):
        pg.sprite.Group.update(self)
        for s in self.sprites():
            if s.getY() + s.getHeight() < 1000:
                s.changeY(self.gravity)
