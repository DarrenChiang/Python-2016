def pascal(rows, items = [1], iteration = 1):
    printRow(rows, items)
    items.insert(0, 0)
    items.insert(len(items), 0)
    if iteration < rows:
        nItems = []
        for i in range(len(items)):
            if i < len(items) - 1:
                nItems.append(items[i] + items[i + 1])
        pascal(rows, nItems, iteration + 1)
    
def printRow(rows, items):
    length = rows * 2 - 1
    cItems = []
    for i in range(len(items)):
        cItems.append(items[i])
        if i < len(items) - 1:
            cItems.append(0)
    void = int((length - len(cItems)) / 2)
    if rows <= 5:
        for i in range(void):
            cItems.insert(0, " ")
            cItems.insert(len(cItems) , " ")
        for i in range(len(cItems)):
            if cItems[i] == 0:
                cItems[i] = " "
    else:
        for i in range(void):
            cItems.insert(0, " ")
            cItems.insert(len(cItems) , " ")
        for i in range(len(cItems)):
            if cItems[i] == 0:
                cItems[i] = "   "
            else:
                cItems[i] = " " + str(cItems[i])
                if len(cItems[i]) < 3:
                    cItems[i] += " "
    for i in cItems:
        print(i, end = "")
    print()
    
        
            


pascal(int(input("How many rows? ")))
