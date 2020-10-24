#Exercise 9 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to convert Celsius temps to Fahrenheit

def main():
    
    print("This program converts temperatures given in Fahrenheit to Celsius. ")

    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32)*5/9

    print("The temperature is", celsius, "degrees in Celsius.")
    input("Press the <Enter> key to quit.")
main()