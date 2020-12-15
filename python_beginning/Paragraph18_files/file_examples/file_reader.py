import os

file = open('example_text.txt', 'r')  # 'r' - режим чтения (он же по умолчанию)
contents = file.read()  # прочесть содержимое файла в строку и поместить в переменную
print(contents)
file.close()  # освободить занятые файлом ресурсы

print()

# Ошибка при открытии файла
try:
    f = open('1example_text.txt')  # открытие на чтение
except:
    print('Error opening file')
else:
    f.close()
    print('Очистка: закрытие файла')

print()

# With - не требует ручного освобождения ресурсов
try:
    with open('1example_text.txt', 'r') as file:
        contents = file.read()
    print(contents)
except:
    print("Error opening file")

print()

print(os.getcwd())  # M:\Programs\workspace\programming\python\python_beginning\Paragraph18_files\file_examples

# Если файл находится в другом каталоге, то необходимо указать путь к нему:
# 1. Абсолютный путь (начиная с корневого каталога): 'C:\\Users\\Dmitriy\\data1.txt'
# 2. Относительный путь (относительно текущего рабочего каталога): 'data\\data1.txt'

#
print()

with open('example_text.txt', 'r') as file:
    contents = file.read()
print(contents)
# First line of text
# Second line of text
# Third line of text

print()

with open('example_text.txt', 'r') as file:
    contents = file.read(10)  # указываем кол-во символов для чтения
    # курсор перемещается на 11 символ
    rest = file.read()  # читаем с 11 символа
print(f'10: {contents}')
print(f'rest: {rest}')
# 10: First line
# rest:  of text
# Second line of text
# Third line of text

# readlines() - список из строк

with open('example_text.txt', 'r') as file:
    lines = file.readlines()
print(lines)  # ['First line of text\n', 'Second line of text\n', 'Third line of text']

print()
print('---------------------------')
print()

with open('plan.txt') as file:
    planets = file.readlines()
print(planets)  # ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune']
print()

for planet in reversed(planets):
    # print(planet.strip('\n'))
    print(planet.strip())  # возвращает копию строки, из которой удален символ '\n'
# Neptune
# Uranus
# Saturn
# Jupiter
# Mars
# Earth
# Venus
# Mercury

print()
print('---------------------------')
print()

with open('plan.txt') as file:
    for line in file:
        print(line.strip())
        print(len(line.strip()))


#
