class Rectangle:
    a = 10
    b = 20

    def __init__(self):
        print('In init!')


r = Rectangle()  # In init! будет вызываться каждый раз при инициализации класса
print(r.a)
print(r.b)

Rectangle.a = 33
print(r.a)  # 33
r.a = 11
print(r.a)  # 11

print(r)  # <__main__.Rectangle object at 0x001EFDD0>
print(type(r))  # <class '__main__.Rectangle'>
print()


class Rectangle2:
    def __init__(self):
        print(self)
        print(type(self))


r2 = Rectangle2()
# <__main__.Rectangle2 object at 0x0039F950>
# <class '__main__.Rectangle2'>

print()


class Rectangle3:
    a = 10
    b = 20

    def __init__(self):
        self.a = 11
        self.b = 21


r3 = Rectangle3()
print(r3.a)  # 11
print(r3.b)  # 21

print(Rectangle3.a)  # 10
print(Rectangle3.b)  # 20

# r4 = Rectangle3(50)
# TypeError: __init__() takes 1 positional argument but 2 were given

print()


class Rectangle4:
    a = 10
    b = 20

    def __init__(self, c):
        print(c)
        self.a = 11
        self.b = 21


r44 = Rectangle4(55)  # 55 будет вызов при инициализации
print()


class Rectangle5:
    a = 10
    b = 20

    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b


r5 = Rectangle5(72)
print(r5.a)  # 72
print(r5.b)  # 72

r5 = Rectangle5(124, 87)
print(r5.a)  # 124
print(r5.b)  # 87


#
