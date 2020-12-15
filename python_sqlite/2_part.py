import sqlite3 as sq
import os


current_dir = os.getcwd() + "\\python_sqlite"
path_to_db = 'C:\\Users\\Orkhan\\Desktop\\workspace_2\\python_sqlite'

# con = sq.connect(current_dir + "\\database.sqlite3")
# # возвращает экземпляр класса курсор
# cur = con.cursor() #Cursor
# # использовать в такой конструкции не самый лучший вариант, большой шанс ошибиться и получить ошибку
# # лучше использовать контекст менеджер
# cur.execute(
#     """
#
#     """
# )
# con.close()


with sq.connect(current_dir + "\\database.sqlite3") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )
        """
    )
