def solution(A):
    length = len(A)
    if len(set(A)) == length and max(A) == length:
        return 1
    else:
        return 0