#Exercise 7 CH8 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
import random

def main():

	print("This program finds prime summands of an even number.")

	number = int(input("Enter a positive integer >= 2: "))

	def is_prime(x):
		for i in range(2, x//2):
			if (x%i) == 0:
				break
		else:
			return x 

	def prime_range(n):
		return [x for x in range(2, n + 1) if is_prime(x) and x%2 != 0]

	def goldbach(z):
			if number >= 2 and number%2 == 0:
				return [(x, y) for x in prime_range(z) for y in prime_range(z) if x + y == z and x <= y]
			else:
				print("Invalid input!")

	print("The Goldbach conjecture for your input is: ", goldbach(number))
	
main()