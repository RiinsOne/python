from ogframework import newline

# функция генератор
# yield возвращает генератор, вместо значения (return)


def myRange(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(myRange())  # <generator object myRange at 0x007B8BF0>

newline()
rangeOne = myRange(1, 5)
for i in rangeOne:
    print(i, end=' ')

#
