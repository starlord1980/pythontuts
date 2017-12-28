#!/usr/bin/env python3
"""guesser.py program
I can write stuff here too

"""

import random


def main():
	print ("Guess a number between 1 and 100")
	randomNumber = random.randint(1,10)
	found = False #flag variable to see if they guess correctly

while not found:
	userGuess = input("your guess: ")
	if userGuess == randomNumber:
		print ("You guess correctly!")
		found = True
	elif userGuess > randomNumber:
		print ("Guess lower!")
	else:
		print ("Aim higher!")


if __name__ == "__main__":
	main()
