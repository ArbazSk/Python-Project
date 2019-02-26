from sqlite3 import *

'''pass_manager database '''
	
def create_masterData_db():
	conn=connect("passManager.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS AppLogin (id INTEGER PRIMARY KEY , userName TEXT NOT NULL ,userPassword TEXT NOT NULL)")
	conn.commit()
	conn.close()


def insert_masterData_db(userName,userPassword):
	conn=connect("passManager.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO AppLogin VALUES(NULL,?,?)",(userName,userPassword))
	conn.commit()
	conn.close()

def lohin_check_master(lusername,lpassword):
	conn=connect("passManager.db")
	cur=conn.cursor()
	cur.execute("SELECT userName FROM AppLogin WHERE userName=?",(str(lusername),))
	found_username= cur.fetchone()
	cur.execute("SELECT userPassword FROM AppLogin WHERE userPassword=?",(str(lpassword),))
	found_userpassword=cur.fetchone()
	if lusername== found_username and lpassword== found_userpassword:
		return True
	else:
		print("sorry, Try again")
		return False


def create_userData_db():
	conn=connect("passManager.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS userData (id INTEGER PRIMARY KEY , website TEXT ,password TEXT)")
	conn.commit()
	conn.close()
	


def insert_userData_db(website,password):
	conn=connect("passManager.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO userData VALUES(NULL,?,?)",(website,password))
	conn.commit()
	conn.close()



def view_userData_db():
	conn=connect("passManager.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM userData")
	data1=cur.fetchall()
	conn.commit()
	conn.close()
	print(data1)
	#return data1



def check_all_user():
	conn=connect("passManager.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM AppLogin")
	found_username= cur.fetchall()
	print(found_username)
'''	
#create_masterData_db()
create_userData_db()
insert_userData_db('arbaz','goku@213')
view_userData_db()
'''
