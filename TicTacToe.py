def displayGrid(grid) :
    """
    This function prints the grid out.
    """
    for i in grid['value'] :
        s = ""
        for z in i :
            s += z
        print(s)
    print()

def loadEmptyGrid(grid) :
    """
    This function empties an existing grid or creates a new one.
    """
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

def getInput(player, grid, repeat, comp, comp2) :
    """
    This function gets the input from either a player or a computer.
    """
    grid['row'] = 0
    grid['column'] = 0
    if repeat : 
        text = "That slot is already taken! Enter another slot: "
    else :
        text = "Enter the row and column in that order (no spaces): "
    if player == 1 :
        if comp2 :
            print("Player 1 (X): ")
            computerTurn(grid, player)
        else :
            if not repeat :
                print("Player 1 (X):")
            while grid['row'] not in [1, 2, 3] or grid['column'] not in [1, 2, 3] : 
                unpackInput(grid, text) 
                if grid['row'] not in [1, 2, 3] or grid['column'] not in [1, 2, 3] :
                    text = "That slot is out of bounds. Enter another: " 
            if grid['value'][fit(grid['row'])][fit(grid['column'])] == ' ' :
                grid['value'][fit(grid['row'])][fit(grid['column'])] = 'X'
            else :
                getInput(player, grid, True, comp)
    elif player == 2 :
        if comp : 
            print("Player 2 (O):")
            computerTurn(grid, player)
        else :
            if not repeat :
                print("Player 2 (O):") 
            while grid['row'] not in [1, 2, 3] and grid['column'] not in [1, 2, 3] : 
                unpackInput(grid, text) 
                if grid['row'] not in [1, 2, 3] or grid['column'] not in [1, 2, 3] :
                    text = "That slot is out of bounds. Enter another: " 
            if grid['value'][fit(grid['row'])][fit(grid['column'])] == ' ' : 
                grid['value'][fit(grid['row'])][fit(grid['column'])] = 'O'
            else :
                getInput(player, grid, True, comp)

def unpackInput(grid, text) :
    """
    This function takes in input value of two integers and applies them to the row and column of choice.
    """
    try :
        grid['row'], grid['column'] = input(text)
        grid['row'] = int(grid['row'])
        grid['column'] = int(grid['column'])
        return grid['row'], grid['column']
    except ValueError :
        unpackInput(grid, "Input is invalid. Enter it correctly: ")

def checkEnd(grid) :
    """
    This function checks whether a player won or if the game is tied.
    """
    end = False
    winner = 0
    
    for i in range(0, 5, 2) :
        temp = [grid['value'][i][x] for x in range(0, 5, 2)]
        if temp == ['X', 'X', 'X'] or temp == ['O', 'O', 'O'] :
            end = True
            if temp == ['X', 'X', 'X'] :
                winner = 1
            else :
                winner = 2

    for x in range(0, 5, 2) :
        temp = [grid['value'][y][x] for y in range(0, 5, 2) ]
        if temp == ['X', 'X', 'X'] or temp == ['O', 'O', 'O'] :
            end = True
            if temp == ['X', 'X', 'X'] :
                winner = 1
            else :
                winner = 2

    a = [grid['value'][x][x] for x in range(0, 5, 2)]
    b = [grid['value'][4 - x][x] for x in range(0, 5, 2)]
    if a == ['X', 'X', 'X'] or a == ['O', 'O', 'O'] or b == ['X', 'X', 'X'] or b == ['O', 'O', 'O'] :
        end = True
        if temp == ['X', 'X', 'X'] :
                winner = 1
        else :
                winner = 2

    space = 0
    for i in grid['value'] :
        for z in i :
            if z == " " :
                space += 1
    if space == 0 :
        end = True
    
    return [end, winner]

def computerTurn(grid, player) :
    """
    This function organizes all possible computer responses based on priority (win => defend => choice).
    """
    mark = ''
    if player == 1 :
        enter = 'X'
        mark = 'O'
    elif player == 2 :
        enter = 'O'
        mark = 'X'
 
    done = checkFill(grid, mark, enter) 

    if not done : 
        done = checkFill(grid, mark, enter) 

    if not done :
        priority(grid, enter) 
        
    return

def checkFill(grid, mark, enter) :
    """
    This function checks whether a row, column, or diagonal is about to be filled with the same mark. It can be used for both defense and offense.
    """
    done = False

    temp = [[grid['value'][row][column] for column in range(0, 5, 2)] for row in range(0, 5, 2)] 
    done = checkOpening(grid, temp, mark, 0, enter) 

    if not done :
        temp = [[grid['value'][row][column] for row in range(0, 5, 2)] for column in range(0, 5, 2)]
        done = checkOpening(grid, temp, mark, 1, enter)

    if not done : 
        count = 0
        empty = 0
        a = [grid['value'][x][x] for x in range(0, 5, 2)]
        for i in range(0, len(a)) :
            if a[i] == mark :
                count += 1
            else :
                empty = i
        if count == 2 and grid['value'][fit(empty)][fit(empty)] == ' ' :
            grid['value'][fit(empty)][fit(empty)] = enter
            done = True
            
    if not done :
        count = 0
        empty = 0
        b = [grid['value'][4 - x][x] for x in range(0, 5, 2)]
        for i in range(0, len(b)) :
            if b[i] == mark :
                count += 1
            else :
                empty = i
        if count == 2 and grid['value'][fit(empty + 1)][fit(empty + 1)] == ' ' :
            grid['value'][fit(empty + 1)][fit(empty + 1)] = enter
            done = True
    
    return done

def checkOpening(grid, temp, mark, direct, enter) :
    """
    This function simplifies the process of check multiple rows and multiple columns for checkFill.
    """
    done = False

    for i in range(0, len(temp)) :
        count = 0
        empty = 0
        eMark = ''
        for z in range(0, len(temp[i])) :
            if temp[i][z] == mark :
                count += 1
            elif temp[i][z] != '|' :
                empty = z
                eMark = temp[i][z]
        if count == 2 and eMark == ' ' :
            if direct == 0 :
                grid['value'][fit(i + 1)][fit(empty + 1)] = enter
            elif direct == 1 :
                grid['value'][fit(empty + 1)][fit(i + 1)] = enter
            done = True
            break

    return done

def priority(grid, enter) :
    """
    This function will prioritize the center grid then the corner grid and then randomize if there's no emergence.
    """
    done = False
    a = []
    if grid['value'][2][2] == ' ' : 
        grid['value'][2][2] = enter
        done = True
    if not done : 
        temp = [[int(iFit(row)), int(iFit(column))] for row in range(0, 5, 2) for column in range(0, 5, 2) if grid['value'][row][column] == " "] #Gathers all empty spaces. (Previous checks make this okay.)
        a = temp
        for i in temp :
            if i in [[1, 1], [1, 3], [3, 1], [3, 3]] :
                grid['value'][fit(i[0])][fit(i[1])] = enter
                done = True
                break
    if not done :
        import random
        b = random.randint(0, len(a) - 1)
        grid['value'][fit(a[b][0])][fit(a[b][1])] = enter
        

def fit(a) : 
    """
    This function changes grid values to list values ([1, 2, 3] => [0, 2, 4]).
    """
    return 2 * a - 2

def iFit(a) :
    """
    This function is the inverse of fit ([0, 2, 4] => [1, 2, 3]).
    """
    return (a + 2) / 2
        
grid = {'row': 0, 'column': 0, 'value': []}

player = 0

comp = False

loadEmptyGrid(grid)

choice = ""
text = "Play against player (p) or computer (c)? : "

while choice not in ['p', 'c', 's'] :
    choice = input(text)
    if choice not in ['p', 'c', 's'] :
        text = "Invalid input, enter again: "

text = "Which player goes first? (1 or 2) "

while player not in [1, 2] :
    player = int(input(text))
    if player not in [1, 2] :
        text = "Invalid input, enter again: "

comp2 = False
if choice == 'c' or choice == 's' :
    comp = True
    if choice == 's' :
        comp2 = True

while not checkEnd(grid)[0] :
    displayGrid(grid)
    getInput(player, grid, False, comp, comp2)
    if player == 1 :
        player = 2
    else :
        player = 1

displayGrid(grid)

print("\nGame Over!")

if checkEnd(grid)[1] == 1 :
    print("Player 1 wins!")
elif checkEnd(grid)[1] == 2 :
    print("Player 2 wins!")
else :
    print("Tie!")
