fp = open('descriptor.txt', 'w')  # режим w будет создавать файл
fp.write('some data')
fp.flush()  # записывает данные в файл и освобождает буффер
fp.seek(0)
fp.write('event_more_view data xxx')  # запись идет поверх
fp.flush()
fp.close()

fp2 = open('descriptor.txt', 'w')
fp2.write('some data yyy ddd')
# данные все сотрутся
fp2.close()

fp3 = open('descriptor.txt', 'a')  # режим для записи, не стирает файл
print(fp3.tell())  # 17 - курсор уже будет в конце
fp3.write('total_handicap data')
print(fp3.tell())  # 26
fp3.flush()
fp3.close()

print()

# 'r+' - не создаст файл, но может и писать и читать
# 'a+' - создает файл, можно читать и писать

fp4 = open('descriptor2.txt', 'a+')
fp4.write('event_more_view data')
fp4.write('event_more_view data')
fp4.write('event_more_view data')  # курсор будет в конце
fp4.flush()
fp4.seek(5)
print(fp4.read())  # atanew datanew data
fp4.close()

fp5 = open('descriptor2.txt', 'w')
fp5.close()

#
