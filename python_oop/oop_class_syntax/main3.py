class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def square(self):
        return self.a*self.b

    def half_square(self):
        return self.square()/2

    def inc_a(self, i_a):
        self.a += i_a


r = Rectangle(10, 20)
print(dir(r))  # [..., 'a', 'b', 'square']

print(r.square())  # 200

print(r.half_square())  # 100.0

r.inc_a(5)  # увеличит 'a' на 5
print(r.a)  # 15



#
