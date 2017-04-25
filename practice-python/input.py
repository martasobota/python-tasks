# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out 
# that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import date

name = input("What's your name? ")
age = int(input("How old are you? "))
number = int(input("Gimme some number: "))

borned_in = (date.today().year) - int(age)

hundred_yrs_yr = (int(borned_in) + 100)

for c in range(number):
	print("Hi {}, you will be 100 years old in {}, congratulations! \n".format(name, hundred_yrs_yr))

