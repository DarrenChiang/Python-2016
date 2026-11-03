def displayGrid(grid) :
    for i in grid['value'] :
        s = ""
        for z in i :
            s += z
        print(s)
    print()

def loadEmptyGrid(grid) :
    grid['value'] = [[], [], [], [], []]
    
    grid['row'] = 1
    while grid['row'] <= 5 :
        grid['column'] = 1
        while grid['column'] <= 5 :
            if grid['row'] % 2 == 0 and grid['column'] % 2 == 0 :
                grid['value'][grid['row'] - 1].append("+")
            elif grid['row'] % 2 == 0 :
                grid['value'][grid['row'] - 1].append("-")
            elif grid['column'] % 2 == 0 :
                grid['value'][grid['row'] - 1].append("|")
            else :
                grid['value'][grid['row'] - 1].append(" ")
            grid['column'] += 1
        grid['row'] += 1

def getInput(player, grid) :
    if player == 1 :
        print("Player 1 (X):")
        grid['row'], grid['column'] = input("Enter the row and column in that order (no spaces) : ")
        grid['row'] = int(grid['row'])
        grid['column'] = int(grid['column'])
        if grid['value'][2 * grid['row'] - 2][2 * grid['column'] - 2] == ' ' :
            grid['value'][2 * grid['row'] - 2][2 * grid['column'] - 2] = 'X'
        else :
            print()
            getInput(player, grid)
    elif player == 2 :
        print("Player 2 (O):")
        grid['row'], grid['column'] = input("Enter the row and column in that order (no spaces) : ")
        grid['row'] = int(grid['row'])
        grid['column'] = int(grid['column'])
        if grid['value'][2 * grid['row'] - 2][2 * grid['column'] - 2] == ' ' :
            grid['value'][2 * grid['row'] - 2][2 * grid['column'] - 2] = 'O'
        else :
            print()
            getInput(player, grid)

def checkWin(grid) :
    win = False
    for i in range(0, len(grid['value']), 2) :
        temp = []
        for x in range(0, len(grid['value']), 2) :
            temp.append(grid['value'][i][x])
        if temp == ['X', 'X', 'X'] or temp == ['O', 'O', 'O'] :
            win = True
    for x in range(0, len(grid['value'][0]), 2) :
        temp = []
        for y in range(0, len(grid['value']), 2) :
            temp.append(grid['value'][y][x])
        if temp == ['X', 'X', 'X'] or temp == ['O', 'O', 'O'] :
            win = True
    a = [grid['value'][x][x] for x in range(0, 5, 2)]
    b = [grid['value'][4 - x][x] for x in range(0, 5, 2)]

    if a == ['X', 'X', 'X'] or a == ['O', 'O', 'O'] or b == ['X', 'X', 'X'] or b == ['O', 'O', 'O'] :
        win = True  
    
    return win
        
grid = {'row': 0, 'column': 0, 'value': []}

player = 1

loadEmptyGrid(grid)

while not checkWin(grid) :
    displayGrid(grid)
    getInput(player, grid)
    if player == 1 :
        player = 2
    else :
        player = 1

print("\nGame Over!")
