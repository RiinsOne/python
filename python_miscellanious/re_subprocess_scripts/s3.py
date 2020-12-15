import subprocess as sp

sp.call('df -h | grep /dev/sd > 29SEP20.logfile', shell=True)

dev_status = []

with open('29SEP20.logfile', 'r', encoding='utf-8') as lf:
    line = lf.readline()
    # print(line)
    lst_line = line.split(' ')
    dev_status = [el for el in lst_line if el and el != lst_line[-1]]

    # print('----------')

    # lf.seek(0)
    # lines = lf.readlines()
    # print(lines)
    # print(type(lines))
    # lf.close()

print()
print(dev_status)
print()

used_disk_space = int(dev_status[4][0:2])
# print(type(used_disk_space))
print('Used disk space is {}%'.format(used_disk_space))
print()

if used_disk_space >= 80:
    print('Allert!!! Check your disk space!!!')
else:
    print('Everything is fine')
print()
