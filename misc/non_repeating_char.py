def non_repeating(given_string):
    check = {}
    for item in given_string:
        if item not in check:
            check[item] = 1
        else:
            check[item] += 1
    for item in check:
        if check[item] == 1:
            return item
    return None


def test():
    assert non_repeating("abcab") == 'c'
    assert non_repeating("abab") == None
    assert non_repeating("aabbbc") == 'c'
    assert non_repeating("aabbdbc") == 'd'
# run on pytest based on python 3.7, where the dict is ordered
