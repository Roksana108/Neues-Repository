from tkinter import Tk, Frame, Label, Button, Entry


class Applictaion(Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        self.my_input = Entry(
            master, 
            bg="PINK",
            fg="WHITE",
            insertbackground="RED"
        )
        
        self.my_input.grid(row=0, column=0, ipadx=10, ipady=10)

root = Tk()
app = Applictaion(root)
app.mainloop()        