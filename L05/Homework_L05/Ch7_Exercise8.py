#Exercise 9 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program outputs a person's eligibility for the Senate or The House.")

	age = float(input("Enter your age): "))
	citizenship = float(input("For how many years have you been a US citizen: "))

	if age < 30:
		if age >= 25 and citizenship >= 7:
			print("You're eligible for The House")
		else:
			print("You're not eligible for neither The Senate nor The House")

	if age >=30:
		if citizenship >= 9:
			print("You're eligible for the Senate and the House")
		elif citizenship in range(7,9):
			print("You're eligible for The House")
		else:
			print("You're not eligible for neither The Senate nor The House")

main()