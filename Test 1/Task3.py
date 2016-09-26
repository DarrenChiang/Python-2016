from timeit import default_timer as timer
import time
import sys

coffee = ""
size = ""
sugar = -1
wait = 0

price = 0

ans = ""

skip = 0

resetting = 0

tinit = 0
tend = 0

def reset() :
    global coffee
    coffee = ""
    global size
    size = ""
    global sugar
    sugar = -1
    global price
    price = 0
    global skip
    skip = 0
    global wait
    wait = 0
    global resetting
    resetting = 1
    return;

def menu(coffee, size, sugar) :
    if coffee == "l" :
        print("Coffee:  LATTE(l)  Americano(a)  Expresso(e)")
    elif coffee == "a" :
        print("Coffee:  Latte(l)  AMERICANO(a)  Expresso(e)")
    elif coffee == "e" :
        print("Coffee:  Latte(l)  Americano(a)  EXPRESSO(e)")
    else :
        print("Coffee:  Latte(l)  Americano(a)  Expresso(e)")

    if size == "s" :
        print("Size:      SMALL(s)                Big(b)")
    elif size == "b" :
        print("Size:      Small(s)                BIG(b)")
    else :
        print("Size:      Small(s)                Big(b)")

    if sugar == 1 :   
        print("Sugar:     0    |1|    2     3     4     5 ")
    elif sugar == 2 :
        print("Sugar:     0     1    |2|    3     4     5 ")
    elif sugar == 3 :
        print("Sugar:     0     1     2    |3|    4     5 ")
    elif sugar == 4 :
        print("Sugar:     0     1     2     3    |4|    5 ")
    elif sugar == 5 :
        print("Sugar:     0     1     2     3     4    |5|")
    elif sugar == 0 :
        print("Sugar:    |0|    1     2     3     4     5 ")
    else :
        print("Sugar:     0     1     2     3     4     5 ")

    return;

while 1 :
    menu(coffee, size, sugar)
    resetting = 0
    tinit = timer()
    tend = timer()
    while 1 :
        if coffee == "l" or coffee == "a" or coffee == "e" or skip :
            break
        coffee = input("Enter the type of coffee: ")
        tend = timer()
        if coffee == "c" :
            skip = 1
            coffee = ""
            break

    menu(coffee, size, sugar)

    if tend - tinit >= 10 or skip :
        skip = 0
        reset()

    if not resetting :
        while 1 :
            if size == "s" or size == "b" or skip :
                break
            size = input("Enter the size: ")
            tend = timer()
            if size == "c" :
                skip = 1
                size = ""
                break

    menu(coffee, size, sugar)

    if tend - tinit >= 10 or skip :
        skip = 0
        reset()

    if not resetting :
        while 1:
            if skip or (sugar >= 0 and sugar <= 5) :
                break
            sugar = int(input("Enter the amount of sugar: "))
            tend = timer()

    if tend - tinit >= 10 or skip :
        skip = 0
        reset()
       
    if coffee == "l" :
        wait = 6
        price = 20
        if size == "b" :
            price = 30
    elif coffee == "a" :
        wait = 4
        price = 30
        if size == "b" :
            price = 50
    elif coffee == "e" :
        wait = 6
        price = 25
        if size == "b" :
            price = 40

    if sugar >= 0 and sugar <= 5 :
        price += sugar
        
    print("Total Price: " + str(price))        

    if price != 0 :
        while 1 :
            ans = input("Your coffee is ready to be made. Start(s) or cancel(c): ")
            tend = timer()
            if ans == "s" or ans == "c" :
                break
        if ans == "s" and tend - tinit < 10 :
            for i in range(1, wait + 1) :
                time.sleep(1)
                print(wait + 1 - i)
                if i == wait :
                    print("Done!")
                    sys.exit()
        elif ans == "c" or tend - tinit >= 10 :
            skip = 1
    

