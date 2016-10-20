def readText(filename) :
    file = open(filename, "r")
    text = file.read().lower()
    textList = text.split()
    return textList

def findWord(string, textList) : #generates a list that contains all the positions (elements of all matching words)
    stay = False
    for i in textList :
        if string == i :
            stay = True
    if not stay :
        exit()
    return [y for y in range(0, len(textList)) if textList[y] == string]

def cycleSearch(elementList, textList) : #generates a list containing all words within 4 words from every occurence of the input
    return [textList[x] for i in elementList for x in range(i - 4, i + 4) if i < len(textList) - 4 and textList[x] != textList[i]]

def rateOccurence(wordList) : #generates a list of all words and their occurence count
    arr = []
    skip = False

    for x in wordList :
        for y in range(0, len(arr)) :
            if x == arr[y] :
                skip = True
                arr[y][1] += 1
                break
        if not skip :
            arr.append([x, 1])
        else :
            skip = False

    return giveRange(arr)

def giveRange(occurenceCount) : #generates a list of all words and their respective ranges (EX: ["dog", 5] ["cat", 7] with dog having 5 to 6)
    arr = []
    for x in range(0, len(occurenceCount)) :
        temp = 0
        for y in range(0, x) :
            temp += occurenceCount[y][1]
        arr.append([occurenceCount[x][0], temp])
    return arr
            
def randomGenerate(wordRange, count, word) : #generates a string that randomly chooses from the words based on the ranges for count times
    import random

    found = False
    string = word + " "

    while count > 0 :
        rn = random.randint(0, len(wordRange))
        found = False
        while not found :
            for x in range(0, len(wordRange)) :
                found = False
                if rn == wordRange[x][1] :
                    string += wordRange[x][0] + " "
                    found = True
                    break
            if not found :
                rn += -1
            
        count += -1
        
    return string


textList = readText("Text1.txt")
word = input("Enter word : ")
elementList = findWord(word, textList)

wordList = cycleSearch(elementList, textList)
wordRange = rateOccurence(wordList)

count = 0

while count < 1 :
    count = int(input("How many words to generate? "))               

print(randomGenerate(wordRange, count, word))

