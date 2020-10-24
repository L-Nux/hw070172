#Exercise 7 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to calculate the value of an investment

def main():
    
    print("This program calculates the the total accumulation of an investment")

    investment = eval(input("Enter the annual investment: "))
    apr = eval(input("Enter an annual interest rate: "))
    years = eval(input("Enter the term of the investment in years: "))

    futureValue = 0

    for i in range(years):
        futureValue = futureValue+investment
        futureValue = futureValue * (1 + apr)

    print("The value in", years, "years is: ", futureValue)
    
main()