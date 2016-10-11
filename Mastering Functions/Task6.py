def separate(a) :
    x = 0
    array = [""]
    word = ""
    
    while x < len(a) :
        if a[x] != " " :
            word += a[x]
        elif a[x] == " " and word != "" :
            array.append(word)
            word = ""
        if x == len(a) - 1 :
            array.append(word)
        x += 1

    array.remove("")
    
    print(array)


string = input("Enter a string: ")

separate(string)
