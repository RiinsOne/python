try:
    x = 'sss'
    # x = int(input('type something: '))
    print(x % 2 == 0)
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')

#
