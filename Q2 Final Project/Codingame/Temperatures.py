n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

tempList = temps.split()

if len(tempList) > 1:
    newTempList = tempList[0 : n]

    result = newTempList[0]
    for i in newTempList:
        if abs(int(i)) < abs(int(result)) or abs(int(i)) == abs(int(result)) and int(i) > 0:
            result = i
    print(result)
else:
    if len(tempList) == 0:
        print(0)
    else :
        print(tempList[0])
