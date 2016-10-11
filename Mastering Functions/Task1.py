def multiply(arr) :
    x = 1
    for i in arr :
        try :
            x *= int(i)
        except ValueError :
            x = x
    return x

arr = ["start"]
enter = 0

while enter != "f" :
    enter = input("Enter integers. Enter f when done. ")
    arr.append(enter)

print(multiply(arr))
