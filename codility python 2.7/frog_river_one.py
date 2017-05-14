def solution(X, A):
	covered = [-1] * X
	uncovered = X

	for i in range(0, len(A)):
	    if covered[A[i]-1] != -1:
	        continue
	    else:
	        covered[A[i]-1] = i
	        uncovered -= 1
	        if uncovered == 0:
	            return i
	return -1