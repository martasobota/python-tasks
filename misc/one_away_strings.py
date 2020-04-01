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
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) == len(s2):
        index_1 = 0
        index_2 = 0
        result = 0
        for i in range(len(s1)-1):
            if s1[i] != s2[i]:
                result += 1
                if result > 1:
                    return False

    # if abs(len(s1) - len(s2)) == 1:
    #     pass
    return True
    # result = 0
    # check_1 = create_table(s1)
    # check_2 = create_table(s2)
    # for item in s1:
    #     if item in check_2:
    #         if check_1[item] != check_2[item]:
    #             result += 1
    #             # print(check_1[item] == check_2[item])
    #             # print(check_1[item], " porównuję do", check_2[item])
    #             # print("result ", result)
    #     if result > 1:
    #         return False
    # return True


is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
print(is_one_away("aaa", "abc"))  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False

def test():
    assert is_one_away("abcde", "abcd") == True
    assert is_one_away("abde", "abcde") == True
    assert is_one_away("a", "a") == True
    assert is_one_away("abcdef", "abqdef") == True
    assert is_one_away("abcdef", "abccef") == True
    assert is_one_away("abcdef", "abcde") == True
    assert is_one_away("aaa", "abc") == False
    assert is_one_away("abcde", "abc") == False
    assert is_one_away("abc", "abcde") ==False
    assert is_one_away("abc", "bcc") == False