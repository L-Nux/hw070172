#Exercise 10 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the length of a ladder
import math
def main():
    
    print("This program calculates the required length of a ladder")

    height = float(input("Please enter the height you want to reach: "))
    angle = float(input("Please enter the angle of the ladder in degrees: "))

    radians = (math.pi/180) * angle 
    length = height / math.sin(radians)

    print("The required length for the ladder is", length)
    
main()