# Importieren von Biblotheken 
from tkinter import Tk, Frame, IntVar
# Klasse erestellen


class Application(Frame):
  
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        # Definition einer Steruerelementvariable
        self.age = IntVar()
        self.age.set(25)
        # Aufruf des Setters
        print(self.age.get())
        self.hight = IntVar()
        # Aufruf des Getters 
        self.hight.set(159)
        print(self.hight.get())


root = Tk()
app = Application(root)
app.mainloop()
