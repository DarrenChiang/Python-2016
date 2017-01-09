n = int(input())
value = []
for i in input().split():
    value.append(int(i))

dy = 0
dx = 0
maxValue = 0
x = 0

for minX in range(len(value) - 1, 1, -1):
    if minX == len(value) - 1 or x >= minX:
        maxValue = 0
        x = 0
        for maxX in range(0, minX):
            if value[maxX] > maxValue:
                maxValue = value[maxX]
                x = maxX
    if maxValue > value[minX]:
        if value[minX] - maxValue < dy:
            dy = value[minX] - maxValue
            dx = minX - x
    

if dx == 0:
    print(0)
else:
    if dy / dx < 0:
        print(dy)
    else:
        print(0)
