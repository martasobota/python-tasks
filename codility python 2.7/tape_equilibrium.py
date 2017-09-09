def solution(A):
    front = A[0]
    end = sum(A[1:])
    min_diff = abs(end-front)
    for i in range(1, len(A)-1):
        front += A[i]
        end -= A[i]
        if abs(front-end) < min_diff:
            min_diff = abs(front-end)
    return min_diff
