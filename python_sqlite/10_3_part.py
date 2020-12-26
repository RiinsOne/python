# read and write BLOB to file

import sqlite3 as sq


db_core = "M:\\Programs\\workspace\\python\\python_sqlite\\database.sqlite3"
ava_folder = "M:\\Programs\\workspace\\python\\python_sqlite\\avas\\"


def write_ava(name, data):
    try:
        with open(ava_folder + name, "wb") as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False

    return True


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

    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']
    write_ava("out.jpg", img)
