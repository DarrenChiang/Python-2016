import pygame as pg

class Animation():
    def __init__(self, listName, cPeriod = 60, iList = []):
        self.name = listName
        self.list = iList
        self.on = False
        self.counter = 0
        self.cyclePeriod = cPeriod
        self.currentPic = 0

    def getName(self):
        return self.name

    def setImageList(self, iList):
        self.list = iList

    def addImage(self, img):
        self.list.append(img)

    def adjustImages(self, sprite):
        self.setImageList([pg.transform.scale(img, (sprite.getWidth(), sprite.getHeight())) for img in self.list])

    def setCyclePeriod(self, period):
        self.cyclePeriod = period

    def turnOn(self, b):
        self.on = b
        self.currentPict = 0

    def getImage(self):
        return self.list[self.currentPic]

    def cycle(self):
        if self.on:
            self.counter += 1
            if self.counter == self.cyclePeriod:
                self.counter = 0
                self.currentPic += 1
                if self.currentPic > len(self.list) - 1:
                    self.currentPic = 0
            return self.getImage()
        else:
            return None
        
