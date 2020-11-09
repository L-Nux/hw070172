#Exercise 3 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program calculates the volume of a sphere.")
    print()
    radius = float(input("Enter the radius of the surface: "))

    def sphere_area(radius):
    	area = 4 * math.pi * radius**2
    	return area

    def sphere_volume(radius):
    	volume = ((4/3) * math.pi * radius**3)
    	return volume

    print("The surface area is: ", sphere_area(radius), "and the volume is: ", sphere_volume(radius))

main()