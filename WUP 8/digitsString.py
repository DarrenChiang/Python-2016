input = int(input("Enter a natural number. "))

while input < 0 :
	input = int(input("Enter a natural number. "))

p = str(input)

f = 1
temp = int(input)

while temp > 1 :
	temp = int(temp / 10)
	f = f + 1
	
x = 0

while x < f :
	print(p[x])
	x = x + 1