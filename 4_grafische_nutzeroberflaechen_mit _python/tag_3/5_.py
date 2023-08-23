from tkinter import Tk, Frame, Label, X, StringVar, IntVar


class Application(Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        self.label = Label(master, text="WBS-Training")
        #  Positionierung in Form von Layouts
        self.label.pack(fill=X, padx=10, pady=15)
        # Positionierung 
        self.age = IntVar()
        # Setter aufrufen 
        self.age.set(31)

        self.name = StringVar()
        self.name.set("Nil Jacob")
        # Getta aufrufen
        print(self.age.get())
        print(self.name.get())


root = Tk()
app = Application(root)
app.mainloop()
