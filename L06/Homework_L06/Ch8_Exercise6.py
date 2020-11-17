#Exercise 6 CH8 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
import random

def main():

	print("This program finds every prime number less than or equal to a given number.")

	number = int(input("Enter a positive integer > 2: "))

	possible_prime = range(2, number+1)

	if number < 2:
		print("Invalid input! ")

	print("The prime number sequence up to the entered number is:")

	for p in possible_prime:
		for i in range(2, p//2):
			if (p%i) == 0:
				break
		else:
			print(p)
main()