import subprocess as sp

with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    # print(lines[1])
    # print(type(lines[1]))
    lst = lines[1].split(' ')
    for el in lst:
        if el == '' or el == '\t' or el == '\n' or el == ' ':
            lst.remove(el)
    # print(lst)
    # print('----------')
    
    lst2 = [el for el in lst if el]
    print(lst2[:-1])

    with open('text1.txt', 'w', encoding='utf-8') as f1:
        f1.write(str(lst2[:-1]))
        f1.write('\n')

    # sp.run('{lst} > file1.txt'.format(lst=lst), shell=True)
    # for line in lines[1]:
        # arr.append(line.strip().split('\t'))
        # print(line.strip())
    # print(arr)

