s = 'This is a total_handicap string from Andrew'
print(sorted(s.split()))
# ['Andrew', 'This', 'a', 'from', 'is', 'string', 'total_handicap']

print(str.lower('a'))  # a
print(str.lower('Andrew'))  # andrew

print(sorted(s.split(), key=str.lower))
# ['a', 'Andrew', 'from', 'is', 'string', 'total_handicap', 'This']
# Сортировка с предварительным применением к каждому элементу списка
# строкового метода lower().

print()

d = {'t1': 2, 't6': 5, 't9': 1}
print(d)
print(sorted(d))  # ['t1', 't6', 't9']
print(d.get('t1'))  # 2
print(sorted(d, key=d.get))

#
