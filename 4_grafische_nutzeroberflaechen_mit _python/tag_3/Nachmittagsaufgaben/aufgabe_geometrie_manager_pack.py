from tkinter import Tk, Frame, Label


# Klasse estellen
class Application(Frame):
    # Konstrutkor
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.label1 = Label(master, text="H.H Karmapa 1", bg="Green", fg="Pink")
        self.label2 = Label(master, text="Mahakala 2", bg="Blue", fg="Silver")
        self.label3 = Label(master, text="Dharma 3", bg="Pink", fg="Purple")
        
        self.label1.grid(row=1, column=0, ipadx=20, ipady=20, padx=5, pady=5)
        self.label2.grid(row=1, column=1, ipadx=20, ipady=20, padx=5, pady=5)
        self.label3.grid(row=1, column=2, ipadx=20, ipady=20, padx=5, pady=5)


root = Tk()
app = Application(root)
app.mainloop()