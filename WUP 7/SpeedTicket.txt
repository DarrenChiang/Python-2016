from sys import argv

name, speed, birthday = argv

spd = int(speed)

if birthday == "true" or birthday == "True" or birthday == "1" :
	spd = spd - 5

if spd <= 60 :
	print("No ticket.")
elif spd <= 80 :
	print("Small ticket.")
elif spd > 80 :
	print("Big ticket.")