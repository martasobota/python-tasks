# Create a program that asks the user for a number and then prints out a list of 
# all the divisors of that number. (If you don’t know what a divisor is, it is a number 
# that divides evenly into another number. For example, 13 is a divisor of 26 
# because 26 / 13 has no remainder.)

number = int(input("Please pass the number: "))

def divisors():
	results = []
	for n in range(1, number):
		if number % n == 0:
			results.append(n)
			print("Divisors of {} are given numbers: {}".format(number, results))
	if not results:
		print("List is empty, there are no divisors for {}".format(number))

divisors()