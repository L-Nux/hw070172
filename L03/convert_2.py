#Exercise 5 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to convert Celsius temps to Fahrenheit

def main():
    
    print("This program shows the conversion of Celsius to Fahrenheit. ")
    cels = 0,10,20,30,40,50,60,70,80,90,100
    for i in cels:
        fahrenheit = 9/5 * i + 32
        print(i, "Celsius are ", fahrenheit, "Fahrenheit degree")
    
main()