# Non-unique Elements description:
# You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
# Input: A list of integers.
# Output: The list of integers.
# How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).
# Precondition:
# 0 < len(data) < 1000

def checkio(data):
	result = []
	for element in data:
		if type(element) is int:
			if data.count(element) > 1:
				result.append(element)
		else:
			print("Type of input should be a list of integers")
	return result


# Tests for the task:

print(checkio([1,2,3,4,4,5,6,7,7,9,9,0,0,0,1]))
print(checkio([2, 33, 33, "name", 33])) #This test returns a list of 33, 33, 33 and an information from else statement


if __name__ == "__main__":
	if checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]: 
		print("1st test passed")
	else:
		print("1st test failed")
	if checkio([1, 2, 3, 4, 5]) == []:
		print("2nd test passed")
	else:
		print("2nd test failed")
	if checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]:
		print("3rd test passed")
	else:
		print("3rd test failed")
	if checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]:
		print("4th test passed")
	else:
		print("4th test failed")


