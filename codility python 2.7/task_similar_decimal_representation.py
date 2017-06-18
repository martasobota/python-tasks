from itertools import permutations

def solution(N):
    perms = [int(''.join(p)) for p in permutations(str(N))]
    return len(set(perms))