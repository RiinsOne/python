fp = open('descriptor2.txt', 'a+')

fp.write('total_handicap data and some data')
fp.write('\n')
fp.write('event_more_view data from event_more_view line')
fp.write('\n')
fp.write('sometext\ttabhere')

fp.seek(0)
print(fp.read())
# total_handicap data and some data
# event_more_view data from event_more_view line
# sometext	tabhere

print()

fp.seek(0)
print(fp.readline())  # total_handicap data and some data
print(fp.readline())  # event_more_view data from event_more_view line
print(fp.readline())  # sometext	tabhere

fp.seek(0)
print()
print(fp.readlines())  # строки прочитает в список
# ['total_handicap data and some data\n', 'event_more_view data from event_more_view line\n', 'sometext\ttabhere']

fp.write('\n')
print()

l = ['one\n', 'two\n', 'three\n']
fp.writelines(l)

fp.close()


lst = ['total_handicap data and some data\n', 'event_more_view data from event_more_view line\n', 'sometext\ttabhere']
for i in lst:
    i = i.strip()  # удаляет пустые строки
    print(i)

#
