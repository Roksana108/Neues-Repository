from tkinter import Tk, Frame, IntVar


class Application(Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        # Definition einer Steruerelementvariable
        self.age = IntVar()
        # Aufruf des Setters
        self.age.set(20)
        # Aufruf des Getters 
        print(self.age.get())


root = Tk()
app = Application(root)
app.mainloop()