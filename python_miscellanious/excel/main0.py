from itertools import islice
from collections import namedtuple


lst = []
# lst2 = []
# InnerBlock = namedtuple('Block', 'agentid, name, password, enable, remarks')
#
#
# class Block(InnerBlock):
#
#     def __str__(self):
#         return '{}\t{}\t{}\t{}\t{}'.format(self.agentid, self.name, self.password, self.enable, self.remarks)


with open(r'C:\OG\workspace\venv_projects\excel\users1.csv', 'r', encoding='utf-8') as f:
    for line in islice(f, 1, None):
        stripped_line = line.strip('\n')
        lst.append(stripped_line.split(','))

for l in lst:
    print(l)

print()

for user_data in lst:
    print('username', user_data[0])
    print('fullname', user_data[1])
    print('password', user_data[2])
    print('is_active', user_data[3])
    print('remarks', user_data[4])
    print('-----')
