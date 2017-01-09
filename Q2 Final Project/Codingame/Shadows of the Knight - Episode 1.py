w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

dx = x0
dy = y0
    
rl = w
ll = 0
ul = 0
dl = h

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if 'U' in bomb_dir:
        dl = dy
        dy -= ((dl - ul) / 2)
    elif 'D' in bomb_dir:
        ul = dy
        dy += ((dl - ul) / 2)
    
    if 'R' in bomb_dir:
        ll = dx
        dx += ((rl - ll) / 2)
    elif 'L' in bomb_dir:
        rl = dx
        dx -= ((rl - ll) / 2)

    dx = int(dx)
    dy = int(dy)

    print(dx, dy)
