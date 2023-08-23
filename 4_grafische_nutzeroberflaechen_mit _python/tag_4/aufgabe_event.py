from tkinter import Tk, Frame, Label, Menu


class Application(Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.label = Label(master, text="Test",)
        self.label.grid(row=0, column=0)
        self.label.bind("<Control-Enter>", self.on_enter)
    
    def on_enter(self, event) -> None:   
        print("Enter")
 
       
root = Tk()
app = Application(root)
app.mainloop()
