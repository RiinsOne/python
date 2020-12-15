import ogframework as og

# pH = float(input('Type pH value: '))
pH = 5.0
if pH == 5.0:
    print(pH, 'Coffee')

if pH == 8.0:
    print(f'{pH} Water')

if pH == 8.0:
    print(f'{pH} Water')
elif 7.36 < pH < 7.44:
    print(f'{pH} Blood')
else:
    print('What is it?')


og.newline()
value = input('Type pH value: ')
if len(value) > 0:
    ph = float(value)
    if ph == 7.0:
        print(f'{ph} Water')
    elif 7.36 < ph < 7.44:
        print(f'{ph} Blood')
    else:
        print('What is it?')
else:
    print('Type pH value again!')


def my_function():
    """
    Не делаем ничего, но документируем.
    Нет, правда, эта функция ничего не делает.
    """
    pass


og.newline()
print(help(my_function))  # вызывем help по имени функции, без скобок


#
