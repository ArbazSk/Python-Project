from sqlite3 import *

'''manager database '''

def create_masterData_db():
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS AppLogin (id INTEGER PRIMARY KEY , userName TEXT NOT NULL ,userPassword TEXT NOT NULL)")
    conn.commit()
    conn.close()

def insert_masterData_db(userName, userPassword):
    if userName!='' and userPassword!='':
        conn = connect("passManager.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO AppLogin VALUES(NULL,?,?)",(userName,userPassword))
        conn.commit()
        conn.close()

def delete_masterData_db(id):
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM AppLogin WHERE  id=?", (id,))  #userData
    conn.commit()
    conn.close()

def login_check_master(lusername, lpassword):
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("SELECT userName FROM AppLogin WHERE userName=?", (lusername,))
    found_username = cur.fetchone()

    cur.execute("SELECT userPassword FROM AppLogin WHERE userPassword=?", (lpassword,))
    found_userpassword = cur.fetchone()

    if (found_username and found_userpassword):
        print("welcome",found_username[0])
        return True
    else:
        print("sorry try again")
        return False

def create_userData_db():
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS userData (id INTEGER PRIMARY KEY , website TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL )")
    conn.commit()
    conn.close()

def insert_userData_db(website, username, password):
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO userData VALUES(NULL,?,?,?)", (str(website), str(username), str(password)))
    conn.commit()
    conn.close()

def delete_userData_db(id):
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM userData WHERE  id=?", (id,))  #userData
    conn.commit()
    conn.close()

def view_userData_db():
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM userData") #userData
    data1 = cur.fetchall()
    conn.commit()
    conn.close()
    print(data1)
    return data1

def view_masterData_db():
    conn = connect("passManager.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM AppLogin") #userData
    data1 = cur.fetchall()
    conn.commit()
    conn.close()
    print(data1)
    return data1

