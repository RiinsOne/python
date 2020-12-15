from ogframework import newline
import sys
import mm


def f():
    return 4


print(sys.path)  # путь к модулям

newline()
print(mm.f())

import mtest
import mtest
import imp
imp.reload(mtest)

newline()

# import mypr  # импорт модуля приводит к выполнению программы

import prog3

#
