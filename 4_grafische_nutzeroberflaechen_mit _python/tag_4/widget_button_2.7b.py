from tkinter import Tk, Frame, Entry, Button


class Application(Frame):
    def __init__(self, master=None) -> None:
        Frame.__init__(self, master)
        
        self.list_counter = 4
        self.list_entries = []
        row_counter = 0
        
        for _ in range(self.list_counter):
            self.list_entries.append(Entry(master, bg="Blue", fg="Pink", insertbackground="Blue"))        
            print("Press Refuge")
        
        for _ in range(self.list_counter):
            self.list_entries[row_counter].grid(row=row_counter, column=1, ipadx=10, ipady=10)
            row_counter += 1   
            
            
root = Tk()
app = Application(root)
app.mainloop()