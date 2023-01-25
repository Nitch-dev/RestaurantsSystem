import sqlite3


def addItemsToDb(food, price):
        con = sqlite3.connect("food.db")
        c = con.cursor()
        c.execute("INSERT INTO EMPLOYEE VALUES('{}','{}')".format(food,price))
        con.commit()   
        con.close()
        