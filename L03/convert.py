#Exercise 2.1 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to convert Celsius temps to Fahrenheit

def main():
    
    print("This program converts temperature given in Celsius to Fahrenheit. ")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32

        print("The temperature is", fahrenheit, "degrees in Fahrenheit.")
    input("Press the <Enter> key to quit.")
main()