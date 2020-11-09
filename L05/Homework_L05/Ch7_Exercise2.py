#Exercise 2 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates the grade given a quiz score.")

	score = int(input("Enter the quiz score (0-5): "))

	if score == 0 and score == 1:
		print("The corresponding grade to the entered score is F")
	elif score == 2:
		print("The corresponding grade to the entered score is D")
	elif score ==3:
		print("The corresponding grade to the entered score is C")
	elif score ==4:
		print("The corresponding grade to the entered score is B")
	elif score ==5:
		print("The corresponding grade to the entered score is A")
	else:
		print("Not a valid quiz score!")
main()