#Exercise 8 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to calculate the value of an investment

def main():
    
    print("This program calculates the the total accumulation of an investment")

    investment = eval(input("Enter the annual investment: "))
    rate = eval(input("Enter a yearly rate: "))
    periods = eval(input("Enter the number of times the interest is compounded each year: "))

    for i in range(10*periods):

        investment = investment * (1 + rate/periods)

    print("The value in 10 years is: ", investment)
    
main()