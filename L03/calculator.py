#Exercise 12 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to convert Celsius temps to Fahrenheit

def main():

    i = 0
    print("This program helps you calculate")

    while i < (100):

        calc = eval(input("Tell me your calculation? "))
        if type(calc) == int or type(calc) == float:
            print("The result of your calculation is: ", calc)
            i =  i+1
        elif type(calc) == str:
            break
main()