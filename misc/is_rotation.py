# Find if one list is a rotation of another

def is_rotation(list1, list2):
    key_A = list1[0]
    key_B = -1
    if len(list1) != len(list2):
        return False
    for item in list2:
        if item == key_A:
            key_B = list2.index(item)
            break
    if key_B == -1:
        return False
    for item in list1:
        j = (key_B + list1.index(item)) % len(list1)
        if item != list2[j]:
            return False
    return True
    

list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
list2b = [4, 5, 6, 7, 1, 2, 3]
list2c = [4, 5, 6, 9, 1, 2, 3]
list2d = [4, 6, 5, 7, 1, 2, 3]
list2e = [4, 5, 6, 7, 0, 2, 3]
list2f = [1, 2, 3, 4, 5, 6, 7]
list2g = [7, 1, 2, 3, 4, 5, 6]

def test():
    assert is_rotation(list1, list2a) is False
    assert is_rotation(list1, list2b) is True
    assert is_rotation(list1, list2c) is False
    assert is_rotation(list1, list2c) is False
    assert is_rotation(list1, list2d) is False
    assert is_rotation(list1, list2e) is False
    assert is_rotation(list1, list2f) is True
    assert is_rotation(list1, list2g) is True