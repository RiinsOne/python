class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def square(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        self.a = self.b = a


# for i in dir(Square):
#    print(i)

s = Square(20)
print(s.square())  # 400


class A:
    a = 1
    b = 1


class B:
    a = 2
    b = 2


class C(A, B):
    b = 3


c = C()
print(c.a)  # 1
print(c.b)  # 3




#
