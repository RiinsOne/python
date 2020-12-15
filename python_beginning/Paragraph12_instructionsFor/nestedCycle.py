from ogframework import newline

outer = [1, 2, 3, 4]  # внешний цикл
inner = [5, 6, 7, 8]  # вложенный (внутренний) цикл

for i in outer:
    for j in inner:
        print(f'i={i}, j={j}')

"""
i=1, j=5
i=1, j=6
i=1, j=7
i=1, j=8
i=2, j=5
i=2, j=6
i=2, j=7
i=2, j=8
i=3, j=5
i=3, j=6
i=3, j=7
i=3, j=8
i=4, j=5
i=4, j=6
i=4, j=7
i=4, j=8
"""

newline()
lst = [[1, 2, 3], [4, 5, 6]]

for i in lst:
    print(i)
# [1, 2, 3]
# [4, 5, 6]

newline()
print()  # следующая строка
for i in lst:  # цикл по элементам внешнего списка
    print()
    for j in i:  # цикл по элементам элементов внешнего списка
        print(j, end='')
# 123
# 456


#
