# найти позицию наименьшего элемента
counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
print(counts.index(min(counts)))  # 6
print()

# поиск двух наименьших элементов

# Вариант 1
def find_two_smallest(L):
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)  # удаляем первый элемент

    nextSmallest = min(L)
    min2 = L.index(nextSmallest)
    L.insert(min1, smallest)  # возвращаем первый минимальный обратно
    if min1 <= min2:  # проверяем индекс второго из-за смещения
        min2 += 1

    print(f'First smallest {smallest} has index {min1}, '
          f'second {nextSmallest} has index {min2}')

    return (min1, min2)  # возвращаем кортеж

print(find_two_smallest(counts))
print()


# Вариант 2
def findTwoSmallestWithSorted(L):
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    return (min1, min2)

print(findTwoSmallestWithSorted(counts))
print()


# Вариант 3
def findTwoSmallestWithFor(L):
    if L[0] < L[1]:
        min1, min2 = 0, 1  # устанавливаем начальные значения
    else:
        min1, min2 = 1, 0

    for i in range(2, len(L)):
        if L[i] < L[min1]:  # первый вариант
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:  # второй вариант
            min2 = i
    return (min1, min2)

print(findTwoSmallestWithFor(counts))
print()

#
