def solution(A):
    length = len(A)
    if length < 3:
        return 0 
    A.sort()
    for i in xrange(length-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0
