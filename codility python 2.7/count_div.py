A = 6
B = 11
K = 2

def solution(A, B, K):
    result = 0
    for i in range(A, B):
        if i % K == 0:
            result += 1
    return result

# print solution(A, B, K)
