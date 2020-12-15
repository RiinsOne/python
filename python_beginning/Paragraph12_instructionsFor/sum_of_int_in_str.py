s = 'asd51sf56s11505sdak'
total = 0
for i in range(len(s)):
    if s[i].isalpha():  # посимвольно проверяем наличие буквы
        continue  # инструкция перехода к следующему шагу цикла
    total += int(s[i])  # накапливаем сумму, если встретилась цифра
print(f'The sum of int: {total}.')

# короткая версия
for i in range(len(s)):
    if s[i].isdigit():
        total += int(s[i])
print(total)


#
