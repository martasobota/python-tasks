# Write a program that takes a list of numbers 
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the 
# first and last elements of the given list. For practice, write this 
# code inside a function.

a = [5, 10, 15, 20, 25]

def first_last(a):
	result = []
	length = len(a)-1
	result.append(a[0])
	result.append(a[length])
	print(result)

first_last(a)