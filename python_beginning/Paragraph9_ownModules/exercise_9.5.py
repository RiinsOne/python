import doctest


def func_x4(x):
    """
    >>> func_x4(4)
    272

    >>> func_x4(2)
    24

    >>> func_x4(3.14)
    109.772

    >>> func_x4(12)
    20784
    """
    return round((x ** 4) + (4 * x), 3)


doctest.testmod()

print(func_x4(4))
print(func_x4(2))
print(func_x4(3.14))
print(func_x4(12))

#
