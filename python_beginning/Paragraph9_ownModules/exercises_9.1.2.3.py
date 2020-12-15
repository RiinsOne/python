import math
from ogframework import newline


def func(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(round(s, 2))
    print(s)


func(2, 4, 5)

newline()
print(round(math.pi, 2))


def func1(x):
    return math.sqrt(1 - (math.sin(x) ** 2))


newline()
print(func1(2))

#
