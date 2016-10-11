def combineLists(l1, l2) :
    nl = [0]
    c1 = 0
    c2 = 0
    for i in range(0, len(l1) * 2) :
        if i % 2 == 0 :
            nl.append(int(l1[c1]))
            c1 += 1
        else :
            nl.append(int(l2[c2]))
            c2 += 1
    del nl[0]
    
    print(nl)

def checkLength(l1, l2) :
    if len(l1) > len(l2) :
        print("Not enough values in list 2.")
        while len(l1) != len(l2) :
            enter = input("Enter values for list 2. ")
            l2.append(enter)
    else :
        print("Not enough values in list 1.")
        while len(l1) != len(l2) :
            enter = input("Enter values for list 1. ")
            l1.append(enter)

arr1 = [None]
arr2 = [None]
enter = 0

while enter != "f" :
    enter = input("Enter values for list 1. Enter f when done. ")
    arr1.append(enter)

del arr1[0]
del arr1[-1]

enter = 0

while enter != "f" :
    enter = input("Enter values for list 2. Enter f when done. ")
    arr2.append(enter)

del arr2[0]
del arr2[-1]

if len(arr1) != len(arr2) :
    checkLength(arr1, arr2)

combineLists(arr1, arr2)


