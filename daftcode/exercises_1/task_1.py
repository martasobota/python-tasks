### Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według schematu: [[0], [2], ... , [98]]

### solution 1

def even_list():
    a = []
    for i in range(100):
        if i % 2 == 0:
            a.append([i])
    return a

# print("'Classic' for loop: ")
# print(even_list())

### solution 2 - list comprehension

def even_list_comprehension():
    return [[i] for i in range(100) if i % 2 == 0]

print(even_list_comprehension())

### solution 3

# shortes version
# print([[x] for x in range(0, 100, 2)])