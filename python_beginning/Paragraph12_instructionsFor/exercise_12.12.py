from random import randint


def matrix(n=4, m=6):
    lst = []
    for i in range(n):
        lst.append(list())
        for j in range(m):
           lst[i].append(randint(0, 5))

    return lst


for k in matrix():
    print(k)

#

print()
print()

countLst = []
for line in matrix(3, 8):
    print(line)
    countNum = 0
    for elem in line:
        if line.count(elem) > countNum:
            countNum = line.count(elem)
    countLst.append(countNum)
    maxLine = countLst.index(max(countLst))
print()
print(countLst)
print()
print(maxLine)


#
