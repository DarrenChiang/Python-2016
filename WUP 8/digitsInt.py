input = int(input("Enter a natural number. "))

while input < 0 :
	input = int(input("Enter a natural number. "))

input = float(input)

f = 0
temp = int(input)

while temp > 1 :
	temp = int(temp / 10)
	f = f + 1

residual = [f + 1]
while f >= 0 :
	input, residual[f] = divmod(input, 10)
	print(int(residual[f]))
	f = f - 1