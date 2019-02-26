from tkinter import *
import sqlite3
import database

win1=Tk()
def mainpage(username_data,userpassword_data):
	checkdata=database.lohin_check_master(username_data,userpassword_data)
	win2=Tk()
	win2.geometry("500x300")
	win2.title("List of Websites")
	success=Label(win1,text="Successfully Logged In").grid()
	
	addSite=Button(win2,text="+ Add Site",command=newEntry).grid()
	
	listb=Listbox(win2,height=15,width=70)
	listb.grid(row=1,column=0,rowspan=10,columnspan=10,padx=10,pady=10)
	
	scroll=Scrollbar(win2)
	scroll.grid(row=1,column=11,rowspan=10,sticky=N+S,pady=10)
	
	listb.config(yscrollcommand=scroll.set)
	scroll.config(command=listb.yview)
	
	mainloop()
	
def newEntry():
	win3=Tk()
	win3.geometry("450x150")
	win3.title("New Site Entry")
	url=Label(win3,text="Website URL").grid()
	urlentry=Entry(win3).grid()
	siteuser=Label(win3,text="Username").grid()
	siteuserentry=Entry(win3).grid()
	sitepswd=Label(win3,text="Password").grid()
	sitepswdentry=Entry(win3).grid()
	save=Button(win3,text="Save").grid()
	mainloop()	
def	loginpage():
	win1.title("PassMan - Login")
	
	win1.geometry("500x300")
	
	user=Label(win1,text="Username").grid(row=3,column=0)
	
	username_data=StringVar()
	
	userentry=Entry(win1,textvariable=username_data)
	userentry.grid(row=3,column=20)
	#userentry.delete(0,END)
	
	pswd=Label(win1,text="Password").grid(row=5,column=0)
	
	userpassword_data=StringVar()
	
	passentry=Entry(win1,textvariable=userpassword_data)
	passentry.grid(row=5,column=20)
	#passentry.delete(0,END)
	
	loginbtn=Button(win1,text="Log In",command= lambda: mainpage(username_data,userpassword_data) and viewlist).grid(row=7,column=1)
	
	cancelbtn1=Button(win1,text="Cancel",command=win1.quit).grid(row=7,column=2)
	
	mainloop()

def vewList():
	listb.delete(0,END)
	for row in database.view_userData_db():
		listb.insert(END,row)
		


loginpage()	 

	
