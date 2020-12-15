from ogframework import newline

list3 = ['str1', 'element2', 55, -150, 'lastChar']


def func(a):

    def iter_func(items, acc):

        if items:  # items != [] - длинный вариант
            print(items[acc])

            del items[acc]

            return iter_func(items, acc)

    return iter_func(a, 0)


func(list3)
print(list3)


# Аналог цикла for, через итеративную рекурсию
L = ['str1', 'element2', 55, -150, 'lastChar']


def fc(a):
    def iter_func(items, acc):
        if len(items) > acc:
            print(items[acc])
            return iter_func(items, acc + 1)
    return iter_func(a, 0)


newline()
fc(L)
print(L)


newline()
newList = list(range(1, 20, 3))
fc(newList)
print(newList)


#
