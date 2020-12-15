class Multyplier:

    def __init__(self, factor=2):
        self.factor = factor

    def __call__(self, *args):
        res = []
        for item in args:
            res.append(item * self.factor)
        return res


mul_by_27 = Multyplier(27)
result = mul_by_27(1, 2, 3, 4)
print(result)

print('-----')

multipliers = []
for factor in (2, 3, 4, 5):
    mul = Multyplier(factor)
    multipliers.append(mul)
print(multipliers)  # [<__main__.Multyplier object at 0x00C7A160>, <__main__.Multyplier object at 0x00C7A238>, <__main__.Multyplier object at 0x00C7A2B0>, <__main__.Multyplier object at 0x00C7A2E0>]

for mul in multipliers:
    print(mul(10, 20, 30))
# [20, 40, 60]
# [30, 60, 90]
# [40, 80, 120]
# [50, 100, 150]
