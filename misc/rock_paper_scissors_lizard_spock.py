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





------------------------------------------------------------------------------------------------



# Rock-paper-scissors-lizard-Spock 
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# and calculate the winner of the game
import random


# helper functions
def number_to_name(number):    
    # converts number to a name using if/elif/else    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'

    
def name_to_number(name):    
    # converts name to number using if/elif/else    
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4


def rpsls(name):
    # converts name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # computes random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)        
    
    # computes difference of player_number and comp_number and uses mod five
    # if diff 1 or 2 player wins
    # if diff 3 or 4 computer wins
    # if diff 0 no one wins
    diff = (player_number - comp_number) % 5
        
    
    # using if/elif/else to determine winner    
    if diff == 1 or diff == 2:
        winner = 'Player'
    if diff == 3 or diff == 4:
        winner = 'Computer'
    
    
    # prints results
    print "Player choose: ", number_to_name(player_number)
    print "Computer choose: ", number_to_name(comp_number) 
    if diff:   
        print winner, "wins!\n"
    else:
        print "We have a tie!\n"
 

# test
if __name__=='__main__': 
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")