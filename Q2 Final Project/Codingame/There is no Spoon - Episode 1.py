grid = []

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(line)


for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != '.':
            origin = str(x) + ' ' + str(y)
            right = ''
            down = ''
            if x < len(grid[y]) - 1:
                tempx = -1
                tempy = -1
                for i in range(x + 1, len(grid[y])):
                    if grid[y][i] != '.':
                        tempx = i
                        tempy = y
                        break
                right = str(tempx) + ' ' + str(tempy)
            else:
                right = '-1 -1'
            if y < len(grid) - 1:
                tempx = -1
                tempy = -1
                for i in range(y + 1, len(grid)):
                    if grid[i][x] != '.':
                        tempx = x
                        tempy = i
                        break
                down = str(tempx) + ' ' + str(tempy)
            else:
                down = '-1 -1'
            print(origin + ' ' + right + ' ' + down)
