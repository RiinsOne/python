import sys
import os
import glob
import shutil  # набор shell утилит
from datetime import datetime
import json
import sqlite3


print(dir(sys))

# for i in dir(sys): print(i)

print(sys.argv)
print(sys.path)  # системные пути питона

print()

print(dir(os))
print(os.getcwd())  # M:\Programs\workspace\programming\python\someFunctions\stdlibs

# os.mkdir('new_dir')  # создат папку new_dir в этом пути
print(os.path)
print(os.path.join('/home/', 'new_dir'))  # /home/new_dir, покажет будущий путь

print()
print(glob.glob('*'))
# ['main1.py', 'new_dir'], список файлов текущей директории
# или относительно другой директории

print(dir(shutil))

print()

d = datetime.now()
print(d)  # 2019-05-26 21:01:57.642860
print(d.date())  # 2019-05-26

print()

str1 = json.dumps({'a': 45, 'f': 87})  # из объекта создают строку
print(str1)  # {"a": 45, "f": 87}

print(json.loads(str1))  # {'a': 45, 'f': 87}
# получить обрато объект


print()



#
