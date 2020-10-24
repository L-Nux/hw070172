#Exercise 10 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to convert Celsius temps to Fahrenheit

def main():
    
    print("This program converts distances measured in kilometres to miles. ")

    km = eval(input("Tell me the distance in kilometres? "))
    miles = km * 0.62

    print("The distance is", miles, "miles.")
    input("Press the <Enter> key to quit.")
main()