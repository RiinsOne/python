# Словарь, dict

# Словарь - неупорядоченная изменяемая коллекция или, "список" с
# произвольными ключами, неизменяемого типа

eng2sp = dict()  # создать пустой словарь
print(eng2sp)  # {}
eng2sp['one'] = 'uno'  # добавляем 'uno' для элемента с индексом 'one'
print(eng2sp)  # {'one': 'uno'}
print(eng2sp['one'])  # uno
eng2sp['two'] = 'dos'
print(eng2sp)  # {'one': 'uno', 'two': 'dos'}
eng2sp['three'] = 'tres'
print(eng2sp)  # {'one': 'uno', 'two': 'dos', 'three': 'tres'}

print()
print()

# В качестве индексов используются неизменяемые строки,
# можно также воспользоваться кортежами, т.к. они неизменяемые:

e = {}
print(e)
e[(4, '6')] = '1'
print(e)  # {(4, '6'): '1'}

# Словари являются неупорядоченной коллекцией.
# Фактически, словарь - это отображение двух множеств: ключей (индексов) и значений

# К словарям применим оператор in:
print()
print()

print(eng2sp)
print('one' in eng2sp)  # True
# поиск по множеству ключей

print()
print()

# Найти частоту встречаемости элементов
# в последовательности(списке, строке, кортеже).


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


lst = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 7]
string = 'kasdklajd19210u212a21'
tpl = (5, 5, 5, 6, 5, 'r', 5)

print(histogram(lst))  # {1: 3, 2: 2, 3: 3, 4: 3, 7: 1}
print(histogram(string))  # {'k': 2, 'a': 3, 's': 1, 'd': 2, 'l': 1, 'j': 1, '1': 4, '9': 1, '2': 4, '0': 1, 'u': 1}
print(histogram(tpl))  # {5: 5, 6: 1, 'r': 1}

#
