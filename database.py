import sqlite3


def initSaveData(fname, lname, balance, creditcard, id, password):  # Adds a row of new user information when they register
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # c.execute('''CREATE TABLE clients
    #             (fname text, lname text, balance integer, creditcard integer, id text, password text)''')

    c.execute("INSERT INTO clients VALUES (:fname, :lname, :balance, :creditcard, :id, :password)",
              {'fname': fname, 'lname': lname, 'balance': balance,'creditcard': creditcard, 'id': id, 'password': password})

    conn.commit()
    conn.close()


def saveData(balance, id):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    c.execute("UPDATE clients SET balance = :balance WHERE id = :id",
              {'balance': balance, 'id': id})

    conn.commit()
    conn.close()


def getIDs():  # Gets a list of all the IDs of users for login purposes
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    
    id_list = [id[0] for id in c.execute("SELECT id FROM clients")]

    conn.close()
    return id_list


def getPasswords():  # Gets a list of all the passwords
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    pass_list = [passw[0] for passw in c.execute("SELECT password FROM clients")]

    conn.close()
    return pass_list


def getData(idin):  # Gets row of data for specific user once they login
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    c.execute("SELECT * FROM clients WHERE id=:id", {'id': idin})
    data = c.fetchone()

    conn.close()
    return data
