import csv

fp = open('person.csv', 'w', newline='')
# newline='' - нужно, чтобы не было пустых строк

csv_w = csv.writer(fp)

csv_w.writerow(['Name', 'Surname', 'Age'])
# fp.flush()

csv_w.writerow(['Ivan', 'Ivanov', '25'])
# fp.flush()

fp.close()


fp = open('person.csv', 'r')

csv_r = csv.reader(fp)
for i in csv_r:
    print(i)


#
