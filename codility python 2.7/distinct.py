def solution(A):
    length = len(A)
    A.sort()
    result = 1 #in case there would be only 1 element on a list
    for i in xrange(1, length):
        if A[i] != A[i-1]:
            result += 1
    return result
