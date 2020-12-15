from random import randint

lst = [randint(1, 100) for i in range(1, 1001)]
print('list', lst)

#


def func(a):
    evenCounts = 0

    for i in a:
        if i % 2 == 0:
            evenCounts += 1

    fiveCount = 0
    newLst = list()
    for i in a:
            newLst.append(str(i))
    for i in newLst:
        for j in i:
            if j[len(j)-1] == '5':
                fiveCount += 1
    # print(newLst)

    tpl = (evenCounts, fiveCount)

    return tpl


print(func(lst))

#
