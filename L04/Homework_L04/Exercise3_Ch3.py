#Exercise 3 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the molecular weight of a carbohydrate
import math

def main():
    
    print("This program calculates the molecular weight of a carbohydrate.")

    hydrogen = int(input("Enter the number of hydrogen atoms: "))
    carbon = int(input("Enter the number of carbon atoms: "))
    oxygen = int(input("Enter the number of oxygen atoms: "))
    	
    carbohydrate = hydrogen*(1.00794)+carbon*(12.0107)+oxygen*(15.9994)

    print("The molecular weight of carbohydrate is: ", carbohydrate, "grams/mole.")
    
main()