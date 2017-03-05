import pygame as pg

class Sprite_Plus(pg.sprite.Sprite):
    all_sprites = pg.sprite.Group()
    
    def __init__(self, spriteInfo):
        pg.sprite.Sprite.__init__(self)
        self.w, self.h = spriteInfo['dimensions']
        self.image = pg.Surface(spriteInfo['dimensions'])
        
        self.c = (255, 255, 255)
        if 'color' in spriteInfo:
            self.c = spriteInfo['color']
        self.image.fill(self.c)

        self.x = 0
        self.y = 0
        if 'coordinate' in spriteInfo:
            self.x, self.y = spriteInfo['coordinate']
        self.rect = self.x, self.y

        self.imgList = []
        self.sprite_image = None
        if 'image list' in spriteInfo:
            self.imgList = spriteInfo['image list']

        self.vSpd = 0
        self.hSpd = 0

        self.animList = None
        self.currentAnim = 0
        self.animOn = False
        

    def setCoordinate(self, coord):
        self.x, self.y = coord

    def center(self, win):
        w, h = win.get_size()
        self.setCoordinate(((w - self.w) / 2, (h - self.h) / 2))

    def getCoordinate(self):
        return self.x, self.y

    def setX(self, xValue):
        self.x = xValue

    def changeX(self, xValue):
        self.x += xValue

    def getX(self):
        return self.x

    def setY(self, yValue):
        self.y = yValue

    def changeY(self, yValue):
        self.y += yValue

    def getY(self):
        return self.y

    def getTop(self):
        return self.y

    def getBottom(self):
        return self.y + self.h

    def getRight(self):
        return self.x + self.w

    def getLeft(self):
        return self.x

    def setColor(self, color):
        self.c = color

    def getColor(self):
        return color

    def setDimensions(self, dim):
        self.w, self.h = dim

    def getDimensions(self):
        return self.w, self.h

    def setWidth(self, width):
        if width >= 0:
            self.w = width

    def changeWidth(self, width):
        if self.w + width >= 0:
            self.w += width

    def getWidth(self):
        return self.w

    def setHeight(self, height):
        if height >= 0:
            self.h = height

    def changeHeight(self, height):
        if self.h + height >= 0:
            self.h += height

    def getHeight(self):
        return self.h

    def addImage(self, img):
        self.imgList.append(img)

    def setImageList(self, iList):
        self.imgList = iList

    def getImageList(self):
        return self.imgList

    def setListImage(self, num):
        if num >= 0 and num < len(self.imgList):
            self.sprite_image = self.imgList[num]
        else:
            self.sprite_image = None

    def setImage(self, img):
        self.sprite_image = img

    def getImage(self):
        return self.sprite_image

    def adjustImages(self):
        self.setImageList([pg.transform.scale(img, (self.w, self.h)) for img in self.getImageList()])

    def setVerticalSpeed(self, spd):
        self.vSpd = spd

    def changeVerticalSpeed(self, spd):
        self.vSpd += spd

    def getVerticalSpeed(self):
        return self.vSpd

    def setHorizontalSpeed(self, spd):
        self.hSpd = spd

    def changeHorizontalSpeed(self, spd):
        self.hSpd += spd

    def getHorizontalSpeed(self):
        return self.hSpd

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

    def update(self):
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(self.c)
        self.changeX(self.getHorizontalSpeed())
        self.changeY(self.getVerticalSpeed())
        self.rect = self.x, self.y
        if self.animOn:
            self.setImage(self.animList[self.currentAnim].cycle())

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

    
    

    
