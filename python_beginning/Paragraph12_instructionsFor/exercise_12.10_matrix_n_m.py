from random import randint


def matrix(n=4, m=6):
    lst = []
    for i in range(n):
        lst.append(list())
        for j in range(m):
            lst[i].append(randint(0, 10))

    return lst


for k in matrix():
    print(k)

#

print()
print()
# вариант в одну строчку
matrix2 = [[randint(-3, 3) for j in range(6)] for i in range(4)]

for a in matrix2:
    print(a)

#
