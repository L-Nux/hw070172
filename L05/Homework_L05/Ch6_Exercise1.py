#Exercise 1 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program prints the lyrics of the song \"Old MacDonald\".")
    print()

    def sing(animal, noise):
    	print("Old Macdonald had a farm, Ee-igh, Ee-igh, Oh!")
    	print("And on his farm he had a",animal, ", Ee-igh, Ee-igh, Oh!")
    	print("With a", noise,"-",noise, "here, and a", noise,"-",noise,"there")
    	print("Here a",noise,", there a", noise,"everywhere a", noise,"-",noise)
    	print("Old Macdonald had a farm, Ee-igh, Ee-igh, Oh!")

    sing("cow", "moo")
    print()
    sing("goat", "baa")
    print()
    sing("chicken", "cluck")
    print()
    sing("pig", "oink")
    print()
    sing("duck", "quack")
    
main()