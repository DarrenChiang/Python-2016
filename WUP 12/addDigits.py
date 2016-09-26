num = int(input("Enter a positive integer: "))

s = 0
count = len(str(num))
digit = 0

for i in (count - 1, 0, -1) :
	s = s + int(num / pow(10, i))
	print(int(num / pow(10, i)))
	num = num - int(num / pow(10, i)) * pow(10, i)
	print(s)
	print(num)


print(s)
