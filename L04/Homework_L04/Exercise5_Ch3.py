#Exercise 5 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the cost of a coffee order
import math

def main():
    
    print("This program calculate the cost of a coffee order.")

    pounds = float(input("Enter the amount of coffe you want to order in pounds: "))
    fixed_cost=1.5

    order = 10.5*(pounds)+0.86*(pounds)+fixed_cost

    print("The cost of your coffee order for", pounds,"pounds of coffee is", order,"$.")
    
    
main()