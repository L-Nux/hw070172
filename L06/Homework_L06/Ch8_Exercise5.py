#Exercise 5 CH8 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
import random

def main():

	print("This program determines if a given number is prime. ")
	j=0
	number = int(input("Enter a positive integer > 2: "))

	stop = int(math.sqrt(number))+1

	divider = range(2, stop, 1)

	if number < 2:
		print("Invalid input! ")
	else:
		for d in divider:
			if number%d == 0:
				j=1
				print("The entered number",number,"is not prime number.")

	if j==0:
		print("The entered number is a prime number")


main()