def total(initial=5, *numbers, **keywords):
    print(numbers)  # (1, 2, 3)
    print(keywords)  # {'vegetables': 50, 'fruits': 100}
    count = initial
    print(count)  # 10
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


# 1, 2, 3 - позиционные аргументы, (*param) - собираются в кортеж
# vegetables, fruits - ключевые аргументы, (**param) - собираются в словарь
print(total(10, 1, 2, 3, vegetables=50, fruits=100))  # 166

#
print()
print()


def newTotal(initial=5, *numbers, extra_number):
    print(f'{numbers} - type(tuple), positions arguments ')
    print(f'{extra_number} - key argument')
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


newTotal(10, 1, 2, 3, extra_number=50)  # 66
newTotal(10, 1, 2, 3)  # error, т.к. нет значения extra_number по умолчанию


#
