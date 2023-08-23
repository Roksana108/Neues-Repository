from tkinter import Tk, Frame, Entry, Button


class Application(Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        self.entry1 = Entry(master, bg="Pink", fg="Yellow", font=("arial", 40))
        self.entry2 = Entry(master, bg="Blue", fg="Red", font=("arial", 40))
        
        self.entry1.grid(column=0, row=0, ipadx=50, ipady=30)
        self.entry2.grid(column=0, row=1, ipadx=50, ipady=30)
        
    def action(self) -> None:
        self.lable.config(text="H.H Karmapa")  # wird nicht angezeigt
        
        
root = Tk()
app = Application(root)
app.mainloop()           