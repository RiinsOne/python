a = []
summ = 0
while True:
    x = input('Type any number or "stop" cancel typing: ')
    if x == 'stop':
        break
    a.append(int(x))
summ = sum(a)
print(summ)



#
