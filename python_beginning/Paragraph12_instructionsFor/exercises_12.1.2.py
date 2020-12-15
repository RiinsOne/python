from ogframework import newline

# 12.1


def y():
    for x in range(10, 30, 2):
        print(x ** 2 + 3, end=' ')


y()

newline()
# 12.2

L = [-8, 8, 6.0, 5, 'строка', -3.1]

result = 0
for i in L:
    if type(i) == int:
        result += i
    if type(i) == float:
        result += i

print(result)


newline()

newList = []
for i in L:
    if type(i) == int:
        newList.append(i)
    if type(i) == float:
        newList.append(i)

print(newList)
print(sum(newList))

#
