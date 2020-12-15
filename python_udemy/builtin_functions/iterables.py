class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # next(my_object)
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


print(sum(FirstHundredGenerator()))  # 4950


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()


# print(sum(FirstHundredIterable()))  # 4950

# for i in FirstHundredIterable():
#     print(i)


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


print(len(AnotherIterable()))  # 2
a = AnotherIterable()
print(a[1])  # Focus

for car in AnotherIterable():
    print(car)


my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])
print(my_numbers)  # [1, 2, 3, 4, 5]
print(my_numbers_gen)  # это не кортеж, это <generator object <genexpr> at 0x01259F70>
print(type(my_numbers_gen))  # <class 'generator'>

print(next(my_numbers_gen))  # 1


