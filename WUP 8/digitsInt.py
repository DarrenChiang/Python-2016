input = int(input("Enter a natural number. "))

while input < 0 :
	input = int(input("Enter a natural number. "))

input = float(input)

f = 0
temp = int(input)

while temp > 1 :
	temp = int(temp / 10)
	f = f + 1
size = f

residual = [None] * f
while f >= 0 :
	f = f - 1
	input, residual[f] = divmod(input, 10)
	print(int(residual[f]))