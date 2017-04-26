# Rock/Paper/Scissors with Big Bang's addition, enjoy 😁 

# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors

import random

choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

print("\n--- Welcome to Sheldon Cooper's presents: Rock 🗻 Paper 📄 Scissors ✂️ Lizard 🦎 Spock 🤦🏻‍♂️ ---\n")
name = input("What's your name? ")


def play():
	global name
	user = input("{}, type: Rock, Paper, Scissors, Lizard or Spock? \n".format(name))
	computer = random.choice(choices)

	while user.lower() == computer.lower():
		print("Your and computer's choices are the same. You typed: {}, computer typed: {}".format(user, computer))
		user = input("Type once more: Rock, Paper, Scissors, Lizard or Spock? ")
		computer = random.choice(choices)
	choices_lower = [choice.lower() for choice in choices]
	if user.lower() in choices_lower:
		print("\nYou typed: {}, computer typed: {} \n".format(user, computer))
	else:
		print("Wrong choice, type one of showed below: ")
		user = input("Type: rock, paper, scissors, lizard or spock? ")

	user_lower = user.lower()
	comp_lower = computer.lower()

	if user_lower == 'scissors' and comp_lower == 'paper':
		print("{}, you won🏆, scissors cuts paper!".format(name))
	elif user_lower == 'paper' and comp_lower == 'scissors':
		print("{}, you loose, computer's scissors cuts your paper!".format(name))

	elif user_lower == 'paper' and comp_lower == 'rock':
		print("{}, you won🏆, paper covers rock!".format(name))
	elif user_lower == 'rock' and comp_lower == 'paper':
		print("{}, you loose, computer's paper covers your rock!".format(name))

	elif user_lower == 'rock' and comp_lower == 'lizard':
		print("{}, you won🏆, rock crushes lizard!".format(name))
	elif user_lower == 'lizard' and comp_lower == 'rock':
		print("{}, you loose, computer's rock crashes your lizard!".format(name))

	elif user_lower == 'lizard' and comp_lower == 'spock':
		print("{}, you won🏆, lizard poisons Spock!".format(name))
	elif user_lower == 'spock' and comp_lower == 'lizard':
		print("{}, you loose, computer's lizard poisons your Spock!".format(name))

	elif user_lower == 'spock' and comp_lower == 'scissors':
		print("{}, you won🏆, Spock smashes scissors!".format(name))
	elif user_lower == 'scissors' and comp_lower == 'spock':
		print("{}, you loose, computer's Spock smashes your scissors!".format(name))

	elif user_lower == 'scissors' and comp_lower == 'lizard':
		print("{}, you won🏆, scissors decapitates lizard!".format(name))
	elif user_lower == 'lizard' and comp_lower == 'scissors':
		print("{}, you loose, computer's scissors decapitates your lizard!".format(name))

	elif user_lower == 'lizard' and comp_lower == 'paper':
		print("{}, you won🏆, lizard eats paper!".format(name))
	elif user_lower == 'paper' and comp_lower == 'lizard':
		print("{}, you loose, computer's lizard eats your paper!".format(name))

	elif user_lower == 'paper' and comp_lower == 'spock':
		print("{}, you won🏆, paper disproves Spock!".format(name))
	elif user_lower == 'spock' and comp_lower == 'paper':
		print("{}, you loose, computer's paper disproves your Spock".format(name))

	elif user_lower == 'spock' and comp_lower == 'rock':
		print("{}, you won🏆, Spock vaporizes rock!".format(name))
	elif user_lower == 'rock' and comp_lower == 'spock':
		print("{}, you loose, computer's Spock vaporizes your rock!".format(name))

	elif user_lower == 'rock' and comp_lower == 'scissors':
		print("{}, you won🏆, rock crushes scissors!".format(name))
	elif user_lower == 'scissors' and comp_lower == 'rock':
		print("{}, you loose, computer's rock crushes your scissors!".format(name))
	more = input("\nWanna play more (y/n)? ")
	if more == 'y' or more == 'yes':
		play()
	else:
		print('Bye, bye!')

play()