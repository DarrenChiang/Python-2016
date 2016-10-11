import os

def mainMenu() :
    os.system('cls' if os.name == 'nt' else 'clear')
    print("This is the main menu. This counts as a menu. Below are 32 options:")
    print(" 1. Cool Menu")
    print(" 2. Not-so-cool Menu")
    enter = input("What is your preference (enter #)? Press X to exit. ")
    return enter

def coolMenu() :
    os.system('cls' if os.name == 'nt' else 'clear')
    print("How cool are you?")
    print(" 1. Very cool")
    print(" 2. Cool enough")
    enter = input("What is your answer? Press X to exit. ")
    return enter

def nCoolMenu()  :
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What tugs you most in life?")
    print(" 1. My social skills.")
    print(" 2. My social skills.")
    print(" 3. My social skills.")
    enter = input("What is your answer? Press X to exit. ")
    return enter

stay = True

while stay:
    result = mainMenu()
    if result == "1" :
        print("You selected the Cool Menu.")
        path = 1
        break
    elif result == "2" :
        print("You selected the Not-so-cool Menu.")
        path = 2
        break
    elif result == "X" or result == "x" :
        path = 0
        break
    else :
        print("Enter a valid answer.")

if path == 1 :
    while stay :
        result = coolMenu()
        if result == "1" :
            print("You're pretty swood!")
            break
        elif result == "2" :
            print("Noice.")
            break
        elif result == "X" or result == "x" :
            break
        else :
            print("Enter a valid answer.")
elif path == 2 :
    while stay :
        result = nCoolMenu()
        if result == "1" or result == "2" or result == "3" :
            print("That sucks man...")
            break
        elif result == "X" or result == "x" :
            break
        else :
            print("Enter a valid answer.")
