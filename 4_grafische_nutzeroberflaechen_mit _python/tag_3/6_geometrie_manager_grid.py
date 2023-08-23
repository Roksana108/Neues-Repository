from tkinter import Tk, Frame, Label 


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.label1 = Label(master, text="Hallo Welt 1", bg="Green", fg="Pink")
        self.label2 = Label(master, text="Hallo Welt 2", bg="Blue", fg="White")
        self.label3 = Label(master, text="Hallo Welt 3", bg="Pink", fg="Purple")
        self.label4 = Label(master, text="Hallo Welt 4", bg="Orange", fg="Pink")
        self.label5 = Label(master, text="Hallo Welt 5", bg="Orange", fg="Gold")
        self.label6 = Label(master, text="Hallo Welt 6", bg="White", fg="Black")
    
        self.label1.grid(row=1, column=0, ipadx=10, ipady=10, padx=5, pady=5)
        self.label2.grid(row=1, column=1, ipadx=10, ipady=10, padx=5, pady=5)
        self.label3.grid(row=1, column=2, ipadx=10, ipady=10, padx=5, pady=5)
        self.label4.grid(row=0, column=0, ipadx=10, ipady=10, padx=5, pady=5)
        self.label5.grid(row=0, column=1, ipadx=10, ipady=10, padx=5, pady=5)
        self.label6.grid(row=0, column=2, ipadx=10, ipady=10, padx=5, pady=5)

root = Tk()
app = Application(root)
app.mainloop()
    
        

