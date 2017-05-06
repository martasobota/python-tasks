# Write a program that asks the user how many Fibonnaci numbers to generate 
# and then generates them. Take this opportunity to think about how you can 
# use functions. Make sure to ask the user to enter the number of numbers in 
# the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
# where the next number in the sequence is the sum of the previous two numbers 
# in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)



# n = int(input("How many Fibonacci's numbers would you like to generate? "))
def fibonacci():
	n = int(input("How many Fibonacci's numbers would you like to generate? "))
	fib = [0, 1]
	for i in range(2, n+1):
		fib.append(fib[-1] + fib[-2])
	return fib

print (fibonacci())
