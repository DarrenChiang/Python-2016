class Object:
    def __init__(self, coord, dim, color = (0, 0, 0), spd = '1', direc = 'r'):
        self.x, self.y = coord
        self.w, self.h = dim
        self.c = color
        self.v = spd
        self.d = direc

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCoordinates(self):
        return self.x, self.y

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def getDimensions(self):
        return self.w, self.h

    def getColor(self):
        return self.c

    def getSpeed(self):
        return self.v

    def getDirection(self):
        return self.d

    def setCoordinates(self, coord):
        self.x, self.y = coord;

    def move(self):
        if self.d == 'u':
            self.y -= self.v
        elif self.d == 'd':
            self.y += self.v
        elif self.d == 'r':
            self.x += self.v
        elif self.d == 'l':
            self.x -= self.v

    def setSpeed(self, spd):
        self.v = spd

    def setDirection(self, direc):
        self.d = direc

    def setColor(self, color):
        self.c = color

    def setDimensions(self, dim):
        self.w, self.h = dim
