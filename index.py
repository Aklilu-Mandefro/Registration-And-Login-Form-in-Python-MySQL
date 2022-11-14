import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db
from subprocess import call
from dashboard import AdsucApp

# ==========Splash window==========.
SplashApp = tk.Tk()
SplashApp.title("LOGIN SYSTEM")
# ==========set center screen window==========
XLeft = (SplashApp.winfo_screenwidth() - 340) / 2
XTop = (SplashApp.winfo_screenheight() - 80) / 2
SplashApp.geometry("%dx%d+%d+%d" % (340, 80, XLeft, XTop))
SplashApp.resizable(0, 0)
SplashApp.configure(bg="gray")
WIDTH, HEIGHT = 326, 76

# ==========Add splash image on label==========.
img = ImageTk.PhotoImage(Image.open("images\splash.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
lbl = tk.Label(SplashApp, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

# ========================================================Login class===================================================


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LOGIN SYSTEM")
        self.resizable(0, 0)
        self.configure(bg="gray")
        # ==========set center screen window==========
        SLeft = (self.winfo_screenwidth() - 380) / 2
        STop = (self.winfo_screenheight() - 310) / 2
        self.geometry("%dx%d+%d+%d" % (380, 310, SLeft, STop))

        # ====================Variables========================#

        admuname = tk.StringVar()
        admupass = tk.StringVar()


        # ============================================================Frames============================================
        self.MFrame = LabelFrame(self, width=320, height=290, font=('arial', 15, 'bold'), bg='lightblue', bd=15,
                                     relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=20, pady=10)
        self.EFrame = LabelFrame(self, width=200, height=100, font=('arial', 10, 'bold'), bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)



        # ========================================================Labels================================================
        self.Lsyslogin = Label(self.MFrame, text='SYSTEM LOGIN:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lsyslogin.grid(row=1, column=0, sticky=W, padx=20)
        self.LUsername = Label(self.MFrame, text='Username:', font=('arial', 10, 'bold'), bg='lightblue')
        self.LUsername.grid(row=2, column=0, sticky=W, padx=20)
        self.Lupass = Label(self.MFrame, text='Password:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lupass.grid(row=3, column=0, sticky=W, padx=20)

        # ========================================================Entries of Frame======================================

        self.TxtUsername = Entry(self.MFrame, font=('arial', 10, 'bold'), textvariable=admuname)
        self.TxtUsername.grid(row=2, column=1, padx=10, pady=5)
        self.Txtupass = Entry(self.MFrame, font=('arial', 10, 'bold'), show="*", textvariable=admupass)
        self.Txtupass.grid(row=3, column=1, padx=10, pady=5)

        # ========================================================Buttons of EFrame=====================================
        self.btnlogin = Button(self.EFrame, text='LOGIN', font=('arial', 10, 'bold'), width=9, command=self.adlogn)
        self.btnlogin.grid(row=0, column=0, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=9, command=self.exitt)
        self.btnExit.grid(row=0, column=1, padx=10, pady=10)

        self.btnAbout = Button(self.EFrame, text='ABOUT', font=('arial', 10, 'bold'), width=9, command=self.clickabout)
        self.btnAbout.grid(row=0, column=2, padx=10, pady=10)
        self.btnReg = Button(self.EFrame, text='REGISTER', font=('arial', 10, 'bold'), width=9, command=self.clickreg)
        self.btnReg.grid(row=1, column=1, padx=10, pady=10)

    # ========================================================functions=================================================
    # ==========Exit Function==========
    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Functions to call scripts==========


    def clickabout(self):
        call(["python", "About.py"])

    def clickreg(self):
        call(["python", "Register.py"])



    # ==========Function for  login==========.

    def adlogn(self):
        admuname = self.TxtUsername.get()
        admupass = self.Txtupass.get()
        if admuname == "" or admupass == "":
            mBox.showerror(self, 'Error Enter username & password')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from admin where admuname=%s and admupass=%s", (admuname, admupass))
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "Login Successfully")
                    self.destroy()
                    AdsucApp()
                else:
                    mBox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
                cursor.close()
                conn.close()
            except Exception as es:
                print('Error', f"due to :{str(es)}")




# ==========Function for to call main window==========

def callmainroot():
    SplashApp.destroy()
    LoginApp()

# ==========Display splash window then main window==========


SplashApp.after(2000, callmainroot)

mainloop()