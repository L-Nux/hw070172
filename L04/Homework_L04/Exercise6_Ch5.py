#Exercise 7 CH5 (Zelle 2017, Python Programming: An Introduction to Computer Science)

def main():
    
    print("This program calculates the numeric value of a full name.")

    name = input("Enter a single name: ")
    name_new = name.lower()
    name_new = name_new.replace(" ", "")

    numbers = []

    for n in name_new: 
    	numbers.append(int(ord(n)-96))

    print("The numeric value of the entered name-", name,"-is:", sum(numbers))

main()