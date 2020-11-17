#Exercise 3 CH8 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates how it takes for an investment to double. ")

	interest_rate = float(input("Enter the annualized interest rate: "))

	initial_i = 1
	investment = initial_i
	years = 0

	while investment <= initial_i*2:
		investment = investment + (investment * interest_rate)
		years += 1

	print("I takes", years,"year[s] to double your investement with the given interest rate.")


main()