#Exercise 4 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program does two different sum calculations.")
    print()
    number_n = int(input("Enter a natural number: "))

    def sumN(n):
    	sumOfn = (n/2)*(n+1)
    	return sumOfn

    def sumNCubes(n):
    	sumCubes = ((n*(n+1)) / 2)**2
    	return sumCubes

    print("The sum of the first", number_n,"natural numbers is:", sumN(number_n))
    print("The sum of the cubes of the first", number_n,"natural numbers is:", sumNCubes(number_n))

main()