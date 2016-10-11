def accumulate(array, element) :
    x = 0
    for i in range(0, element + 1) :
        try :
            x += int(array[i])
        except ValueError :
            x = x
    return x

def cycle(array) :
    narray = list(array)
    for i in range(0, len(array)) :
        array[i] = accumulate(narray, i)
    print(array)

arr = ["start"]
enter = 0

while enter != "f" :
    enter = input("Enter integers. Enter f when done. ")
    arr.append(enter)

del arr[0]
del arr[-1]

cycle(arr)
