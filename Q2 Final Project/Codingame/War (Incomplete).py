def strip(card):
    return card[0 : -1].lower()

def getValue(card):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    return order.index(strip(card))

def result(give, get, quan):
    get = get[quan: ] + get[0: quan]
    get += give[0 : quan]
    give = give[quan : ]
    return give, get

def battle(d1, d2, count = 1):
    con = count - 1
    if getValue(d1[con]) > getValue(d2[con]):
        d2, d1 = result(d2, d1, count)
        return d1, d2
    elif getValue(d2[con]) > getValue(d1[con]):
        d1, d2 = result(d1, d2, count)
        return d1, d2
    elif len(d1) >= count + 4 and len(d2) >= count + 4:
        return battle(d1, d2, count + 4)
    else:
        return [], []

n = int(input())  # the number of cards for player 1
deck1 = []
for i in range(n):
    deck1.append(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
deck2 = []
for i in range(m):
    deck2.append(input()) # the m cards of player 2

rounds = 0
while len(deck1) > 0 and len(deck2) > 0:
    deck1, deck2 = battle(deck1, deck2)
    rounds += 1

if len(deck1) > 0:
    print(1, rounds)
elif len(deck2) > 0:
    print(2, rounds)
else:
    print('PAT')
