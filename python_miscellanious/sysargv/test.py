import sys


args = sys.argv[1:]
# print(sum(map(int, args)))

l1 = list()

for arg in args:
    c1 = input('enter first value')
    l1.append(int(c1))

print(sum(l1))