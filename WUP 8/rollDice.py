from random import randint

count = 0 
rolls = 1

while rolls <= 10000 :
	if randint(1, 6) == 6 :
		count = count + 1
	rolls = rolls + 1

print("Number of 6's: " + str(count))

p = count / 100

print("Percentage: " + str(p) + "%")
	