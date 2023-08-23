from tkinter import Tk, Frame, Label, Button, Menu


class Application(Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        # Defnition der Menubar und Zuordnung zu den Fenster als Master 
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        # Definition des Obejcts file_menu und Zuordnung zu menubar als menu...
        self.file_menu = Menu(self.menubar)
        self.file_menu.add_command(label="Neu")
        # Commmnds 
        # Einordnung des Objeckts filter_menu in die menu_bar 
        self.menubar.add_cascade(label="Datei", menu=self.file_menu)


root = Tk()
app = Application(root)
app.mainloop()