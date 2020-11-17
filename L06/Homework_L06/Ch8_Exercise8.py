#Exercise 8 CH8 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
import random

def main():

	print("This program finds the GCD of two numbers.")

	m = int(input("Enter first positive integer: "))
	n = int(input("Enter second positive integer: "))

	def gcd_calculation(m,n):
		if m == 0:
			return n
		if n == 0:
			return m
		return gcd_calculation(n, m%n)

	print("GCD of {} and {} is {}".format(m, n, gcd_calculation(m,n))) 

main()