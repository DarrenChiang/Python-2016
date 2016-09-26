b = input("Enter only 1's and 0's: ")
# b is bin and is also the user input of the program. It has to be in binary.
s = 0
# s is the sum of all digits from b. s is used to ensure that b is in binary.

for c in range(0, len(b) - 1) :
    s += int(b[c])
# This loop goes through every element in the list of the input (as str),
# converts them to int, then adds them to s.

while s > len(b) :
    b = input("Enter only 1's and 0's: ")
    s = 0
    for c in range(0, len(b) - 1) :
        s += int(b[c])
# This loop combines the two actions before into one. The condition is that if
# the sum of all digits is greater than the number of digits there are, then it
# isn't in binary.

# The greatest possible sum of digits in a five digit binary should be
# 1 + 1 + 1 + 1 + 1 = 5, so len(b) is used.

dec = 0
# dec is the variable for storing the base 10 output.
m = len(b) - 1
# m is the last digit's element used for convenience.

for c in range(0, m + 1) :
    dec += int(b[c]) * pow(2, m - c)
# This loop goes through every digit in the binary and multiplies them by the
# appropriate value of 2^c, with c corresponding to the digit's place.

# Since the ordering of the list is opposite to the ordering of a binary, the
# program goes through the values of 2^c and b[c] reversely.

print("Decimal number is " + str(dec))
