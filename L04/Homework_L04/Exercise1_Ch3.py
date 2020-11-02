#Exercise 1 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the volume and surface area of a sphere 

import math

def main():
    
    print("This program calculates the volume and surface area of a sphere given its radius.")

    radius = float(input("Enter the radius of a sphere:" ))
    	
    volume_sphere =  4/3 * math.pi * radius**3
    surface_sphere = 4 * math.pi * radius**2


    print("The volume is: ", volume_sphere, "and the surface area is: ", surface_sphere)
    
main()