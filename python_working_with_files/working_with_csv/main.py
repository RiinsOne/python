fp = open('total_handicap.txt', 'w')
fp.write('Hello world!!!')
fp.close()

print()

fp2 = open('total_handicap.txt', 'r')
print(fp2.tell())  # 0 - позиция курсора
s = fp2.read()
print(s)  # Hello world!!!
print(fp2.tell())  # где сейчас находится курсор, на 14 символе
s1 = fp2.read()
print(s1)  # '' - ничего уже не прочитает, пусто
fp2.close()

print()

fp3 = open('total_handicap.txt', 'r+')  # читать и писать файл
print(fp3.tell())  # 0
print(fp3.read())  # Hello world!!!
print(fp3.tell())  # 14
fp3.write('New data')
fp3.close()

print()

fp4 = open('total_handicap.txt', 'r+')  # открывает сессию работы с файлом
fp4.seek(14)  # поставить курсор на 14 позицию
print(fp4.read())  # New data
fp4.close()



#
