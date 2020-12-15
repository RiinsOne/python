from random import randint


def matrix(n=5):
    lst = []
    for i in range(n):
        lst.append(list())
        for j in range(n):
            lst[i].append(randint(0, 10))

    return lst


for k in matrix():
    print(k)

#
