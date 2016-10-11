def frame(arr) :
    length = 0
    
    for i in range(0, len(arr)) :
        if len(arr[i]) > length :
            length = len(arr[i])

    length += 4

    print("*" * length)
    
    for i in arr :
        print("*" + i + (length - len(i) - 2) * " " + "*")
        
    print("*" * length)

a = [None]
enter = ""

while enter != "end" :
    enter = input("Enter strings. Enter end when done. ")
    a.append(enter)

del a[0]
del a[-1]

print("\n")

frame(a)
