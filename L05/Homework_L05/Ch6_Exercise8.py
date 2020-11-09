#Exercise 8 CH6 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math
def main():
    
    print("This program guesses the squareroot of number x.")
    print()
    x = int(input("Enter the a number: "))
    numb_guesses = (int(input("How many times should be guessed: ")))
    guess_value = x/2

    def nextGuess(g_value, x):
    	g = (g_value + (x/g_value)) / g_value
    	return g

    for i in range(numb_guesses):
    	n_guess = nextGuess(guess_value, x)

    diff = (math.sqrt(x)) - n_guess

    print("The next guess is:", n_guess)
    print("The difference to the squareroot of x =", diff)
main()