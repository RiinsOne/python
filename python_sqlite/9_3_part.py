import sqlite3 as sq


db_core = "M:\\Programs\\workspace\\python\\python_sqlite\\database.sqlite3"

with sq.connect(db_core) as con:
    cur = con.cursor()

    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust(
            name TEXT,
            tr_in INTEGER,
            buy INTEGER
        );
        """
    )

    cur.execute("INSERT INTO cars VALUES(NULL, 'Zaporoshec', 1000)")
    last_row_id = cur.lastrowid  # последняя запись в cur

    buy_car_id = 2
    cur.execute("INSERT INTO cust VALUES('Fedor', ?, ?)", (last_row_id, buy_car_id))
