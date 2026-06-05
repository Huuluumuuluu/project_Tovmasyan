import sqlite3

with sqlite3.connect("rent.db") as con:
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS rent(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        floor INTEGER,
        area REAL,
        conditioner TEXT,
        price REAL
    )
    """)

while True:
    print("""
1 Добавить
2 Показать

3 Поиск по этажу
4 Поиск по площади
5 Поиск по кондиционеру

6 Изменить цену
7 Изменить площадь
8 Изменить кондиционер

9 Удалить по ID
10 Удалить по этажу
11 Удалить по цене

0 Выход
""")

    n = input("Выбор: ")

    with sqlite3.connect("rent.db") as con:
        cur = con.cursor()

        if n == "1":
            cur.execute(
                "INSERT INTO rent(floor,area,conditioner,price) VALUES(?,?,?,?)",
                (
                    int(input("Этаж: ")),
                    float(input("Площадь: ")),
                    input("Кондиционер: "),
                    float(input("Цена: "))
                )
            )

        elif n == "2":
            cur.execute("SELECT * FROM rent")
            print(*cur.fetchall(), sep="\n")

        elif n == "3":
            cur.execute(
                "SELECT * FROM rent WHERE floor=?",
                (int(input("Этаж: ")),)
            )
            print(*cur.fetchall(), sep="\n")

        elif n == "4":
            cur.execute(
                "SELECT * FROM rent WHERE area>=?",
                (float(input("Площадь от: ")),)
            )
            print(*cur.fetchall(), sep="\n")

        elif n == "5":
            cur.execute(
                "SELECT * FROM rent WHERE conditioner=?",
                (input("Да/Нет: "),)
            )
            print(*cur.fetchall(), sep="\n")

        elif n == "6":
            cur.execute(
                "UPDATE rent SET price=? WHERE id=?",
                (float(input("Цена: ")), int(input("ID: ")))
            )

        elif n == "7":
            cur.execute(
                "UPDATE rent SET area=? WHERE id=?",
                (float(input("Площадь: ")), int(input("ID: ")))
            )

        elif n == "8":
            cur.execute(
                "UPDATE rent SET conditioner=? WHERE id=?",
                (input("Да/Нет: "), int(input("ID: ")))
            )

        elif n == "9":
            cur.execute(
                "DELETE FROM rent WHERE id=?",
                (int(input("ID: ")),)
            )

        elif n == "10":
            cur.execute(
                "DELETE FROM rent WHERE floor=?",
                (int(input("Этаж: ")),)
            )

        elif n == "11":
            cur.execute(
                "DELETE FROM rent WHERE price<?",
                (float(input("Цена меньше: ")),)
            )

        elif n == "0":
            break
