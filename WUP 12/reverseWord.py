word = input("Enter a word (string) and I'll reverse the letters in it: ")

size = len(word) - 1
rWord = ""

for i in range(size, -1, -1) :
	rWord = rWord + word[i]

print(rWord)


