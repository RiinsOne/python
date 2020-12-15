from random import randint

lst = [randint(10, 100) for i in range(1, 11)]
print(lst)


def diff(a):
    maxNum = max(a)
    minNum = min(a)
    return maxNum - minNum


print(diff(lst))


#