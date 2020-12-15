from itertools import islice

xf = 'xmlfile.XML'


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


lst = list()

with open(xf) as xmlFile:
    lines = islice(xmlFile, 6, 7)
    for line in lines:
        line = line.strip()
        lst.append(line)
        print(line)
        print(len(line))

print(lst)

print()

num_lines = sum(1 for line in open(xf))
print(num_lines)


with open(xf) as file:
    data = file.readlines()
    index = data.index('<Airline Host="152" SubHost="T5">\n')

print(index)




