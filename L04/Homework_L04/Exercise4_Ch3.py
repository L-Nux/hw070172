#Exercise 4 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to determine the distance to a lightning strike
import math

def main():
    
    print("This program determines the distance to a lightning strike.")

    time = int(input("Enter the time elapsed between flash and sound of thunder in in seconds: "))
    	
    distance = 1100*time
    distance_miles = distance / 5280
    print("The distance to the lightning strike is:", distance_miles, "miles.")
    
main()