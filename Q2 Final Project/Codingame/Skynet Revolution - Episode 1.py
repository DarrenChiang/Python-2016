# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
links = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links.append([n1, n2])
exits = []
for i in range(e):
    exits.append(int(input()))  # the index of a gateway node


while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    output = ''

    d = False
    for exit in exits:
        if [si, exit] in links or [exit, si] in links:
            a = si
            b = exit
            d = True
            if [a, b] in links:
                links.remove([a, b])
            else:
                links.remove([b, a])
    if not d:
        for link in links:
            if si in link:
                a, b = link
                break
    
    output = str(a) + ' ' + str(b)
    
    print(output)
