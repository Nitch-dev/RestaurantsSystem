import tkinter as tk
from func import validate_name, validate_price
from backend import *
import sqlite3
root = tk
  
class tkinterApp(root.Tk):
     
    def __init__(self, *args, **kwargs):
         
        root.Tk.__init__(self, *args, **kwargs)
        container = root.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 

        for F in (WelcomePage, addItem, orderFood):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(WelcomePage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class WelcomePage(root.Frame):
    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)

        label = root.Label(self, text ="W E L C O M E ")
        label.grid(row=1, column=5, padx=10, pady=10)
  
        button1 = root.Button(self, text ="Add Food Items",
        command = lambda : controller.show_frame(addItem))
 
        button2 = root.Button(self, text ="Order Food",
        command = lambda : controller.show_frame(orderFood))
        button1.grid(row=2, column=2, padx=10, pady=10)

        button2.grid(row=2, column=3, padx=10, pady=10)

class addItem(root.Frame):
     
    def __init__(self, parent, controller):

        root.Frame.__init__(self, parent)

        label = root.Label(self, text ="Add Food Item Into DataBase (Admin)")
        label.grid(row=1, column=2, padx=10, pady=10)

        label = root.Label(self, text="Food name:")
        label.grid(row=2, column=1, padx=10, pady=10)

        foodNameEntry = root.Entry(self) 
        foodNameEntry.grid(row=2, column=2)

        label = root.Label(self, text="Food price:")
        label.grid(row=3, column=1, padx=10, pady=10)

        foodPriceEntry = root.Entry(self)
        foodPriceEntry.grid(row=3, column=2)

        addItemBtn = root.Button(self, text ="Add Item", command=lambda: self.addFood(foodNameEntry.get(), foodPriceEntry.get(), infoLabel))
        addItemBtn.grid(row=4, column=1, padx=10, pady=10)

        infoLabel = root.Label(self, text="")
        infoLabel.grid(row=4, column=2, padx=10, pady=10)

        goBackBtn = root.Button(self, text ="<--", command=lambda:controller.show_frame(WelcomePage))
        goBackBtn.grid(row=1, column=1, padx=10, pady=10)
    
    def addFood(self, name, price, label):
        if not validate_name(name):
            label.config(text="Name length must \n be greater then 2")
        elif not validate_price(price):
            label.config(text="Price value must \n be greater then 0")
        else:
            addItemsToDb(name,price)




class orderFood(root.Frame):
     
    def __init__(self, parent, controller):

        root.Frame.__init__(self, parent)

        label = root.Label(self, text ="Order Food")
        label.grid(row=1, column=5, padx=10, pady = 10)
  
        goBackBtn = root.Button(self, text ="<--", command=lambda:controller.show_frame(WelcomePage))
        goBackBtn.grid(row=1, column=1, padx=10, pady=10)


app = tkinterApp()
app.title("Restaurants System")
app.geometry("720x480")
app.eval('tk::PlaceWindow . center')
app.minsize(720, 480)
app.mainloop()