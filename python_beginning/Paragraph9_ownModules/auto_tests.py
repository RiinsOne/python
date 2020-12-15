import doctest
# автоматически проверяет тесты в документации


def func_m(v1, v2, v3):
    """
    Вычисляет среднее арифметическое трех чисел.

    >>> func_m (20, 30, 70)
    40.0

    >>> func_m(1, 5, 8)
    4.667
    """
    return round((v1 + v2 + v3) / 3, 3)


doctest.testmod()


print(func_m(20, 30, 70))
print(func_m(1, 5, 8))

#
