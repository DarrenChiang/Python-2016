class Sprite:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    def __init__(self, spriteInfo):
        self.x, self.y = spriteInfo['coordinate']
        self.w, self.h = spriteInfo['dimensions']
        self.c = (0, 0 ,0)
        self.img = ''

    def setCoordinate(self, coord):
        self.x, self.y = coord

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

    def setDimensions(self, dim):
        self.w, self.h = dim

    def getDimensions(self):
        return self.w, self.h

    def setWidth(self, width):
        self.w = width

    def getWidth(self):
        return self.w

    def setHeight(self, height):
        self.h = height

    def setImage(self, image):
        self.img = image

    def getImage(self):
        return self.img

    def imageList(self, iList):
        self.imgList = iList

    def setColor(self, color):
        self.c = color

    def getColor(self):
        return self.c

    def update(self, pgEvent = None):
        pass

class Character(Sprite):
    def __init__(self, charInfo):
        Sprite.__init__(self, charInfo)
        self.name = charInfo['name']
        self.d = charInfo['direction']
        self.maxHp = charInfo['max hp']
        self.hp = self.maxHp
        self.spd = 0

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setHp(self, h):
        self.hp = h

    def getHp(self):
        return self.hp

    def setMaxHp(self, m):
        self.maxHp = m

    def getMaxHp(self):
        return self.maxHp

    def setSpecial(self, specialInfo):
        self.special = specialInfo

    def getSpecial(self):
        return self.special

    def setSpeed(self, s):
        self.spd = s

    def getSpeed(self):
        return self.spd

    def setDirection(self, direction):
        self.d = direction

    def getDirection(self):
        return self.d
