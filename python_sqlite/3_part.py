import sqlite3 as sq
import os


path_to_db = 'C:\\Users\\Orkhan\\Desktop\\workspace_2\\python_sqlite'

with sq.connect(path_to_db + "\\database.sqlite3") as con:
    cur = con.cursor()

    cur.execute(
        """
        SELECT * FROM users
        WHERE score > 100
        ORDER BY score DESC
        LIMIT 2, 5
        """
    )
    # result = cur.fetchall()
    # print(result)
    # [('Юля', 2, 23, 700), ('Николай', 1, 22, 500), ('Елена', 2, 17, 500), ('Мария', 2, 18, 400), ('Федор', 1, 32, 200)]

    # for result in cur:
    #     print(result)
    # либо перебрать через итерируемый объет cur

    result1 = cur.fetchone()  # первнет первую запись
    result2 = cur.fetchmany(2) # вернет вторую и третью запись, т.к. курсор сдвинулся на один при result1
    print(result1)
    print(result2)
