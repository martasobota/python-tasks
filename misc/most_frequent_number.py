# Find the most frequently occuring item in an array

def most_frequent(given_list):
    max_item = None
    check = dict()
    for n in given_list:
        if n in check:
            check[n] += 1
        else:
            check[n] = 1
    item_occurences = 0
    for item, value in check.items():
        if value > item_occurences:
            item_occurences = value
            max_item = item
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
