def solution(A):
    appear = [False] * (len(A)+1)
    for i in A:
        if 1 <= i <= len(A)+1:
            appear[i-1] = True
    
    for i in xrange(len(A)+1):
        if appear[i] == False:
            return i + 1
    return -1
