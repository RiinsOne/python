from ogframework import newline
from random import randint

a = []
for i in range(1, 16):
    a += [i]
print(a)

b = []
for i in range(1, 6):
    b.append(i)
print(b)

c = list(range(1, 16))
print(c)

# "списковое включение" или "генератор списка"
d = [i for i in range(1, 6)]
print(d)

newline()
e = [i**2 for i in range(1, 6)]
print(e)  # [1, 4, 9, 16, 25]

newline()
f = [i**2 for i in range(1, 6) if i != 4]  # число 4 цикл пропустит
print(f)  # [1, 4, 9, 25]

newline()
A = [2, -2, 4, -4, 7, 5]
B = [i**2 for i in A]
print(B)  # [4, 4, 16, 16, 49, 25]

newline()
C = [i*3 for i in 'list' if i != 'i']  # перебираем 'list', исключая 'i'
print(C)  # ['lll', 'sss', 'ttt']


def f(x):
    return x + 5


newline()
D = list(map(f, [1, 3, 4]))  # функция map
print(D)  # [6, 8, 9]
# Функции, которые принимают на вход другие функции,
# называются "функциями высшего порядка".

"""
Функция map() принимает на вход в качестве аргументов имя функции
и список (или строку).
Получить результат вызова функции можно через цикл for или list()
"""


def f2(s):
    return s*2


newline()
E = list(map(f2, 'hello'))
print(E)  # ['hh', 'ee', 'll', 'll', 'oo']


# список из случайных целых чисел
AA = [randint(1, 9) for i in range(5)]
print(AA)  # [5, 2, 8, 4, 2]


#
