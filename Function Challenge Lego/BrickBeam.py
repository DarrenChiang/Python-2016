import numpy as np
import matplotlib.pyplot as plt

brick = 0 
beam = 0

def distance(x1, y1, x2, y2) :
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)

def comparison(x, y) :
    if distance(x, y, 7, 4) < distance(x, y, 3, 5) :
        global brick
        brick = brick + 1
    elif distance(x, y, 7, 4) > distance(x, y, 3, 5) :
        global beam
        beam = beam + 1
    return

legos = np.loadtxt("Legos.txt", delimiter = ",")

for x, y in legos :
    comparison(x, y)

print("Bricks: " + str(brick))
print("Beams:  " + str(beam))
