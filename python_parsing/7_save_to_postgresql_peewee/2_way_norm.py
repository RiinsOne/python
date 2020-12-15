import csv
from peewee import *


db = PostgresqlDatabase(database='test', user='postgres', password='Black79128', host='localhost')


class Coin(Model):
    name = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db


def main():

    db.connect()
    db.create_tables([Coin])

    with open('cmc.csv') as f:
        order = ['name', 'url', 'price']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        with db.atomic():
            for row in coins:
                Coin.create(**row)


if __name__ == '__main__':
    main()

