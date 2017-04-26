# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
# (using input), compare them, print out a message of congratulations to 
# the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

choices = ['rock', 'paper', 'scissors']

print("\n--- Welcome to Rock 🗻 Paper 📄 Scissors ✂️ ---\n")
name = input("What's your name? ")


def play():
	global name
	user = input("{}, type: Rock, Paper or Scissors? \n".format(name))
	computer = random.choice(choices)

	while user.lower() == computer.lower():
		print("Your and computer's choices are the same. You typed: {}, computer typed: {}".format(user, computer))
		user = input("Type once more: Rock, Paper or Scissors? ")
		computer = random.choice(choices)
	choices_lower = [choice.lower() for choice in choices]
	if user.lower() in choices_lower:
		print("\nYou typed: {}, computer typed: {} \n".format(user, computer))
	else:
		print("Wrong choice, type one of showed below: ")
		user = input("Type: rock, paper or scissors: ")

	user_lower = user.lower()
	comp_lower = computer.lower()

	if user_lower == 'rock' and comp_lower == 'scissors':
		print("{}, you won🏆, rock crushes scissors!".format(name))
	elif user_lower == 'scissors' and comp_lower == 'rock':
		print("{}, you loose, computer's rock crushes your scissors!".format(name))

	elif user_lower == 'scissors' and comp_lower == 'paper':
		print("{}, you won🏆, scissors cuts paper!".format(name))
	elif user_lower == 'paper' and comp_lower == 'scissors':
		print("{}, you loose, computer's scissors cuts your paper!".format(name))

	elif user_lower == 'paper' and comp_lower == 'rock':
		print("{}, you won🏆, paper covers rock!".format(name))
	elif user_lower == 'rock' and comp_lower == 'paper':
		print("{}, you loose, computer's paper covers your rock!".format(name))


	more = input("\nWanna play more (y/n)? ")
	if more == 'y' or more == 'yes':
		play()
	else:
		print('Bye, bye!')

play()