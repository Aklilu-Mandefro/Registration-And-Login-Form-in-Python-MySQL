import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db

class RegApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SIGN UP ")
        self.resizable(0, 0)
        self.configure(bg="gray")
        self.geometry("347x310+10+60")

        # ====================Variables========================#

        admuname = tk.StringVar()
        admupass = tk.StringVar()

        # ============================================================Frames============================================
        self.MFrame = LabelFrame(self, width=320, height=290, font=('arial', 15, 'bold'), bg='lightblue', bd=15,
                                 relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=20, pady=10)
        self.EFrame = LabelFrame(self, width=200, height=100, font=('arial', 10, 'bold'), bg='lightblue',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels================================================
        self.Lsyslogin = Label(self.MFrame, text='SIGN UP:', font=('arial', 10, 'bold'), bg='lightblue')
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
        self.btnlogin = Button(self.EFrame, text='SIGN UP', font=('arial', 10, 'bold'), width=9, command=self.savst)
        self.btnlogin.grid(row=0, column=0, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='RESET', font=('arial', 10, 'bold'), width=9, command=self.allclear)
        self.btnExit.grid(row=0, column=1, padx=10, pady=10)

        self.btnAbout = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=9, command=self.exitt)
        self.btnAbout.grid(row=0, column=2, padx=10, pady=10)


        # ========================================================functions=================================================
        # ==========Exit Function==========

    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

        # ==========Clear Function==========
    def allclear(self):
        self.TxtUsername.delete(0, END)
        self.Txtupass.delete(0, END)

    # ==========Register student Function==========
    def savst(self):
        admuname = self.TxtUsername.get()
        admupass = self.Txtupass.get()

        if admuname == "" or admupass == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from admin where admuname=%s", admuname)
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "username. already used")
                else:
                    cursor.execute("Insert into admin( admuname, admupass)" "values(%s,%s)", (admuname, admupass))
                    conn.commit()
                    if cursor:
                        mBox.showinfo("Done", "Successfully Registered,Login")
                        self.destroy()
                    else:
                        mBox.showerror("Error", "Unable to Register")
                    cursor.close()
                    conn.close()
            except Exception as es:
                print('Error', f"due to :{str(es)}")

if __name__ == "__main__":
    regpapp = RegApp()
    regpapp.mainloop()

