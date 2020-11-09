#Exercise 2 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program prints the lyrics of the song \"The Ants Go Marching\".")
    print()

    def sing(activity, number):
    	for i in range(2):
    		print("The ants go marching",number,"by",number,",hurrah, hurrah")
    	print("The ants go marching",number,"by",number,",")
    	print("The little one stops to",activity,",")
    	print("And they all go marching down to the ground.")
    	print("To get out of the rain.")
    	print("Boom! Boom! Boom!")

    sing("suck his thumb", "one")
    print()
    sing("tie his shoe", "two")
    print()
    sing("climb a tree", "three")
    print()
    sing("shut the door", "four")
    print()
    sing("take a dive", "five")
    print()
    sing("pick up sticks", "six")
    print()
    sing("call up Evan", "seven")
    print()
    sing("roller skate", "eight")
    print()
    sing("check the time", "nine")
    print()
    sing("shout \"The End\"", "ten")
    
main()