a = []
n = int(input('Type number of elements: '))
for i in range(n):
    new_element = int(input('Type element: '))
    a.append(new_element)
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)


# решение этой задачи в одну строку:
A = [int(input()) for i in range(int(input()))]
print(A)

#
