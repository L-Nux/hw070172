#Exercise 2 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the cost per square inch of a circular pizza

import math

def main():
    
    print("This program calculates the the cost per square inch of a circular pizza given its diameter and price.")

    diameter = float(input("Enter the diameter of the pizza in inches:" ))
    price = float(input("Enter the price of the pizza:" ))
    	
    area = math.pi * (diameter/2)**2
    price_perInch = price/area

    print("The cost per square inch for the pizza is: ", price_perInch)
    
main()