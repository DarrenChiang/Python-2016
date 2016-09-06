print("Enter y or n for each question.")
#This program guides the user through several questions to determine whether they can use an image. The user mostly just has to type y or n.
#EX: Will you answer this question?    y

global input

#Here's a global string variable. This is so that the function below can modify it.

def checkAns(b) :
	if b == 1 :
		if input != "y" and input != "n" and input != "x" :
			input = input("Please enter again.")
			checkAns(b)
	else :
		if input != "y" and input != "n" :
			input = input("Please enter again.")
			checkAns(b)
	return

#This function checks if the input that the user gave is valid. If not, it will ask the user to give another input and call itself to check again.
#The integer argument is only used for a special case when a third answer aside from yes or no is needed. The function only changes when 1 is put in.

input = input("Did you take or create the image yourself? ")

checkAns(0)
if input == "y" :
	input = input("Was the picture you created an original idea? If you're not sure, enter x. ")
	checkAns(1)
	if input == "y" :
		print("Yes! If you can rightfully call the picture your own, then you automatically own all copyrights to it.")
	elif input == "n" :
		print("No! If you created a shockingly similar picture to someone else's, you may be in trouble.")
	else :
		print("When in doubt, do your research to find out if you copied an idea. Otherwise, watch out!")
else :
	print("Ask yourself the Fair Use Questions:")
	input = input("Are you using SPARINGLY the image for personal, non-profit, educational, research, or scholarly purposes? ")
	checkAns(0)
	if input == "y" :
		print("Yes! If it is indeed used for educational, limited non-profit use, then you're safe.")
	else :
		input = input("Are you transforming or repurposing the image to create a new meaning? ")
		checkAns(0)
		if input == "y" :
			print("Yes! If you completely rework the image so that it isn't recognizeable, you can use it!")
		else :
			input = input("Are you publishing the image in a fact-based context or publication that benefits the public as a whole? ")
			checkAns(0)
			if input == "y" :
				print("Probably. If the image is published in a non-biased way, you MAY be safe.")
			else :
				input = input("Would it be considered impossible to obtain permission from the original source? ")
				checkAns(0)
				if input == "y" :
					print("Yes! If it's impossible (usually because the original source is no longer available), it's usually safe.")

				else :
					input = input("Is the image in the public domain or protected by creative common agreements? ")
					checkAns(0)
					if input == "y" :
						print("Yes! If the image's in the public domain, you should be fine!")
					else :
						input = input("Did you purchase it or obtain permission from the original source? ")
						checkAns(0)
						if input == "y" :
							print("Yes! It's all good if you purchased or obtained copyright.")
						else :
							print("No! By all means, DON'T use it!")
					



