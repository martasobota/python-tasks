# Find the most frequently occuring item in an array

def most_frequent(given_list):
    max_item = None
    item_occurences = 0
    check = dict()
    for n in given_list:
        if n in check:
            check[n] += 1
        else:
            check[n] = 1
        if check[n] > item_occurences:
            item_occurences = check[n]
            max_item = n
    return max_item

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

print(most_frequent(list1))
print(most_frequent(list2))
print(most_frequent(list3))
print(most_frequent(list4))
print(most_frequent(list5))
