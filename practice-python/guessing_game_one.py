# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, 
# too high, or exactly right. (Hint: remember to use the user input lessons from 
# the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, 
# print this out.

import random

try:
	rand = random.randint(1, 9)
	guess = int(input("Guess the number between 1 and 9: "))

	while guess != rand:		
		if guess > rand:
			print("{} is too high!".format(guess))
			guess = int(input("Guess once more: "))
		elif guess < rand:
			print("{} is too low!".format(guess))
			guess = int(input("Guess once more: "))
	else:
		print("Whoa! You won!!!")
except ValueError:
	print("Type number between 1 and 9, not letters")