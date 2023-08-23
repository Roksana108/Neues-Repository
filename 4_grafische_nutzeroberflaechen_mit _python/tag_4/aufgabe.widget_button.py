from tkinter import Tk, Frame, Label, Button 


class Applictaion (Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        # Definition der Widgets
        self.label = Label(master, text="WBS-Traning")
        # Referenz auf Methodenobject action 
        self.button = Button(master, text="Click", command=self.action)
        # Positionierung der Widgets 
        self.label.grid(column=0, row=0)
        self.button.grid(column=1, row=0)
      
    def action(self) -> None:
        self.label.config(text="Python")    


root = Tk()
app = Applictaion(root)
app.mainloop()        