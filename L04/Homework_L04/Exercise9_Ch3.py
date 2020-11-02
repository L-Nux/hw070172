#Exercise 9 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the area of a triangle
import math
def main():
    
    print("This program calculates the area of a triangle.")

    a = float(input("Please enter the length of side a: "))
    b = float(input("Please enter the length of side b: "))
    c = float(input("Please enter the length of side c: "))

    s = (a+b+c)/2

    A = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("The area of the triangle is", A)
    
main()