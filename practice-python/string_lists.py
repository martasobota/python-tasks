# Ask the user for a string and print out whether this string is a palindrome 
# or not. (A palindrome is a string that reads the same forwards and backwards.)

def palindrome():
	s = input("Write something and I will check if it's palindrome: ")
	if s.lower() == (s[::-1]).lower():
		print("{} is a palindrome!".format(s))
	else:
		print("{} isn't a palindrome.".format(s))

palindrome()