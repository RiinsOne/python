# restore db from sql dump file

import sqlite3 as sq


db_core = "M:\\Programs\\workspace\\python\\python_sqlite\\db_from_dump.sqlite3"
folder = "M:\\Programs\\workspace\\python\\python_sqlite\\"

with sq.connect(db_core) as con:
    cur = con.cursor()

    with open(folder+"sql_damp.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)
