from random import randint

lst = [randint(-100, 100) for i in range(1, 1001)]
print('list', lst)

countsElements = 0
for i in lst:
    countsElements += 1


def closestToAverage(a):
    averageValue = sum(a) / countsElements
    absValue = round(abs(averageValue))
    if absValue in lst:
        print(lst[absValue])
    else:
        print('There is no such element in the list')


closestToAverage(lst)

#
