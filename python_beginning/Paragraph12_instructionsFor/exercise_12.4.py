from ogframework import newline
from random import randint


def guessNum():
    randNum = randint(1, 100)
    enteredNum = input('Try to guess the number from 1 to 100 or type "stop" to exit: ')

    while True:
        if enteredNum == 'stop':
            print('Exiting the program. Bye!')
            break
        elif int(enteredNum) > randNum:
            print('The entered number is bigger that guessed,')
            enteredNum = input('try again: ')
        elif int(enteredNum) < randNum:
            print('The entered number is lower that guessed,')
            enteredNum = input('try again: ')
        else:
            print(f'You won, the guessed number is {enteredNum}!')
            break


guessNum()

#
