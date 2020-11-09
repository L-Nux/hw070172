#Exercise 9 CH7 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def main():

	print("This program outputs the date of Easter in the years 1982-2048")

	year = int(input("Enter a year in the range 1982-2048: "))

	if year in range(1982, 2049):

		a = year%19
		b = year%4
		c = year%7
		d = (19*a+24)%30
		e = (2*b + 4*c + 6*d + 5)%7

		if (d+e) <= 9:
			print("The date of Easter is March,", 22+(d+e), year)
		else:
			print("The date of Easter is April", (d+e) - 9, year)

	else:
		print("Not a valid input!")


main()