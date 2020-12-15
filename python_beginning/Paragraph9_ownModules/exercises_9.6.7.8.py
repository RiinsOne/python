import math
from ogframework import newline
from random import randint


def funcz(x, y):
    # numerator - числитель
    # denominator - знаменатель
    numer = (x + (2 + y) / x ** 2)
    denom = (y + (1 / math.sqrt(x ** 2 + 10)))

    return round(numer / denom, 2)


print(funcz(2, 4))
print(funcz(4, 2))


def funcq(x, y):
    return round((2.8 * math.sin(x) + abs(y)), 2)


newline()
print(funcq(2, 4))
print(funcq(-4, -8))


def func_f(x):
    if x >= 0.2 and x <= 0.9:
        return round(math.sin(x), 2)
    return 1


newline()
print(func_f(0.8))
print(func_f(0.1))


def cub():
    player1 = randint(1, 6)
    player2 = randint(1, 6)

    if player1 > player2:
        print(f'First player won, with number {player1} against {player2}.')
    elif player1 < player2:
        print(f'Second player won, with number {player2} against {player1}.')
    else:
        print(f'It\'s draw, they got {player1}.')


newline()
cub()


#
