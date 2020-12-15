import random
from ogframework import newline

L = ['самовар', 'весна', 'лето']


def func():
    randList = random.randint(0, (len(L) - 1))
    # print(randList)
    chosenWord = L[randList]
    # print(chosenWord)

    # newline()
    randChar = random.randint(0, (len(chosenWord) - 1))
    # print(randChar)
    chosenChar = chosenWord[randChar]
    # print(chosenChar)

    # newline()
    hiddenWord = chosenWord[:randChar] + '?' + chosenWord[randChar + 1:]
    print(hiddenWord)

    newline()
    guessChar = input('Угадай скрытую букву: ')
    if guessChar == chosenChar:
        print(f'Ты угадал, слово {chosenWord}')


# func()

# random.choice
# Return a random element from the non-empty sequence seq.
# If seq is empty, raises IndexError.

newline()
randomWord = random.choice(L)
print(randomWord)
randomChar = random.choice(randomWord)
print(randomChar)

#
