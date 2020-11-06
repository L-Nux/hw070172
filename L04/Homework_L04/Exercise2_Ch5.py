#Exercise 2 CH5 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program prints the grade of a quiz score.")

    score = int(input("Enter the quiz score: "))
    grades = ["A", "B", "C", "D", "F"]

    if score == 0 or score == 1:
    	print("The corresponding grade is: ", grades[4])
    elif score == 2:
    	print("The corresponding grade is: ", grades[3])
    elif score == 3:
    	print("The corresponding grade is: ", grades[2])
    elif score == 4:
    	print("The corresponding grade is: ", grades[1])
    elif score == 5:
    	print("The corresponding grade is: ", grades[0])
    else:
    	print("This is not a valid input.")	
      
main()