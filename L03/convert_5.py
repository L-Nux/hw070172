#Exercise 11 CH2 (Zelle 2017, Python Programming: An Introduction to Computer Science)

#convert.py

# A program to convert Celsius temps to Fahrenheit

def main():
    
    print("This program converts data volume measured in bytes to kilobytes. ")

    byte = eval(input("Tell me the data volume in bytes? "))
    kiloBytes = byte * 0.001

    print("The data volume is", kiloBytes, "kilobytes.")
    input("Press the <Enter> key to quit.")
main()