# fetchall, fetchmany, fetchone

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
    con.row_factory = sq.Row  # для возвращение значений не в виде кортежей, а в виде словаря ключ+значение
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

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    cur.execute("SELECT model, price FROM cars")
    # rows = cur.fetchall()  # все записи
    # row = cur.fetchone()  # первая запись
    # rows = cur.fetchmany(4)  # первые 4 записи

    # cur итерируемый объект
    # преимущество такого подхода в экономии памяти
    # for result in cur:
    #     print(result)

    for result in cur:
        print(result['model'], result['price'])
