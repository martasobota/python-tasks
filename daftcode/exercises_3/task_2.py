"""
Link to task description [PL]:
https://github.com/daftcode/zajecia_python_mini_edycja3/blob/master/zajecia_3/praca_domowa/praca_domowa.txt
"""

class MyIter():
    def __init__(self, *args):
        print('__init__ called')
        if len(args) == 0:
            raise TypeError("At least 1 argument expected")
        elif len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("At most 3 arguments expected")
        self.curr = self.start


    def __iter__(self):
        print('__iter__ called')
        self.curr = self.start - self.step
        return self

    def __next__(self):
        print('__next__ called')
        self.curr += self.step
        if self.step > 0:
            if self.curr < self.stop:
                return self.curr
            else:
                raise StopIteration
        elif self.step == 0:
            raise ValueError("MyIter() arg 3 must not be zero")
        elif self.step < 0:
            if self.curr > self.step:
                return self.curr
            else:
                raise StopIteration


assert [x for x in MyIter(0, 10)] == list(range(0, 10))
assert [x for x in MyIter(4)] == list(range(4))
assert [x for x in MyIter(2, 30, 5)] == list(range(2, 30, 5))
assert [x for x in MyIter(-50, -1, 7)] == list(range(-50, -1, 7))

#dlaczego to nie działa? liczby są 'na odwrót' ale ma iść od tyłu
assert [x for x in MyIter(-1, -50, -7)] == list(range(-1, -50, -7))