import pygame as pg

class Group_Plus(pg.sprite.Group):
    def __init__(self):
        pg.sprite.Group.__init__(self)

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            if spr.getImage() == None:
                self.spritedict[spr] = surface_blit(spr.image, spr.rect)
            else:
                surface.blit(spr.getImage(), spr.getCoordinate())
        self.lostsprites = []

class Platformer(Group_Plus):
    def __init__(self, gameInfo):
        Group_Plus.__init__(self)
        self.gravity = 5
        if 'gravity' in gameInfo:
            self.gravity = gameInfo['gravity']

    def update(self):
        pg.sprite.Group.update(self)
        for s in self.sprites():
            if s.getBottom() < 600:
                s.changeVerticalSpeed(self.gravity)
            elif s.getBottom() > 600:
                s.setY(600 - s.getHeight())
                s.setVerticalSpeed(0)
                
