import pygame
import random
from Object import Object

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)
purple = (200, 0, 200)
green = (0, 255, 0)
blue = (0, 0, 255)

def grid(win, color, size):
    w, h = pygame.display.get_surface().get_size()
    for c in range(0, w, size):
        pygame.draw.line(win, color, (c, 0), (c, h))
    for r in range(0, h, size):
        pygame.draw.line(win, color, (0, r), (w, r))

def display(win, obj):
    pygame.draw.rect(win, obj.getColor(), obj.getCoordinates() + obj.getDimensions(), 0)

def showScore(win, font, score):
    w, h = pygame.display.get_surface().get_size()
    win.blit(font.render(str(score), False, blue), (w - 40, 0))

def endScreen(win, font, score, hScore):
    win.fill(white)
    w, h = pygame.display.get_surface().get_size()
    line1 = 'Game Over!'
    line2 = 'Score: ' + str(score)
    line3 = 'High Score: ' + str(hScore)
    line4 = 'Press SPACE to play again.'
    win.blit(font.render(line1, False, red), (w / 2 - 200, h / 2 - 100))
    win.blit(font.render(line2, False, red), (w / 2 - 200, h / 2 - 50))
    win.blit(font.render(line3, False, red), (w / 2 - 200, h / 2))
    win.blit(font.render(line4, False, red), (w / 2 - 200, h / 2 + 50))

def startScreen(win, font):
    win.fill(white)
    w, h = pygame.display.get_surface().get_size()
    win.blit(font.render('SNEKGAME', False, red), (w / 2 - 200, h / 2 - 30))
    win.blit(font.render('Press SPACE to start.', False, red), (w / 2 - 200, h / 2 + 30))

def hitBoundary(obj):
    hit = False
    w, h = pygame.display.get_surface().get_size()
    if obj.getX() < 0 or obj.getX() > w - obj.getWidth():
        hit = True
    if obj.getY() < 0 or obj.getY() > h - obj.getHeight():
        hit = True
    return hit

def snekMove(win, snek):
    new = snek[0].getCoordinates()
    snek[0].move()
    old = (0, 0)
    for i in range(1, len(snek)):
        old = snek[i].getCoordinates()
        snek[i].setCoordinates(new)
        new = old

def contact(obj1, obj2):
    hit = False
    dx = obj1.getX() - obj2.getX()
    dy = obj1.getY() - obj2.getY()
    if dx == 0 and dy == 0:
        hit = True
    return hit

def grow(snek):
    snek.append(Object(snek[len(snek) - 1].getCoordinates(), snek[len(snek) - 1].getDimensions(), snek[len(snek) - 1].getColor()))

def suicide(snek, t, lim):
    hit = False
    if t >= lim:
        for i in range(1, len(snek)):
            if contact(snek[0], snek[i]):
                hit = True
                break
    return hit

def getRandom(size):
    w, h = pygame.display.get_surface().get_size()
    x = random.randint(2, w / size - 2)
    y = random.randint(2, h / size - 2)
    return x * size, y * size

def checkSnek(snek, coord):
    overlap = False
    for i in range(len(snek)):
        if snek[i].getCoordinates() == coord:
            overlap = True
            break
    return overlap

def portal(snek):
    if hitBoundary(snek[0]):
        w, h = pygame.display.get_surface().get_size()
        x, y = snek[0].getCoordinates()
        if x <= 0:
            snek[0].setCoordinates((w, y))
            snek[0].setDirection('l')
        elif x >= w:
            snek[0].setCoordinates((0, y))
            snek[0].setDirection('r')
        elif y <= 0:
            snek[0].setCoordinates((x, h))
            snek[0].setDirection('u')
        elif y >= h:
            snek[0].setCoordinates((x, 0))
            snek[0].setDirection('d')

def start(snek, point):
    gridSize = 20
    spd = 20
    x = 80
    y = 80
    w = gridSize
    h = gridSize
    direc = 'r'
    length = 5

    del snek[length : ]

    for i in range(len(snek)):
        snek[i].setCoordinates((x, y))
        snek[i].setDimensions((w, h))
        snek[i].setSpeed(spd)
        snek[i].setDirection(direc)
        
    newCoord = getRandom(gridSize)
    while checkSnek(snek, newCoord):
        newCoord = getRandom(gridSize)
    point = Object(newCoord, (w, h), green)

def checkFile(filename):
    try:
        file = open(filename, 'r')
        file.close()
    except IOError:
        file = open(filename, 'w')
        file.close()

pygame.init()

pygame.font.init()
font = pygame.font.SysFont("Lobster", 50)

width = 760
height = 500
gridSize = 20
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snek Game')
clock = pygame.time.Clock()

fps = 20

spd = 20

x = 80
y = 80
w = gridSize
h = gridSize

score = 0

direc = 'r'

length = 5

snek = [Object((x, y), (w, h), red, spd, direc) for i in range(length)]

snek[0] = Object((x, y), (w, h), purple, spd, direc)

newCoord = getRandom(gridSize)
while checkSnek(snek, newCoord):
    newCoord = getRandom(gridSize)
point = Object(newCoord, (w, h), green)

immunity = 0

game_on = True
state = ['start', 'play', 'end']
game_state = state[0]

highScore = 0

checkFile('high_score.txt')

reader = open('high_score.txt', 'r')
try:   
    highScore = int(reader.read())
except ValueError:
    pass
reader.close()

while game_on:
    if game_state == state[0]:
        startScreen(window, font)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_on = False
                elif event.key == pygame.K_SPACE:
                    game_state = state[1]
           
    if game_state == state[1]:
        window.fill(white)
        grid(window, black, gridSize)
        showScore(window, font, score)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_on = False
                elif event.key == pygame.K_w and snek[0].getDirection() != 'd':
                    snek[0].setDirection('u')
                elif event.key == pygame.K_s and snek[0].getDirection() != 'u':
                    snek[0].setDirection('d')
                elif event.key == pygame.K_d and snek[0].getDirection() != 'l':
                    snek[0].setDirection('r')
                elif event.key == pygame.K_a and snek[0].getDirection() != 'r':
                    snek[0].setDirection('l')
         
        if immunity <= fps:
            immunity += 1

        if contact(snek[0], point):
            score += 1
            newCoord = getRandom(gridSize)
            while checkSnek(snek, newCoord):
                newCoord = getRandom(gridSize)
            point.setCoordinates(newCoord)
            grow(snek)
        
        if suicide(snek, immunity, fps):
            game_state = state[2]
            if score > highScore:
                highScore = score
        else:
            snekMove(window, snek)
            portal(snek)

        for i in range(len(snek)):
            display(window, snek[i])

        display(window, point)

    if game_state == state[2]:
        endScreen(window, font, score, highScore)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_on = False
                elif event.key == pygame.K_SPACE:
                    start(snek, point)
                    immunity = 0
                    score = 0
                    game_on = True
                    game_state = state[1]
         
    """ 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            game_start = False
            game_play = False
            game_over = False
            game_on = False
        elif game_start:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = False
                    game_play = True
                    game_over = False
                    game_on = True
        elif game_play:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snek[0].getDirection() != 'd':
                    snek[0].setDirection('u')
                elif event.key == pygame.K_s and snek[0].getDirection() != 'u':
                    snek[0].setDirection('d')
                elif event.key == pygame.K_d and snek[0].getDirection() != 'l':
                    snek[0].setDirection('r')
                elif event.key == pygame.K_a and snek[0].getDirection() != 'r':
                    snek[0].setDirection('l')
        elif game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = False
                    game_play = True
                    game_over = False
                    game_on = True
                    start(snek, point)
                    immunity = 0
                    score = 0
    """  
    pygame.display.flip()
    clock.tick(fps)
    
writer = open('high_score.txt', 'w')
writer.write(str(highScore))
writer.close()

pygame.quit()
