import csv


def write_csv(data):
    with open('names.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (data['name'], data['surname'], data['age'])
        )


def write_csv2(data):
    with open('names2.csv', 'a', newline='') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)


def main():
    d = {'name': 'Petr', 'surname': 'Ivanov', 'age': 21}
    d1 = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 18}
    d2 = {'name': 'Ksu', 'surname': 'Petrova', 'age': 32}

    lst = [d, d1, d2]

    for i in lst:
        # write_csv(i)
        write_csv2(i)


if __name__ == '__main__':
    main()
