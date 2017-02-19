x = 0
y = 0

w = 0
h = 0

v = 0

c = (0, 0, 0)

def snek(coord, dim, color, spd):
    global x
    global y
    global w
    global h
    global v
    global c
    x, y = coord
    w, h = dim
    v = spd
    c = color

def setCoord(x1, y1):
    global x
    global y
    x = x1
    y = y1

def setDim(w1, h1):
    global w
    global h
    w = w1
    h = h1

def setSpd(v1):
    global v
    v = v1

def setClr(c1):
    global c
    c = c1

def move(direction):
    global x
    global y
    global v
    if direction == 'r':
        x += v
    elif direction == 'l':
        x -= v
    elif direction == 'u':
        y -= v
    elif direction == 'd':
        y += v

    return (x, y)

def getX():
    global x
    return x

def getY():
    global y
    return y

def getDim():
    global w
    global h
    return (w, h)
    
    
