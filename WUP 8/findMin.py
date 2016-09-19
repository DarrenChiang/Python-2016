def f(x) :
	return (4 * pow(x, 3) - 9 * pow(x, 2))

def df(x) :
	return (12 * pow(x, 2) - 18 * x)

def search(x) :
	while df(x) != 0 and df(-x) != 0 :
		x = x + 0.1
		if x == 1.5 :
			print(x)
	return

def posNeg(x) :
	if df(x) == 0 :
		return x
	elif df(-x) == 0 :
		return -x

print("This program will find the minimum of the function: 4x^3 - 9x^2.")

x = 0.0
repeat = True

while repeat:
	search(x)
	if f(posNeg(x)) > f(posNeg(x) + 0.1) or f(posNeg(x)) < f(posNeg(x) - 0.1) :
		x = x + 0.1
	else :
		repeat = false

print("Minimum: " + str(x))
	



