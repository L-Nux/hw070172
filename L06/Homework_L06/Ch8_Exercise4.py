#Exercise 4 CH8 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates the Syracuse sequence for a given starting value. ")

	start_number = int(input("Enter a positive integer: "))

	if start_number < 0:
		print("Invalid input! ")
	else:
		print(start_number)
		while start_number != 1:
			if start_number %2 == 0:
				start_number = start_number/2
				print(start_number)
			else:
				start_number = 3*start_number +1
				print(start_number)
main()