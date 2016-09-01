print("Enter a grade (0-100): ")
input = int(input())

if input > 100 :
	print("Grade too high.")
elif input >= 97 :
	print("A+")
elif input >= 93 :
	print("A")
elif input >= 90 :
	print("A-")
elif input >= 87 :
	print("B+")
elif input >= 83 :
	print("B")
elif input >= 80 :
	print("B-")
elif input >= 77 :
	print("C+")
elif input >= 73 :
	print("C")
elif input >= 70 :
	print("C-")
elif input >= 67 :
	print("D+")
elif input >= 63 :
	print("D")
elif input >= 60 :
	print("D-")
elif 60 > input >= 0 :
	print("F")
else :
	print("Score too low.")