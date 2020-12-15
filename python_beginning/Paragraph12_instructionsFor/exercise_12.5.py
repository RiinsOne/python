from ogframework import newline

# вариант 1


def func():
    a = input('Type any number with 3 or more digits: ')
    lst = list(map(int, a))
    result = 0

    for i in lst:
        if i % 2 == 0:
            continue
        result += i**2

    return result


print(func())

# вариант 2
newline()
acc = 0
x = input('Type any num: ')
for k in x:
    if k.isdigit() and int(k) % 2 != 0:
        acc += int(k)**2
print(acc)

#
