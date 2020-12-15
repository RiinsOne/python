import ogframework as og


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print(outer(4, 5))


def kn(a):
    def inner():        # замыкание не использует аргументов
        return a + 5    # но использует внешний параметр kn()
    return inner        # возвращает имя функции вместо её вызова


og.newline()
print(kn(4))  # <function kn.<locals>.inner at 0x002E9588>

a = kn(4)
print(a)  # <function kn.<locals>.inner at 0x002E9588>

print(a())  # 9, запомнилось значение в момент создания a


#
