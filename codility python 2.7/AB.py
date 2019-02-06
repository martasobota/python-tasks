# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def add_ab(substring, A_count, B_count):
    substring += 'ab'
    A_count -= 1
    B_count -= 1
    return substring, A_count, B_count

def add_a(substring, A_count):
    substring += 'a'
    A_count -= 1
    return substring, A_count

def add_b(substring, B_count):
    substring += 'b'
    B_count -= 1
    return substring, B_count

def add_aa(substring, A_count):
    substring += 'aa'
    A_count -= 2
    return substring, A_count

def add_bb(substring, B_count):
    substring += 'bb'
    B_count -= 2
    return substring, B_count

def solution(A, B):
    substring = ''
    A_count = A
    B_count = B

    if A == B:
        substring += 'ab' * A
        return substring
    if abs(A-B) == 1:
        while A_count > B_count:
            if B_count != 0:
                substring, A_count, B_count = add_ab(substring, A_count, B_count)
            else:
                substring, A_count = add_a(substring, A_count)

        while A_count < B_count:
            if A_count != 0:
                substring, A_count, B_count = add_ab(substring, A_count, B_count)
            else:
                substring, B_count = add_b(substring, B_count)
    if abs(A-B) == 2:
        if A > B:
            substring, A_count = add_a(substring, A_count)
            while A_count > B_count:
                if B_count != 0:
                    substring, A_count, B_count = add_ab(substring, A_count, B_count)
                else:
                    substring, A_count = add_a(substring, A_count)
        else:
            substring, B_count = add_b(substring, B_count)
            while A_count < B_count:
                if A_count != 0:
                    substring, A_count, B_count = add_ab(substring, A_count, B_count)
                else:
                    substring, B_count = add_b(substring, B_count)
    if abs(A-B) == 3:
        if A > B:
            substring, A_count = add_a(substring, A_count)
            while A_count > B_count:
                if B_count != 0:
                    substring, A_count, B_count = add_ab(substring, A_count, B_count)
                else:
                    substring, A_count = add_aa(substring, A_count)
        else:
            substring, B_count = add_bb(substring, B_count)
            while A_count < B_count:
                if A_count != 0:
                    substring, A_count, B_count = add_ab(substring, A_count, B_count)
                else:
                    substring, B_count = add_b(substring, B_count)

    if abs(A-B) == 4:
        if A > B:
            while A_count > B_count:
                if B_count != 0:
                    substring += 'aab'
                    A_count -= 2
                    B_count -= 1
                else:
                    substring, A_count = add_aa(substring, A_count)
        else:
            while A_count < B_count:
                if A_count != 0:
                    substring += 'bba'
                    A_count -= 1
                    B_count -= 2
                else:
                    substring, B_count = add_b(substring, B_count)
    return substring


print(solution(5,4))
print(solution(4,5))
print(solution(5,3))
print(solution(3,5))
print(solution(4,1))
print(solution(1,4))
print(solution(6,2))
print(solution(2,6))