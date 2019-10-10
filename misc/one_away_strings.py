# Implement your function below.
def create_table(s):
    table = {}
    for item in s:
        if item in table:
            table[item] += 1
        else:
            table[item] = 1
    return table

def is_one_away(s1, s2):
    result = 0
    check_1 = {}
    check_2 = {}
    for item in s1:
        if item in check_1:
            check_1[item] += 1
        else:
            check_1[item] = 1
    if abs(len(s1) - len(s2)) > 1:
        return False
    if result > 1:
        return False
    f

# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
