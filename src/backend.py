import sqlite3

con = sqlite3.connect("food.db")
c = con.cursor()

food = input("Food > ")
price = input("price > ")


def addItemsToDb(food,price):
        c.execute("INSERT INTO food VALUES('{}','{}')".format(food,price))

def showTable():
        c.execute("SELECT * FROM food")
        print(c.fetchall())
def deleteFood():
        c.execute("DELETE FROM food WHERE price = '$100' ")

def main():
        addItemsToDb(food,price)
        showTable()
        con.commit()   
        con.close()

main()