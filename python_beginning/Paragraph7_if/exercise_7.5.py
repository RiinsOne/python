import ogframework as og

# 7.5


def city_code():
    code = int(input('Type city code: '))
    time = int(input('Type minutes: '))
    if code == 343:
        print(f'The 343 code city is Ekaterinburg, cost of the {time} minutes are {time * 15} rubles')
    elif code == 381:
        print(f'The 381 code city is Omsk, cost of the {time} minutes are {time * 18} rubles')
    elif code == 473:
        print(f'The 473 code city is Voronezh, cost of the {time} minutes are {time * 13} rubles')
    elif code == 485:
        print(f'The 485 code city is Yaroslavl, cost of the {time} minutes are {time * 11} rubles')
    else:
        print('Not found')


city_code()

#
