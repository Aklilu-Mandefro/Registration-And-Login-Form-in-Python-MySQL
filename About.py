import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


class AboutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ABOUT")
        self.geometry("370x120+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        WIDTH, HEIGHT = 350, 100
        # ============================================================Frames============================================

        self.MFrame = LabelFrame(self, width=360, height=110, font=('arial', 15, 'bold'), bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=5, pady=5)
        # Add image on a Label.
        self.img = ImageTk.PhotoImage(
            Image.open("images\mcabout.gif").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.lbl = tk.Label(self.MFrame, image=self.img)
        self.lbl.img = self.img
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.


if __name__ == "__main__":
    abapp = AboutApp()
    abapp.mainloop()