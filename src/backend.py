import sqlite3

database = "src/database.db"


def createDatabase():
    try:
        con = sqlite3.connect(database)
        c = con.cursor()
        c.execute(
            """CREATE TABLE if not Exists Foods
                        (name TEXT, price INTEGER)"""
        )
        con.commit()
        con.close()

    except Exception as e:
        print(e)
        print("Could not create database or table")


def addItemsToDb(food, price):
    con = sqlite3.connect(database)
    c = con.cursor()
    c.execute("INSERT INTO Foods VALUES('{}','{}')".format(food, price))
    con.commit()
    con.close()


def showMenu():
    con = sqlite3.connect(database)
    c = con.cursor()
    c.execute("SELECT * FROM Foods")
    menu = tuple(c.fetchall())
    con.commit()
    con.close()
    return menu
