from tkinter import *
import trashdatabase as db


class Manager:
    def __init__(self):
        self.win1 = Tk()
        db.create_masterData_db()
        db.create_userData_db()

    def loginpage(self):           
        self.win1.title("PassMan - Login")
        self.win1.geometry("500x300")
        Label(self.win1, text="Username:").grid(row=0, column=0)
        self.username_data = StringVar()
        self.userentry = Entry(self.win1, textvariable=self.username_data)
        self.userentry.grid(row=0, column=1, columnspan=4)

        Label(self.win1, text="Password:").grid(row=1, column=0)

        self.userpassword_data = StringVar()
        self.passentry = Entry(self.win1, textvariable=self.userpassword_data, show="*")
        self.passentry.grid(row=1, column=1, columnspan=8)

        loginbtn = Button(self.win1, text="Log In", command=self.check)
        loginbtn.grid(row=2, column=1)

        Button(self.win1, text="Cancel", command=self.win1.quit).grid(row=2, column=2)

        Button(self.win1, text="Create Account", command=self.createAccount).grid(row=2, column=3)

        mainloop()

    def mainpage(self):
        win2 = Tk()
        win2.geometry("500x300")
        win2.title("List of Websites")
        Label(self.win1, text="Successfully Logged In").grid()
        Button(win2, text="+ Add Site", command=self.newEntry).grid(row=0, column=1)
        Button(win2, text="View All", command=self.viewList, width=8).grid(row=0, column=2)
        self.listb = Listbox(win2, height=15, width=70)
        self.listb.grid(row=1, column=0, rowspan=10, columnspan=10, padx=10, pady=10)
        self.listb.bind("<<listboxSelect>>", self.selection)
        scroll = Scrollbar(win2)
        scroll.grid(row=1, column=11, rowspan=10, sticky=N + S, pady=10)
        # configure
        self.listb.config(yscrollcommand=scroll.set)
        scroll.config(command=self.listb.yview)
        self.viewList()
        mainloop()

    def newEntry(self):
        self.win3 = Tk()
        self.win3.geometry("450x150")
        self.win3.title("New Site Entry")
        Label(self.win3, text="Website URL").grid(row=1, column=0)
        Label(self.win3, text="Username").grid(row=3, column=0)
        Label(self.win3, text="Password").grid(row=5, column=0)
        self.newebsite = StringVar(self.win3)
        Entry(self.win3, textvariable=self.newebsite).grid(row=2, column=0)
        self.neuser = StringVar(self.win3)
        Entry(self.win3, textvariable=self.neuser).grid(row=4, column=0)
        self.nepass = StringVar(self.win3)
        Entry(self.win3, textvariable=self.nepass).grid(row=6, column=0)
        Button(self.win3, text="Save", command=self.entryexit).grid()
        self.viewList()
        mainloop()

    def createAccount(self):
        self.win4 = Tk()
        self.win4.geometry("450x250")
        self.win4.title("Create Account")
        Label(self.win4, text=" User Name").grid(row=0, column=0)
        Label(self.win4, text="Password").grid(row=1, column=0)
        self.causer = StringVar(self.win4)  # user name entry
        Entry(self.win4, textvariable=self.causer).grid(row=0, column=1)
        self.capass = StringVar(self.win4)  # password entry
        Entry(self.win4, textvariable=self.capass).grid(row=1, column=1)
        Button(self.win4, text="Sign Up", command=self.signup).grid(row=2, column=1)
        mainloop()

    def signup(self):
        db.insert_masterData_db(self.causer.get(), self.capass.get())
        Label(self.win4, text="successfully Created").grid(columnspan=4)
        self.win4.destroy()

    def check(self):
        if self.username_data.get()!='' and self.userpassword_data.get()!='':
            if db.login_check_master(self.username_data.get(), self.userpassword_data.get()):
                self.userentry.delete(0, END)
                self.passentry.delete(0, END)
                self.mainpage()
            else:
                Label(self.win1, text="UserName or Password did not matched").grid(row=3, column=0, columnspan=4)
        else:
            Label(self.win1, text="Please Fill The Username and Password").grid(row=3, column=0, columnspan=4)

    def entryexit(self):
        db.insert_userData_db(self.newebsite.get(), self.neuser.get(), self.nepass.get())
        self.win3.quit()

    def viewList(self):
        self.listb.delete(0, END)
        for row in db.view_userData_db():
            self.listb.insert(END, "Website:")
            self.listb.insert(END, row[1])
            self.listb.insert(END, "User Name:")
            self.listb.insert(END, row[2])
            self.listb.insert(END, "Password:")
            self.listb.insert(END, row[3])
            self.listb.insert(END, "--------------------------")

    def selection(self, event):
        cur_sel = self.listb.curselection()[0]
        index = self.listb.get(cur_sel)
        print(index)

c = Manager()
c.loginpage()

