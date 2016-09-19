n = int(input("This program prints out the first nth prime numbers. \nEnter n as an integer: "))

x = 1                                                                          #The xth number in the list of 1 to n.
cand = 1	                                                               #The candidate number, check this for whether prime or not.
nprime = 0				      #Boolean for whether to print cand or not.

while x <= n :
	for i in range(1, cand) :            
		if cand % i == 0 and i != 1 and i != cand:             
			nprime = 1
	if nprime == 0 :
		print(cand)
		x = x + 1
	cand = cand + 1
	nprime = 0




