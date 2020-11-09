#Exercise 1 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program calculates the total wage for a week.")

	hours = float(input("Enter hours worked in this week: "))
	rate = float(input("Enter hourly rate: "))

	if hours <= 40:
		total_wage = hours * rate
	else:
		hours_extra = hours - 40
		total_wage = (40 * rate) + (hours_extra * (rate*1.5))

	print("The total wage for this week is", total_wage)

main()