# A = [1, 2, 2, 4, 6, 6, 8, 8, 8, 1, 1, 2]

# solution 1

def solution_1(A):
	B = []
	for i in A:
		if i not in B:
			B.append(i)
	return B


# solution 2
def solution_2(A):
	return set(A)

# print solution_1(A)
# print solution_2(A)