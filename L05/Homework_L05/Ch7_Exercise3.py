#Exercise 3 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates the grade given a quiz score.")

	score = int(input("Enter the quiz score (0-100): "))

	if score < 60:
		print("The corresponding grade is: F")
	elif score in range(60, 70):
		print("The corresponding grade is: D")
	elif score in range(70, 80):
		print("The corresponding grade is: C")
	elif score in range(80, 90):
		print("The corresponding grade is: B")
	elif score in range(90, 101):
		print("The corresponding grade is: A")
	else:
		print("Not a valid quiz score!")

main()