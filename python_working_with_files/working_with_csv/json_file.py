import json

d = {'a': 1, 'b': [1, 2, 3], 'c': 3}
d1 = json.dumps(d)  # преобразует в строку
print(d1)  # '{"a": 1, "b": [1, 2, 3], "c": 3}'
print(type(d1))  # <class 'str'>

fp = open('example.json', 'w')
fp.write(d1)
fp.close()

print()

fp = open('example.json', 'r')
s = fp.read()
# print(s)
d2 = json.loads(s)  # преобразует в словарь
print(d2)  # {'a': 1, 'b': [1, 2, 3], 'c': 3}
print(type(d2))  # <class 'dict'>
fp.close()

fp = open('example.json', 'w')
json.dump(d, fp)
# принимает переменную d и указатель file pointer куда указать
fp.close()

print()

fp = open('example.json', 'r')
d5 = json.load(fp)  # {'a': 1, 'b': [1, 2, 3], 'c': 3}
# передаем файл поинтер
print(d5)
fp.close()


#
