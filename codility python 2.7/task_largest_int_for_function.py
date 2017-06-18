def solution(N):
    if N == 0:
        return 0
        
    result = 0
    
    for i in range(1, N):
        f = f(i-1) + i
        # i -= 1
        
        if f <= N:
            result = f
        else:
            return result
    return result

print solution(17)