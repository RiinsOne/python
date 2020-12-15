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

        for row in coins:
            # плохой способ, очень сильно грузит жесткий диск
            coin = Coin(name=row['name'], url=row['url'], price=row['price'])
            coin.save()


if __name__ == '__main__':
    main()

