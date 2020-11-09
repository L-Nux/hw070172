#Exercise 7 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates babysitter charges")

	start_time = float(input("Enter the start time (0-24): "))
	end_time = float(input("Enter the end time (0-24): "))

	if end_time <= 21:
		charge = (end_time-start_time)*2.5
		print("The babysitting bill is:", charge)
	else:
		charge_till9 = (21-start_time)*2.5
		charge_from9 = (end_time-21)*1.75
		charge = charge_till9+charge_from9
		print("The babysitting bill is:", charge)

main()