import sys
from random import random
from random import randint


def generate_range(dot='.'):
    s1 = ''
    for k in range(1, 5):
        for i in range(randint(1, 3)):
            s1 += str(random())[2]
        s1 += dot
    return s1[:-1]


# print(generate_range(3, '.'))


def generate_text_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(10 ** 4):
            f.writelines(generate_range() + '\n')


generate_text_file('ip_list_2.txt')
