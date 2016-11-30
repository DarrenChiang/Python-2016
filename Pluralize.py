def pluralize(word, num):
    """
    Returns a string that holds num in word form and the appropriate pluralization for "word."
    """
    word = word.lower().lstrip()
    string = ""
    numList = ["zero", "one", "two", "three", "four", "five", "six", "seven",
               "eight", "nine", "ten", "eleven", "twelve", "thirteen",
               "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
               "nineteen", "twenty", "thirty", "forty", "fifty", "sixty",
               "seventy", "eighty", "ninety"]
    vowels = ["a", "e", "i", "o", "u", "y"]
    multi_exception = {"is": "es", "us": "i", "ix": "ices", "eau": "eaux", "ouse": "ice",
                       "ch": "es", "sh": "es"}
    o_exception = ["hero", "potato", "volcano"]
    special = {"goose": "geese", "man": "men", "mouse": "mice",
                  "tooth": "teeth", "child": "children",
                  "woman": "women", "ox": "oxen", "wolf" : "wolves"}
    unchanging = ["deer", "fish", "sheep", "species", "aircraft", "bison"]
    if num <= 20:
        string = numList[num]       
    else:
        temp1 = int(num / 10)
        temp2 = int(num % 10)
        string = numList[temp1 + 18] + "-" + numList[temp2]
    string += " "
    if num != 1 and word not in unchanging:
        if word in special:
            word = special[word]
        elif multiCheck(word, multi_exception)[0]:
            b = multiCheck(word, multi_exception)[1]
            word = word[0 : -len(b)] + multi_exception[b]
        elif word[-1] == "y":
            if word[-2] in vowels:
                word += "s"
            else:
                word = word[0 : -1] + "ies"
        elif word[-1] in ["s", "x", "z"] or word in o_exception:
            word += "es"
        else:
            word += "s"
    return string + word

def multiCheck(word, multi_exception):
    """
    Returns a boolean for whether word has an ending in the multi_exception and the ending itself.
    """
    length = 0
    a = False
    b = ""
    for keys in multi_exception:
        if len(keys) > length:
            length = len(keys)
    for i in range(1, length + 1):
        if word[-i:] in multi_exception:
            a = True
            b = word[-i:]
    return a, b
                                                   
                            
                                                   

print(pluralize(input("Enter a singular noun: "), int(input("Enter a value: "))))
