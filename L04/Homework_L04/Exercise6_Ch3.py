#Exercise 6 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the slope of a (non-vertical) line
import math

def main():
    
    print("This program calculates the slope of a (non-vertical) line.")

    x1, y1 = eval(input("Enter the first two coordinates: "))
    x2, y2 = eval(input("Enter the second two coordinates: "))

    slope = (y2 - y1) / (x2 - x1)

    print("The slope of the line is", slope)
    
main()