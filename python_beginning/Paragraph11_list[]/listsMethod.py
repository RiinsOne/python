from ogframework import newline

colors = ['red', 'orange', 'green']
colors.extend(['black', 'blue'])  # расширяет список списком
print(colors)  # ['red', 'orange', 'green', 'black', 'blue']

newline()
colors.append('purple')  # добавляет элемент в список
print(colors)  # ['red', 'orange', 'green', 'black', 'blue', 'purple']

newline()
colors.insert(2, '(2) yellow')  # добавляет элемент в указанную позицию
print(colors)  # ['red', 'orange', '(2) yellow', 'green', 'black', 'blue', 'purple']

newline()
colors.remove('black')  # удаляет элемент из списка
print(colors)  # ['red', 'orange', '(2) yellow', 'green', 'blue', 'purple']

newline()
print(colors.count('red'))  # считает количество повторений аргумента метода
print(colors.index('green'))  # возвращает позицию в списке аргумента метода

newline()
col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(col)
print(col.pop())  # удаляет и возвращает последний элемент списка
print(col)  # ['red', 'orange', 'yellow', 'green', 'blue']

newline()
col.reverse()  # список в обратном порядке
print(col)  # ['blue', 'green', 'yellow', 'orange', 'red']

newline()
col.sort()  # сортирует список (сравнение строк)
print(col)  # ['blue', 'green', 'orange', 'red', 'yellow']

newline()
col.clear()  # очищает список. Метод появился в версии 3.3. Аналог del col[:]
print(col)  # []

#
