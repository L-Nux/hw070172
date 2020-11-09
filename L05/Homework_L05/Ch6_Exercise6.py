#Exercise 6 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program computes the area of a triangle.")
    print()
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    def area_triangle(a,b,c):
    	s = (1/2)*(a+b+c)
    	area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    	return area 

    print("The area of the triangle is: ", area_triangle(a,b,c))
main()