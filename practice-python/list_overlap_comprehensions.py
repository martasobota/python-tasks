# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), 
# except require the solution in a different way.

# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. 

# Extra:

# Randomly generate two lists to test this

import random

list_1 = []
list_2 = []
# function creates two random lists of 15 and 20 elements from 0 to 25
def create_random_list():
	global list_1, list_2
	for n in range(15):
		list_1.append(random.randint(0, 25))
	for n in range(20):
		list_2.append(random.randint(0, 25))
	# print(list_1, list_2)
	# line below shows sorted list but without chaning the original nor creating a copy of new one
	print(sorted(list_1), sorted(list_2)) 

create_random_list()

print(list(set(list_1).intersection(list_2)))