def displayGrid(grid) : #Prints grid
    for i in grid['value'] :
        s = ""
        for z in i :
            s += z
        print(s)
    print()

def loadEmptyGrid(grid) : #Loads or resets grid to empty slots
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

def getInput(player, grid, repeat, comp) : #Gets player input
    #Funtion fit appears often. Scroll down for info.
    grid['row'] = 0
    grid['column'] = 0
    if repeat : #Modifies text when appropriate
        text = "That slot is already taken! Enter another slot: "
    else :
        text = "Enter the row and column in that order (no spaces): "
    if player == 1 :
        if not repeat :
            print("Player 1 (X):") #Only prints once
        while grid['row'] not in [1, 2, 3] or grid['column'] not in [1, 2, 3] : #Input must be within grid
            unpackInput(grid, text) #Check function unpackInput for info
            if grid['row'] not in [1, 2, 3] or grid['column'] not in [1, 2, 3] :
                text = "That slot is out of bounds. Enter another: " #Modifies text when appropriate
        if grid['value'][fit(grid['row'])][fit(grid['column'])] == ' ' : #Check if slot's taken
            grid['value'][fit(grid['row'])][fit(grid['column'])] = 'X'
        else :
            getInput(player, grid, True, comp)
    elif player == 2 :
        if comp : #Check how player 2 is controlled
            print("Player 2 (O):")
            computerTurn(grid)
        else :
            if not repeat :
                print("Player 2 (O):") #Only prints once
            while grid['row'] not in [1, 2, 3] and grid['column'] not in [1, 2, 3] : #Input must be within grid
                unpackInput(grid, text) #Check functin unpackInput for info
                if grid['row'] not in [1, 2, 3] or grid['column'] not in [1, 2, 3] :
                    text = "That slot is out of bounds. Enter another: " #Modifies text when appropriate
            if grid['value'][fit(grid['row'])][fit(grid['column'])] == ' ' : #Check if slot's taken
                grid['value'][fit(grid['row'])][fit(grid['column'])] = 'O'
            else :
                getInput(player, grid, True, comp)

def unpackInput(grid, text) : #Program uses unpacking of inputs [a, b = input()], which is prone to many errors. This function corrects that.
    try :
        grid['row'], grid['column'] = input(text)
        grid['row'] = int(grid['row'])
        grid['column'] = int(grid['column'])
        return grid['row'], grid['column']
    except ValueError :
        unpackInput(grid, "Input is invalid. Enter it correctly: ") #Repeats sequence with modified text if ValueError occurs.

def checkEnd(grid) : #When to end the looping of turns
    end = False
    winner = 0
    
    #Horizontal win check
    for i in range(0, 5, 2) :
        temp = [grid['value'][i][x] for x in range(0, 5, 2)]
        if temp == ['X', 'X', 'X'] or temp == ['O', 'O', 'O'] :
            end = True
            if temp == ['X', 'X', 'X'] :
                winner = 1
            else :
                winner = 2
    #Vertical win check
    for x in range(0, 5, 2) :
        temp = [grid['value'][y][x] for y in range(0, 5, 2) ]
        if temp == ['X', 'X', 'X'] or temp == ['O', 'O', 'O'] :
            end = True
            if temp == ['X', 'X', 'X'] :
                winner = 1
            else :
                winner = 2
    #Diagonal win check
    a = [grid['value'][x][x] for x in range(0, 5, 2)]
    b = [grid['value'][4 - x][x] for x in range(0, 5, 2)]
    if a == ['X', 'X', 'X'] or a == ['O', 'O', 'O'] or b == ['X', 'X', 'X'] or b == ['O', 'O', 'O'] :
        end = True
        if temp == ['X', 'X', 'X'] :
                winner = 1
        else :
                winner = 2
    #Tie check
    space = 0
    for i in grid['value'] :
        for z in i :
            if z == " " :
                space += 1
    if space == 0 :
        end = True
    
    return [end, winner]

def computerTurn(grid) : #Function for computer-generated responses
    done = checkFill(grid, 'O') #Check for chance to win. (Looks for 2 O's in the same row, horizontal, or diagonal.) Between winning and blocking, prioritize winning.

    if not done : #Done limits the computer's turn to one action.
        done = checkFill(grid, 'X') #Check for blocking. (Looks for 2 X's in the same row, horizontal, or diagonal.)

    if not done :
        priority(grid) #When neither of above is necessary, other actions are taken. Check priority for more info.
        
    return

#Computer functions:
#All of the functions here return a boolean, because the computer needs to know when to stop (at 1 action).

def checkFill(grid, mark) : #Checks for occurences of 2 "marks" (X or O)
    done = False

    temp = [[grid['value'][row][column] for column in range(0, 5, 2)] for row in range(0, 5, 2)] #Creates a list for rows for checking.
    done = checkOpening(grid, temp, mark, 0) #Check checkOpening for more info.

    if not done :
        temp = [[grid['value'][row][column] for row in range(0, 5, 2)] for column in range(0, 5, 2)] #Creates a list for columns for checking.
        done = checkOpening(grid, temp, mark, 1)

    #The rest are for diagonals. The reason they are different is because temp now only hold one chain (1 diagonal) instead of 3 chains (3 rows or 3 columns).
    if not done : #The logic, however, is similar to checkOpening.
        count = 0
        empty = 0
        a = [grid['value'][x][x] for x in range(0, 5, 2)]
        for i in range(0, len(a)) :
            if a[i] == mark :
                count += 1
            else :
                empty = i
        if count == 2 and grid['value'][fit(empty)][fit(empty)] == ' ' :
            grid['value'][fit(empty)][fit(empty)] = 'O'
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
            grid['value'][fit(empty + 1)][fit(empty + 1)] = 'O'
            done = True
    
    return done

def checkOpening(grid, temp, mark, direct) : #Checks for 2's in the vertical and horizontal. Direct determines whether vertical or horizontal.
    done = False

    for i in range(0, len(temp)) : #For every chain, reset count and add to it to find the occurences of mark (X, O). If count is 2 and the remaining space (empty) is truly "empty" then proceed.
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
                grid['value'][fit(i + 1)][fit(empty + 1)] = 'O'
            elif direct == 1 :
                grid['value'][fit(empty + 1)][fit(i + 1)] = 'O'
            done = True
            break

    return done #Probably should've just merged horizontal and vertical into this one function.

def priority(grid) :
    done = False
    a = []
    if grid['value'][2][2] == ' ' : #Prioritize center block if no need for blocking or winning.
        grid['value'][2][2] = 'O'
        done = True
    if not done : 
        temp = [[int(iFit(row)), int(iFit(column))] for row in range(0, 5, 2) for column in range(0, 5, 2) if grid['value'][row][column] == " "] #Gathers all empty spaces. (Previous checks make this okay.)
        a = temp
        for i in temp :
            if i in [[1, 1], [1, 3], [3, 1], [3, 3]] : #Prioritze corners.
                grid['value'][fit(i[0])][fit(i[1])] = 'O'
                done = True
                break
    if not done : #If no emergence (after checking everything above), then randomizing is safe.
        import random
        b = random.randint(0, len(a) - 1)
        grid['value'][fit(a[b][0])][fit(a[b][1])] = 'O'
        

def fit(a) : #Changes grid values to list values ([1, 2, 3] => [0, 2, 4])
    return 2 * a - 2

def iFit(a) : #Changes list values to grid values ([0, 2, 4] => [1, 2, 3])      May not be used
    return (a + 2) / 2
        
grid = {'row': 0, 'column': 0, 'value': []}

player = 0

comp = False

loadEmptyGrid(grid)

choice = ""
text = "Play against player (p) or computer (c)? : "

while choice not in ['p', 'c'] :
    choice = input(text)
    if choice not in ['p', 'c'] :
        text = "Invalid input, enter again: "

text = "Which player goes first? (1 or 2) "

while player not in [1, 2] :
    player = int(input(text))
    if player not in [1, 2] :
        text = "Invalid input, enter again: "

if choice == 'c' :
    comp = True

while not checkEnd(grid)[0] :
    displayGrid(grid)
    getInput(player, grid, False, comp)
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
