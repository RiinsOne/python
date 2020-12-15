class SomeClass:
    """Some help text"""
    a = 10
    b = 20
    c = []

    def some_func(self):
        print("Hello")


print(str)  # <class 'str'>

print(SomeClass)  # <class '__main__.SomeClass'>
print(SomeClass.a)
print(SomeClass.b)

sc = SomeClass()  # экземпляр класса
print(type(sc))  # <class '__main__.SomeClass'>
print(sc.a)  # 10

sc.b = 45
print(sc.b)  # 45
print(SomeClass.b)  # 20

sc.c.append(34)
print(sc.c)  # [34] если модифицировали объект, то он будет у всех инстансов
print(SomeClass.c)  # [34]

sc.c = [22]
print(sc.c)  # [22] тут мы создали новый объект
print(SomeClass.c)  # [34]

#
