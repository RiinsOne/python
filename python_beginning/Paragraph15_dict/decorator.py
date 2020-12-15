def doc_it(func):
    def new_func(*args, **kwargs):
        print('Имя функции: ', func.__name__)
        print('Позиционные аргументы: ', args)
        print('Ключевые аргументы: ', kwargs)
        result = func(*args, **kwargs)
        print('Результат: ', result)
        return result  # либо return func(*args, **kwargs)

    return new_func  # возвращаем новую функцию без аргументов


def add_ints(*args, **kwargs):
    count = 0
    for i in args:
        count += i
    for j in kwargs:
        count += kwargs[j]
    return count


print(add_ints(3, 6))

# ручное присваивание декоратора:
print()
new_add_ints = doc_it(add_ints)
# присваиваем new_add_ints функцию doc_it с аргументом функции add_ints без аргументов


new_add_ints(4, 10, test=5)
print('----------')
new_add_ints(21, 31)  # можно и без ключевых аргументов


#
print()


def sumFunc(a, b):
    return a + b


newSumFc = doc_it(sumFunc)
newSumFc(11, 22)

print()


@doc_it  # ещё вариант написания декорирования
def abFc(a, b):
    return a + b


abFc(5, 5)


#
