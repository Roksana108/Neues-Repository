from tkinter import Tk, Frame, Label


class Application(Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        
        self.label = Label(master, text="Hierhin",)
        self.label_2 = Label(master, text="")
        
        self.label.grid(row=0, column=0)
        self.label_2.grid(row=1, column=0)
        
        self.label.config(bg="Pink")


root = Tk()
app = Application(root)
app.mainloop()        
    