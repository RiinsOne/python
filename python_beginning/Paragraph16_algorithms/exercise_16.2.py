from random import randint

lst = [randint(-100, 100) for i in range(1, 1001)]
print('list', lst)

# Вариант 1
def diffCountsMinMaxElements(a):
    counts = 0
    minIndexRange = a.index(min(a))
    print('min index - ', minIndexRange)
    maxIndexRange = a.index(max(a))
    print('max index - ', maxIndexRange)

    if minIndexRange < maxIndexRange:
        for i in a[minIndexRange+1:maxIndexRange]:
            if i < 0:
                counts += 1
    else:
        for i in a[maxIndexRange+1:minIndexRange]:
            if i < 0:
                counts += 1

    return counts


print('Counts of minus elements between - ', diffCountsMinMaxElements(lst))
print()

# Вариант 2, только для разницы, не учитывая отрицательные элементы
def fc(a):
    minIndex = a.index(min(a))
    maxIndex = a.index(max(a))
    if minIndex > maxIndex:
        return minIndex - (maxIndex + 1)
    else:
        return maxIndex - (minIndex + 1)


print(fc(lst))


