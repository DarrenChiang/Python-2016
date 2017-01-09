while True:
    maxHeight = 0
    highest = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > maxHeight:
            maxHeight = mountain_h
            highest = i

    print(highest)
