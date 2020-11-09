#Exercise 6 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates speeding fines")

	speed_limit = float(input("Enter the speed limit: "))
	speed_clocked = float(input("Enter the clocked speed: "))

	if speed_clocked <= speed_limit:
		print("Speed is legal!")
	else:
		if speed_clocked < 90:
			fine = 50 + (speed_clocked-speed_limit)*5
			print("The fine is: ", fine)
		else:
			fine = 250 + (speed_clocked-speed_limit)*5
			print("The fine is ", fine)

main()