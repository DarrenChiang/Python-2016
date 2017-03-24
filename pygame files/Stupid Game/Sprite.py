import pygame as pg
import math
from Vector import Vector

class Sprite_Plus(pg.sprite.Sprite):
    all_sprites = pg.sprite.Group()
    
    def __init__(self, spriteInfo):
        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.Surface(spriteInfo['dimensions'])
        self.current_image = self.image
        self.angle = 0
        
        self.rect = self.image.get_rect()
        
        self.c = (0, 0, 0)
        if 'color' in spriteInfo:
            self.c = spriteInfo['color']

        self.image.fill(self.c)

        if 'coordinate' in spriteInfo:
            self.rect.center = spriteInfo['coordinate']

        self.imgList = []
        if 'image list' in spriteInfo:
            self.imgList = spriteInfo['image list']

        self.vector = Vector(0, 0)

        self.animList = None
        self.currentAnim = 0
        self.animOn = False
        

    def setCoordinate(self, coord):
        self.rect.center = coord

    def center(self, win):
        w, h = win.get_size()
        self.setCoordinate((w / 2, h / 2))

    def getCoordinate(self):
        return self.rect.center

    def move(self):
        self.rect.x += self.vector.horizontal()
        self.rect.y += self.vector.vertical()

    def setX(self, xValue):
        self.rect.centerx = xValue

    def changeX(self, xValue):
        self.rect.centerx += xValue

    def getX(self):
        return self.rect.centerx

    def setY(self, yValue):
        self.rect.centery = yValue

    def changeY(self, yValue):
        self.rect.centery += yValue

    def getY(self):
        return self.rect.centery

    def getTop(self):
        return self.rect.top

    def getBottom(self):
        return self.rect.bottom

    def getRight(self):
        return self.rect.right

    def getLeft(self):
        return self.rect.left

    def setColor(self, color):
        self.c = color
        if self.current_image == None:
            self.image.fill(color)

    def getColor(self):
        return self.c

    def setDimensions(self, dim):
        self.rect.size = dim

    def getDimensions(self):
        return self.rect.size

    def setWidth(self, width):
        if width >= 0:
            self.rect.width = width

    def changeWidth(self, width):
        if self.rect.width + width >= 0:
            self.rect.width += width

    def getWidth(self):
        return self.rect.width

    def setHeight(self, height):
        if height >= 0:
            self.rect.height = height

    def changeHeight(self, height):
        if self.rect.height + height >= 0:
            self.rect.height += height

    def getHeight(self):
        return self.rect.height

    def addImage(self, img):
        self.imgList.append(img)

    def setImageList(self, iList):
        self.imgList = iList

    def getImageList(self):
        return self.imgList

    def setListImage(self, num):
        if num >= 0 and num < len(self.imgList):
            self.current_image = self.imgList[num]
        else:
            self.current_image = None

    def setImage(self, img = None):
        if img == None:
            self.image = pg.Surface(self.getDimensions())
            self.image.fill(self.c)
        else:
            self.image = img
        self.current_image = self.image

    def getImage(self):
        return self.image

    def adjustImages(self):
        self.setImageList([pg.transform.scale(img, self.rect.size) for img in self.getImageList()])

    def adjustImage(self, img):
        return pg.transform.scale(img, self.rect.size)
    
    def rotate(self, angle):
        self.angle += angle
        coord = self.rect.center
        self.image = pg.transform.rotate(self.current_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = coord

    def setAngle(self, angle):
        self.angle = angle
        coord = self.rect.center
        self.image = pg.transform.rotate(self.current_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = coord
        
    def setVerticalSpeed(self, spd):
        self.vector.set_vertical(spd)

    def changeVerticalSpeed(self, spd):
        self.vector.change_vertical(spd)

    def getVerticalSpeed(self):
        return self.vector.vertical()

    def setHorizontalSpeed(self, spd):
        self.vector.set_horizontal(spd)

    def changeHorizontalSpeed(self, spd):
        self.vector.change_horizontal(spd)

    def getHorizontalSpeed(self):
        return self.vector.horizontal()

    def stop(self):
        self.vector.stop()

    def createAnimationSet(self, aList):
        self.animList = aList

    def addAnimation(self, a):
        self.animList.append(a)

    def useAnimation(self, name):
        for i in range(len(self.animList)):
            if self.animList[i].getName() == name:
                self.currentAnim = i

    def animation_On(self, b):
        self.animOn = b
        self.animList[self.currentAnim].turnOn(b)
        if b == False:
            self.rotate(0)

    def animation(self):
        if self.animOn:
            self.image = self.animList[self.currentAnim].cycle()

    def update(self):
        self.move()
        self.animation()

    def hit(self, damage):
        #if collide
        pass
        
class Character(Sprite_Plus):
    def __init__(self, spriteInfo):
        Sprite_Plus.__init__(self, spriteInfo)
        self.name = spriteInfo['name']
        self.maxHp = spriteInfo['max hp']
        self.hp = self.maxHp

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setHp(self, h):
        self.hp = h
    
    def changeHp(self, c):
        self.hp += c

    def getHp(self):
        return self.hp

    def update(self):
        Sprite_Plus.update(self)
        if self.hp < 0:
            self.kill()

    def hit(self, damage):
        self.hp -= damage

    
    

    
