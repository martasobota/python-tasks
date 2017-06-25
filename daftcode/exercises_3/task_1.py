"""
Link to task description [PL]:
https://github.com/daftcode/zajecia_python_mini_edycja3/blob/master/zajecia_3/praca_domowa/praca_domowa.txt
"""
class SizeError(ValueError):
    pass


class Vector():
    def __init__(self, *args):
        self.coordinates = list(x for x in args)

    def __str__(self):
        return '{} ({})'.format(
            self.__class__.__name__, ', '.join((str(x) for x in self.coordinates))
        )

    def __eq__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise SizeError("Cannot compare vectors with different sizes")
        return self.coordinates == other.coordinates

    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise SizeError("Cannot add vectors with different sizes")
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
v3 = Vector(110, 220, 330, 440)
print("v1: {}\nv2: {}\nv3: {}".format(v1, v2, v3))
print("")
# print("Vectors {} and {} have the same coordinates: {}".format("v1", "v2", v1 == v2))
# print("Vectors {} and {} have the same coordinates: {}".format("v1", "v3", v1 == v3))
# print("Vectors {} and {} have the same coordinates: {}".format("v2", "v3", v2 == v3))
# print("")
print("Is v1 the same object as v2? Answear: {}".format(v1 is v2))
print("Is v1 the same object as v3? Answear: {}".format(v1 is v3))
print("Is v2 the same object as v3? Answear: {}".format(v2 is v3))
print("")
print("v2 + v3 = {}".format(v2 + v3))