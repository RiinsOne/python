from random import randint
from ogframework import newline

x = randint(1, 10)
print(x)


def func():
    ask = int(input('Try to guess a random number from 1 to 10: '))
    if ask == x:
        print('You won!')
    else:
        print('Try again!')
        return func()


func()


#
