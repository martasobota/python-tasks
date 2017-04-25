# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one 
# number to divide by (check). If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.

num = int(input("Gimme your number: "))
check = int(input("Now, put number 2 to divide: "))


if num % 4 == 0:
	print("Your number is even and multiple of 4!")
elif num % 2 == 0:
	print("Your number is even")
elif num % 2 != 0:
	print("Your number is odd")
else:
	print("Number, please")

print("Now we'll check if your number can be divided be number 2")

result = num % check

if result == 0:
	print("Yes, you can divide number by number 2 and gain integer! ")
else:
	print("The result of the division won't be integer, it's {} ".format(result))