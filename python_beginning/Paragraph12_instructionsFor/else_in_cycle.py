for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n}, равно {x} * {n//x}')
            break
    else:
        # циклу не удалось найти множитель
        print(f'{n} - просто число')

#
