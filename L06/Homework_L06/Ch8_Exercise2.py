#Exercise 2 CH8 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates and outputs until the nth Fibonacci number.")

	count = 0
	number1= 0
	number2= 1

	number_n = int(input("Enter a number >=1 :  "))

	if number_n <= 0:
		print("Not a valid input! ")
	else:
		print("This is your Fibonacci sequence: ")
		while count < number_n:
			next_number = number1 + number2
			print(number1)
			number1 = number2
			number2 = next_number
			count += 1

main()