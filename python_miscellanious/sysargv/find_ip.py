import sys


args = sys.argv[1:]
ip_name = str(args[0])
filename = str(args[1])

total = 0

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        if ip_name in line:
            print(line.strip())
            total += 1

print('Total matches: ', total)
