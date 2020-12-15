# если файла нет, то создаст.
# если файл есть, то будет перезаписан
with open('top.txt', 'w') as output_file:
    output_file.write('Hello!\n')
    # метод write() возвращает число записанных символов

# для добавления строки в файл необходимо открыть файл в режиме 'a' (append)
with open('top.txt', 'a') as output_file:
    output_file.write('Append some text\n')

#
