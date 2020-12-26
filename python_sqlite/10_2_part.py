# write BLOB to database

import sqlite3 as sq


db_core = "M:\\Programs\\workspace\\python\\python_sqlite\\database.sqlite3"
ava_folder = "M:\\Programs\\workspace\\python\\python_sqlite\\avas\\"


def read_ava(n):
    try:
        with open(ava_folder+f"{n}.jpg", "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


with sq.connect(db_core) as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            ava BLOB,
            score INTEGER
        )
        """
    )

    img = read_ava(1)
    if img:
        binary = sq.Binary(img)
        cur.execute("INSERT INTO users VALUES('Nikolay', ?, 1000)", (binary,))
