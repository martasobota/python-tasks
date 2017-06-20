# Powerset - Napisać kod tworzący ze zbioru A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} zbiór zawierający wszystkie podzbiory A 
# (włącznie z pustym i A). UWAGA: w python zbiory nie mogą być elementami innych zbiorów, proszę użyć tupli jako zbiorów wewnętrznych

from itertools import chain, combinations

A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

def powerset(iterable):
    s = list(iterable)
    result = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return list(result)

print(powerset(A))