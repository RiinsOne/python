import ogframework as og


def summ(num):
    str_num = str(num)

    i = 0
    result = 0
    for i in range(len(str_num)):
        result = result + int(str_num[i])
        i += 1

    return result


print(summ(555))


def summ1(num):
    str_num = str(num)

    i = 0
    result = 0
    while i < len(str_num):
        result = result + int(str_num[i])
        i += 1

    return result


print(summ1(5555))


def summ2(num):
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    return result


print(summ2(555))


#
