import tkinter as tk
from tkinter import ttk

app_name="Restaurants System"
version="Beta"
width, height = 720, 480

  
class tkinterApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) 
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

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="W E L C O M E ")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Add Food Items",
        command = lambda : controller.show_frame(addItem))
 
        button2 = ttk.Button(self, text ="Order Food",
        command = lambda : controller.show_frame(orderFood))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

class addItem(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Add Food Item Into DataBase")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        entry1 = tk.Entry(self) 
        canvas1.create_window(200, 140, window=entry1)
        button1 = ttk.Button(self, text ="<--",
                            command = lambda : controller.show_frame(WelcomePage))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)



class orderFood(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Order Food")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="<--",
                            command = lambda : controller.show_frame(WelcomePage))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

  
app = tkinterApp()
app.title(app_name+f"({version})")
app.geometry(f"{width}x{height}")
app.eval('tk::PlaceWindow . center')
app.minsize(width, height)
app.mainloop()