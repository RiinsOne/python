from random import randint

lst = [randint(0, 100) for i in range(1, 101)]
print(lst)
# print(len(lst) - 1)


def firstPairOfList(a):
    firstElemIndex = 0
    secondElemIndex = 1

    for i in a:
        firstPairElem = a[firstElemIndex]
        secondPairElem = a[secondElemIndex]
        # print('Значение 1 -', firstPairElem)
        # print('Значение 2 -', secondPairElem)
        # print('first', firstElemIndex)
        # print('second', secondElemIndex)

        if firstPairElem == secondPairElem and firstPairElem % 2 != 0:
            print(f'The first elements pair indexes are: {firstElemIndex}, {secondElemIndex}')
            break
        elif secondElemIndex < (len(a) - 1):
            firstElemIndex += 1
            secondElemIndex += 1
        else:
            print('There are no pair.')
            break


firstPairOfList(lst)

#
