#Exercise 3 CH5 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program prints the grade of a quiz score.")

    score = int(input("Enter the quiz score: "))
    grades = ["A", "B", "C", "D", "F"]

    if score < 60:
    	print("The corresponding grade is: ", grades[4])
    elif score in range(60, 70):
    	print("The corresponding grade is: ", grades[3])
    elif score in range(70, 80):
    	print("The corresponding grade is: ", grades[2])
    elif score in range(80, 90):
    	print("The corresponding grade is: ", grades[1])
    elif score in range(90, 101):
    	print("The corresponding grade is: ", grades[0])
      
main()