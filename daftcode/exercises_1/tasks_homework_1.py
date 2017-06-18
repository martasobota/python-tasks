### Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według schematu: [[0], [2], ... , [98]]

def even_list():
    a = []
    for i in range(100):
        if i % 2 == 0:
            a.append([i])
    return a

# print("'Classic' for loop: ")
# print(even_list())

# list comprehension
def even_list_comprehension():
    a = []
    [a.append([i]) for i in range(100) if i % 2 == 0]
    return a

# print('List comprehesion: ')
# print(even_list_comprehension())

# shortes version
# print([[x] for x in range(0, 100, 2)])

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

### Stworzyć listę 100 list, każda z liczbami od 0 do 100. Potem dla każdej j-tej z tych list wewnętrznych na jej końcu
### dodać sumę jej pierwszych j elementów. spodziewany efekt: [ [0, 1, 2, 3, ..., 100, 0], [0, 1, 2, 3, ..., 100, 1], [0, 1, 2, 3, ..., 100, 3], ..., [0, 1, 2, 3, ..., 100, 5050] ]

a = list(range(101))
print(a)
a_100 = [None] * 100
print("a_100 has {} elements".format(len(a_100)))
total = 0

for i in range(100):
    b = a[:]
    total += i
    b.append(total)
    a_100[i] = b

# print(a_100)
# print(a_100[i][-1] for i in range(100)

for i in range():
    # print(a_100[i][-1])

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

# Napisać kod transformujący podany słownik: 
# { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', } 
# do postaci: 
# { 'Poniedziałek': 1, 'Środa': 3, 'Piątek': 5, 'Niedziela': 7, } Zamiana klucza z wartością i zostawienie tylko dni nieparzystych

dict = { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', } 

for key in dict:
    print(key)


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

# Powerset - Napisać kod tworzęcy ze zbioru A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} zbiór zawierający wszystkie podzbiory A (włącznie z pustym i A). UWAGA: w python zbiory nie mogą być elementami innych zbiorów, proszę użyć tupli jako zbiorów wewnętrznych