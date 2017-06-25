"""
Link to task description [PL]:
https://github.com/daftcode/zajecia_python_mini_edycja3/blob/master/zajecia_2/praca_domowa/praca_domowa.txt
"""

class Vector():
    def __init__(self, *args):
        self.coordinates = list(x for x in args)

    def __str__(self):
        return '{} ({})'.format(
            self.__class__.__name__, ', '.join((str(x) for x in self.coordinates))
        )

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        ### beta version ;)
        # coordinates_1 = self.coordinates
        # coordinates_2 = other.coordinates
        # coordinates_result = []

        # n = max(len(coordinates_1), len(coordinates_2))
        # i = 0
        # while n > 0:
        #     coordinates_result.append(coordinates_1[i] + coordinates_2[i])
        #     i += 1
        #     n -= 1
        # return coordinates_result

        ### alfa version
        n = max(len(self.coordinates), len(other.coordinates))
        coordinates_result = [self.coordinates[i] + other.coordinates[i] for i in range(n)]
        return Vector(*coordinates_result)

    def __mul__(self, other):
        multiply_result = [x * other for x in self.coordinates]
        return Vector(*multiply_result)

    def __rmul__(self, other):
        return self * other

v1 = Vector(10, 20, 30)
v2 = Vector(90, 80, 70)
v3 = Vector(10, 20, 30)
print("v1: {}\nv2: {}\nv3: {}".format(v1, v2, v3))
print(" ")
print("v1 id: {}".format(id(v1)))
print("v2 id: {}".format(id(v2)))
print("v3 id: {}".format(id(v3)))
print(" ")
print("Vectors {} and {} have the same coordinates: {}".format("v1", "v2", v1 == v2))
print("Vectors {} and {} have the same coordinates: {}".format("v1", "v3", v1 == v3))
print("Vectors {} and {} have the same coordinates: {}".format("v2", "v3", v2 == v3))
print("")
print("Is v1 the same object as v2? Answear: {}".format(v1 is v2))
print("Is v1 the same object as v3? Answear: {}".format(v1 is v3))
print("Is v2 the same object as v3? Answear: {}".format(v2 is v3))
print("")
print("v2 + v3 = {}".format(v2 + v3))
print("")
print("Multiplication vector * number:")
print(v1 * 10)
print(v2 * 10)
print(v3 * 10)
print("")
print("Multiplication number * vector:")
print(10 * v1)
print(10 * v2)
print(10 * v3)