#Exercise 6 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to calculate the value of an investment

def main():
    
    print("This program calculates the value of an investment ")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter an annual interest rate: "))
    years = eval(input("Enter the term of the investment in years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, " years is: ", principal)
    
main()