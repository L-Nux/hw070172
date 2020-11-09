#Exercise 4 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates class standing.")

	credits = float(input("Enter the credits earned: "))

	if credits < 7:
		print("You're a Freshman!")
	elif credits in range(7, 16):
		print("You're a Sophomore!")
	elif credits in range(16, 26):
		print("You're a Junior!")
	elif credits >= 26:
		print("You're a Senior!")
	else:
		print("Not a valid credit!")

main()