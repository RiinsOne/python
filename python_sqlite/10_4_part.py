# iterdump() - экземпляр класса con
# формирование SQL запросов для формирования таблиц указанной базы данных

import sqlite3 as sq


db_core = "M:\\Programs\\workspace\\python\\python_sqlite\\database.sqlite3"
folder = "M:\\Programs\\workspace\\python\\python_sqlite\\"

with sq.connect(db_core) as con:
    cur = con.cursor()

    # for sql in con.iterdump():
    #     print(sql)

    with open(folder+"sql_damp.sql", "w") as f:
        for sql in con.iterdump():
            f.write(sql)
