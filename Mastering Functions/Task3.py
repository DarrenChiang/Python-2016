def returnOdd(array) :
    for i in range(0, len(array)) :
        if i % 2 != 0 :
            print(array[i])

arr = [None]
enter = 0

while enter != "f" :
    enter = input("Enter values. Enter f when done. ")
    arr.append(enter)

del arr[0]
del arr[-1]

returnOdd(arr)
