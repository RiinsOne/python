import os
import sqlite3 as sq


cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]


db_core = "M:\\Programs\\workspace\\python\\python_sqlite\\database.sqlite3"

with sq.connect(db_core) as con:
    cur = con.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        )
        """
    )

    # execute с помощью коллекции (список из кортежей)
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57127)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Skoda', 9000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Bentley', 350000)")

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # обновить price на 0 всем моделям начинающихся с 'A'
    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})

    # для выполнения несколько SQL комманд
    # нельзя шаблон на запросах
    cur.executescript(
        """
        DELETE FROM cars WHERE model LIKE 'A%';
        UPDATE cars SET price = price + 1000
        """
    )
