class Bread:

    def __str__(self):
        return 'I\'m bread'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sausage:

    def __str__(self):
        return 'I\'m sausage'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sandwich:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'I\'m bread. Contains with ' + str(self.part1) + ' and ' + str(self.part2)


borodinsky = Bread()
salami = Sausage()
result = borodinsky + salami
print(result)

print('-----')


def func(*args, **kwargs):
    print(args, kwargs)


print(func)
func(a=2, b=2)  # args - (), kwargs - {'a': 2, 'b': 2}
func(3, '55' ,a=2, b=2)  # (3, '55') {'a': 2, 'b': 2}

print('-----')


class MyFuction:

    def __call__(self, *args, **kwargs):
        print(args, kwargs)


func2 = MyFuction()
print(func)
func(34, a=2, b=2)  # (34,) {'a': 2, 'b': 2}
