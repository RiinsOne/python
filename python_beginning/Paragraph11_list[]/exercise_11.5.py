def func():
    str1 = input('Type first string: ')
    str2 = input('Type second string: ')

    if str1.isdigit() and str2.isdigit():
        summ = int(str1) + int(str2)
        lst = [int(str1), summ, int(str2)]
        # list3 = [int(str1)]
        # list3.append(summ)
        # list3.append(int(str2))

    else:
        lst = [str1, str1 + str2, str2]

    print(lst)


func()

#
