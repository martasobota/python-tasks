"""
Link to task description [PL]:
[zadnaie 3]
https://github.com/daftcode/zajecia_python_mini_edycja3/blob/master/zajecia_3/praca_domowa/praca_domowa.txt
"""

def collatz_gen(x):
    yield x
    while x != 1:
        if x % 2 == 0:
            x /= 2
            print(int(x))
        else:
            x = (x * 3) +1
            print(int(x))
        yield x
    raise StopIteration

# print(collatz_gen(1234))

assert list(collatz_gen(1)) == [1]
assert list(collatz_gen(2)) == [2, 1]
assert list(collatz_gen(3)) == [3, 10, 5, 16, 8, 4, 2, 1]
assert list(collatz_gen(12)) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert list(collatz_gen(19)) == [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]