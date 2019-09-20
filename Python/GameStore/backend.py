import sqlite3


def create_table():
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS game ( id INTEGER PRIMARY KEY , tittle text, company text, type text, year integer )")
    conn.commit()
    conn.close()


create_table()


def insert(tittle, company, type, year):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO game VALUES ( NULL ,?,?,?,?)", (tittle, company, type, year))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()
    # cur.execute("SELECT MAX (id) FROM game;")
    # var = cur.fetchone()
    # var = var[0] + 1
    # print(var)
    # cur.execute("ALTER TABLE game AUTOINCREMENT = id")
    cur.execute("SELECT * FROM game")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM game WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, tittle, company, type, year):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()
    cur.execute("UPDATE game SET tittle=?, company=?, type=?, year=? WHERE id=?", (tittle, company, type, year, id))
    conn.commit()
    conn.close()


def search(tittle="", company="", type="", year=""):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM game WHERE tittle=? OR company=? OR type=? OR year=?", (tittle, company, type, year))
    rows = cur.fetchall()
    conn.close()
    return rows

update(3,'dasd','ads','ads',2222)
print(view())