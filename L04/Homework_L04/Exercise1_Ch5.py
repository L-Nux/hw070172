#Exercise 1 CH5 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to 
import math
def main():
    
    print("This program converts the date layout")

    dateStr = input("Enter a date (mm/dd/yyyy): ")
    monthStr, dayStr, yearStr = dateStr.split("/")

    months = ["January", "February", "March", "April", "May", "June", 
    			"July", "August", "September", "October", "November", "December"]

    monthStr = months[int(monthStr)-1]

    print("The converted date is: {0}, {1}.{2}".format(monthStr, dayStr, yearStr) )
    
main()