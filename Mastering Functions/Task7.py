def modifiedSeparate(a) :
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
    
    return array

def searchNumber(word, array) :
    count = 0
    for i in array :
        if i == word :
            count += 1
    print("The number of occurrences of " + word + " is " + str(count) + ".")


string = input("Enter a string: ")
word = input("Enter a word and the program will search for the number of occurrences: ")

searchNumber(word, modifiedSeparate(string))
