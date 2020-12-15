d = {'a': 1, 'b': 2, 'c': 3}

s = repr(d)  # преобразовать словарь в строку
print(s)  # # '{'a': 1, 'b': 2, 'c': 3}'
# словарь вернется в виде строки

fp = open('dict.txt', 'w')
fp.write(s)
fp.close()

print()

fp = open('dict.txt', 'r')
s1 = fp.read()
print(s1)  # '{'a': 1, 'b': 2, 'c': 3}'
print(type(s1))  # <class 'str'>

d1 = eval(s1)  # обратно в словарь, обратная функция
print(d1)
print(type(d1))  # <class 'dict'>
print(d1['a'])  # 1

print()

print(repr('sdsdsd'))  # ''sdsdsd'', строка в строке


#
