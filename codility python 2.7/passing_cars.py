def solution(A):
    length = len(A)
    east = 0
    passing = 0
    for i in range(length):
        if A[i] == 0:
            east += 1
        else:
            passing += east

            if passing > 1000000000:
                return -1
    return passing
