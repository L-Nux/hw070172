#Exercise 4 CH5 (Zelle 2017, Python Programming: An Introduction to Computer Science)

def main():
    
    print("This program prints the acronym of a phrase.")

    phrase = input("Enter a phrase: ")
    words = phrase.split()

    characters = []

    for w in words:
    	characters.append(w[0])

    acronym = "".join(characters)
    acronym = acronym.upper()
    
    print(acronym)

main()