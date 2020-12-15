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
    for element in line[index:]:
        product *= element
    index += 1
    print(line[index:])

print()
print('product is: ', product)

print()


# однострочный вариант написания матрицы
newMatrix = [[randint(-3, 3) for j in range(5)] for i in range(5)]
for x in newMatrix:
    print(x)

#