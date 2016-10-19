def readText(filename) :
    file = open(filename, "r")
    text = file.read().lower()
    textList = text.split()
    return textList

def findWord(string, textList) : #generates a list that contains all the positions (elements of all matching words
    return [y for y in range(0, len(textList)) if textList[y] == string]

def cycleSearch(array, count, textList) : #generates a list containing lists of the matching words with "count" words after them
    arr = []
    for i in range(0, len(array)) :
        arr.append(viewAhead(array[i], count, textList))
    return arr
    
def viewAhead(num, count, textList) : #adds "count" words after the matching words to their respective lists.
    arr = []
    for i in range(num, num + count) :
        try :
            arr.append(textList[i])
        except IndexError :
            arr.append(None)
    return arr

def mostCommon(array, element, fin) : #returns a list that contains all the words element places after and their occurences in order.
    wordList = []
    for i in range(0, len(array)) :
        wordList.append(array[i][element])

    count = wordHelp(wordList)

    ordered = []
    for x in range(0, len(count)) :
        for y in range(0, len(array)) :
            if count[x][0] == array[y][element] :
                temp = []
                for i in array[y] :
                    temp.append(i)
                ordered.append(temp)

    for x in range(0, len(count)) :
        temp = []
        for y in range(0, len(ordered)) :
            if count[x][0] == ordered[y][element] :
                temp.append(ordered[y])
        try :
            mostCommon(temp, element + 1, fin)
        except IndexError :
            for i in ordered :
                fin.append(i)
            break
    return
            

def wordHelp(wordList) : #returns a list with all strings and their occurences in the given list.
    skip = False
    count = []
    for x in range(0, len(wordList)) :
        for y in range(0, len(count)) :
            if wordList[x] == count[y][0] :
                skip = True
                count[y][1] += 1
                break
        if not skip :
            count.append([wordList[x], 1])
        else :
            skip = False
    #randomize(count)
    for x in range(0, len(count)) :
        for y in range(0, x) :
            if count[x][1] > count[y][1] :
                temp = count[x]
                count[x] = count[y]
                count[y] = temp
    return count

def randomize(array) :
    import random
    for x in range(0, len(array)) :
        array[x][1] = random.randint(1, array[x][1])

def printFin(fin) :
    for x in range(0, len(fin)) :
        temp = ""
        for y in fin[x] :
            try :
                temp += y + " "
            except TypeError :
                break
        print(temp)
    return

def removeDuplicates(array) :
    skip = False
    arr = []
    for x in array :
        for y in arr :
            if x == y :
                skip = True
                break
        if not skip :
            arr.append(x)
        else :
            skip = False
    return arr

textList = readText("Text2.txt")

enter = input("Search: ")
wordcount = int(input("Number of words to generate: "))

pos = findWord(enter, textList)

arr = cycleSearch(pos, wordcount, textList)

fin = []

mostCommon(arr, 1, fin)

fin = removeDuplicates(fin)

printFin(fin)


