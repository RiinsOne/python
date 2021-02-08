a = 1
b = 1
b  # 1
# один объект и две переменные
id(a)  # 140722586680384
id(b)  # 140722586680384

# если поменяем a, то b не изменится
a = 2
a  # 2
b  # 1
# id(a) также изменится
del(a, b)  # удалить переменные

#

a = []
b = a
a.append('xxx')
b  # 'xxx'
# мы взяли тот объект на которые ссылаются обе переменные и изменили содержание этого объекта
# мы не создавали новый объект, а изменили старого

def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
    return inner

o = one()
o  # <function __main__.one.<locals>.inner()>
o()
# ['one', 'two']
# 2205187331080
o.__closure__  # (<cell at 0x000002668AB9DE58: list object at 0x000002668AB53C48>,)

o.__closure__[0].cell_contents  # ['one', 'two']
a = o.__closure__[0].cell_contents
print(id(a))  # 1967621231624

a.append('xxx')
o()  # ['one', 'two', 'xxx']
