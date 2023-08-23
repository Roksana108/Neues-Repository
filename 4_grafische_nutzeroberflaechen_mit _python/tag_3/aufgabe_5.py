from tkinter import Tk, Frame, Label, X, IntVar


class Application(Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        self.label = Label(master, text="Hello Word!")
        self.label.pack(fill=X, padx=30, pady=30)
        self.label1 = Label(master, text="this is the text")
        self.label1.pack(fill=X, padx=30, pady=30)
        self.label3 = Label(master, bg="Blue", text="blue like a sky")
        self.label3.pack(fill=X, padx=20)


root = Tk()
app = Application(root)
app.mainloop()