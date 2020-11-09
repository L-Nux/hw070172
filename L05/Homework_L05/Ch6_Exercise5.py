#Exercise 5 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program does pizza calculations")
    print()
    radius = float(input("Enter the radius of the pizza: "))
    price = float(input("What is the price of the pizza: "))

    def pizza_area(r):
    	area = math.pi * (r)**2
    	return area

    area = pizza_area(radius)

    def pizza_costs(p, a):
    	costs = p / a
    	return costs

    print("The area of the pizza is:", area)
    print("The cost per square inch of the pizza: ", pizza_costs(price, area))


main()