import sqlite3 as sq


db_core = "M:\\Programs\\workspace\\python\\python_sqlite\\database.sqlite3"

con = None

try:
    con = sq.connect(db_core)
    cur = con.cursor()

    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        BEGIN;
        INSERT INTO cars VALUES(NULL, 'Audi', 52642);
        INSERT INTO cars VALUES(NULL, 'Mercedes', 57127);
        INSERT INTO cars VALUES(NULL, 'Skoda', 9000);
        INSERT INTO cars VALUES(NULL, 'Volvo', 29000);
        INSERT INTO cars VALUES(NULL, 'Bentley', 350000);
        UPDATE cars SET price = price + 1000
        """
    )

    con.commit()

except sq.Error as e:
    # если будет ошибка, то rollback() откатит к BEGIN
    if con: con.rollback()
    print("Error with executing query")
finally:
    if con: con.close()
