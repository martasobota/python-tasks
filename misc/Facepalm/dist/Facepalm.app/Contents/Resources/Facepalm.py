import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk
root = tk.Tk()
root.title("Facepalm 🤦🏻‍♂️")
tk.Button(root, text="Play the game! 🗻📄✂️🦎🤦🏻‍♂️").pack()
tk.mainloop()

import random

choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

print("\n--- Welcome to Sheldon Cooper's presents: Rock 🗻  Paper 📄  Scissors ✂️  Lizard 🦎  Spock 🤦🏻‍♂️ ---\n")
name = input("What's your name? ")


def play():

	#taking variable name inside the play function
	global name

	user = input("{}, type: Rock, Paper, Scissors, Lizard or Spock? \n".format(name))
	computer = random.choice(choices)

	#lowering cases in each choice to compare them easily and use later in comparisions
	user_lower = user.lower()
	comp_lower = computer.lower()
	choices_lower = [choice.lower() for choice in choices]

	while user_lower == comp_lower:
		print("Your and computer's choices are the same. You typed: {}, computer typed: {}".format(user, computer))
		
		#creating new choices for both user and computer
		user = input("Type once more: Rock, Paper, Scissors, Lizard or Spock? ")
		user_lower = user.lower()
		computer = random.choice(choices)
		comp_lower = computer.lower()

	if user.lower() in choices_lower:
		print("\nYou typed: {}, computer typed: {} \n".format(user, computer))
	elif user.lower() not in choices_lower or type(user) is int: #added or statement
		print("Wrong choice, type one of showed below: ")
		user = input("Type: rock, paper, scissors, lizard or Spock? ")
		user_lower = user.lower()
		computer = random.choice(choices)
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

	#ask for one more game	
	more = input("\nWanna play more (y/n)? ")
	if more == 'y' or more == 'yes':
		play()
	else:
		print('Bye, bye!')

play()