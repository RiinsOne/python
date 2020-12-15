from random import randint


def matrix(n=5):
    lst = []
    for i in range(n):
        lst.append(list())
        for j in range(n):
           lst[i].append(randint(1, 3))

    return lst


#

index = 0
product = 1

for line in matrix(4):
    print(line)
    for element in line[:index]:
        product *= element
    index = index + 1

print()
print('product is: ', product)

print()

#
