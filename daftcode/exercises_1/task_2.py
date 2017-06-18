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