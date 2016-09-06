import sys
from sys import argv

name, a_smile, b_smile = argv


if a_smile != "True" or a_smile != "true" or a_smile != "False" or a_smile != "false" or a_smile != "1" or a_smile != "0" :
	sys.exit

if a_smile == "True" or a_smile == "true" or  a_smile == "1" :
	a_smile = "t"
else :
	a_smile = "f"

if b_smile == "True" or b_smile == "true" or b_smile == "1" :
	b_smile = "t"
else :
	b_smile = "f"

if a_smile == b_smile :
	print("We are in trouble.")
else :
	print("We are fine.")

