#Exercise 7 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program computes the nth Fibonacci number")
    print()
    number = int(input("Enter the a whole number<0: "))

    def fibonacci(n):
    	if n == 0:
    		return 0
    	if n == 1:
    		return 1
    	else:
    		return fibonacci(n-1)+fibonacci(n-2)


    print("The n^th Fibonacci number is:", fibonacci(number))
main()