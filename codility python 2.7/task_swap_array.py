def solution(A):
    
    counter = 0
    A_sorted = sorted(A)
    length = len(A)
    
    for i in range(0, length):
        if A[i] != A_sorted[i]:
            counter += 1
    if counter <= 2:
        return True
    else: 
        return False
