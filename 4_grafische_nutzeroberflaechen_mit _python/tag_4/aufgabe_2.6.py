from tkinter import Tk, Frame, Label, Button


class Application(Frame):
    def __init__(self, master=None) -> None:
        Frame .__init__(self, master)
        self.label1 = Label(master, text="H.H Karmapa", bg="Pink", fg="Green")
        self.label2 = Label(master, text="Mahakala", bg="Gold", fg="Green")
        self.label3 = Label(master, text="Dharama", bg="White", fg="Green")

        self.button = Button(master, text="Press Refuge", command=self.action)

        self.label1.grid(column=0, row=0)
        self.label2.grid(column=1, row=0)
        self.label3.grid(column=2, row=0)

        self.button.grid(column=3, row=0)

    def action(self) -> None:
        self.label1.config(text="Manjushri", bg="Yellow")
        self.label2.config(text="Chenrezig", bg="Beige")
        self.label3.config(text="Green Tara", bg="Green")


root = Tk()
app = Application(root)
app.mainloop() 



