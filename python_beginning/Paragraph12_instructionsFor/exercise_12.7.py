s = 'Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог'
lst = s.split()  # сделать список, разделитель по умолчанию пробел
lst2 = []
print(lst)
for i in lst:
    if i[0] == 'м' or i[0] == 'М':
        lst2.append(i[1:])
    else:
        lst2.append(i)
print(lst2)
s2 = str.join(' ', lst2)  # собрать список, пробел как разделитель между элементами
print(s2)


#
