import sqlite3

con = sqlite3.connect("food.db")
c = con.cursor()

#for now value is null
food = None #put your food input name var equal to this
price =  None #put your food input name var equal to this

#adds items to database
def addItemsToDb(food,price):
        c.execute("INSERT INTO food VALUES('{}','{}')".format(food,price))
#show all database
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