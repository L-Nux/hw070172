#Exercise 5 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates the BMI.")

	weight = float(input("Enter your weight (in pounds): "))
	height = float(input("Enter your height (in inches): "))

	bm_index = (weight*720) / height**2

	if bm_index < 19:
		print("You're below the healthy BMI range", bm_index)
	elif bm_index in range(19, 26):
		print("Your within the healthy BMI range", bm_index)
	elif bm_index > 25:
		print("You're above the healthy BMI range", bm_index)
	else:
		print("Not a valid input!")

main()