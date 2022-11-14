import tkinter as tk
from tkinter import Menu
from subprocess import call


class AdsucApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LOGGED IN")
        self.geometry("963x600+5+5")
        self.configure(bg="gray")
        self.resizable(0, 0)
        self.menuBar = Menu(self)
        self.configure(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.exitt)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="About", command=self.clickabout)
        self.menuBar.add_cascade(label="About", menu=self.helpMenu)

    # ==========Exit Function==========
    def exitt(self):
        self.destroy()

    # ==========Functions to call scripts==========
    def clickabout(self):
        call(["python", "About.py"])


if __name__ == "__main__":
   adapp = AdsucApp()
   adapp.mainloop()
