#Exercise 8 CH3 (Zelle 2017, Python Programming: An Introduction to Computer Science)

# A program to calculate the Gregorian epact

def main():
    
    print("This program determines the Gregorian epact.")

    year = int(input("Please type in a 4-digit year: "))

    c = year // 100

    epact = (8+(c//4) - c + ((8*c+13)//25) + 11*(year%19))%30

    print("The Gregorian epact for the year", year, "is", epact)
    
main()