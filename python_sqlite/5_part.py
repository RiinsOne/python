import sqlite3 as sq
import os


path_to_db = 'C:\\Users\\Orkhan\\Desktop\\workspace_2\\python_sqlite'

with sq.connect(path_to_db + "\\database.sqlite3") as con:
    cur = con.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER,
        score INTEGER,
        time INTEGER
        )
        """
    )
