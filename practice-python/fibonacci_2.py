# Write a program that asks the user how many Fibonnaci numbers to generate 
# and then generates them. Take this opportunity to think about how you can 
# use functions. Make sure to ask the user to enter the number of numbers in 
# the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
# where the next number in the sequence is the sum of the previous two numbers 
# in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci_2():
	n = int(input("How many Fibonacci's numbers would you like to generate? "))-1
	a = 0
	b = 1
	result = []
	while (len(result)) <= n:
		result.append(a)
		c = a + b
		a = b
		b = c
	print (len(result))
	return result

print (fibonacci_2())