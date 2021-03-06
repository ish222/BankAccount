import sqlite3


class Database:  # Created a class with static functions to reduce the chance of naming conflicts due to the size of this project
    @staticmethod
    def initSaveData(fname, lname, balance, creditcard, id, password):  # Adds a row of new user information when they register
        """
        # c.execute('''CREATE TABLE clients
        #             (fname text, lname text, balance integer, creditcard integer, id text, password text)''')
        The command above was used to create the table for the base data of the users.
        """
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        c.execute("INSERT INTO clients VALUES (:fname, :lname, :balance, :creditcard, :id, :password)",
                  {'fname': fname, 'lname': lname, 'balance': balance,'creditcard': creditcard, 'id': id, 'password': password})

        conn.commit()
        conn.close()

    @staticmethod
    def secondaryFuncData(id, loan, mortgage, savingsacc, date, mortgageDays):
        """
        c.execute('''CREATE TABLE secData
                         (id text, loan integer, mortgage integer, savingsacc integer, date integer, mortgageDate integer)''')
        """
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        c.execute("INSERT INTO secData VALUES (:id, :loan, :mortgage, :savingsacc, :curdate, :mortgageDays)",
                  {'id': id, 'loan': loan, 'mortgage': mortgage, 'savingsacc': savingsacc, 'curdate': date, 'mortgageDays': mortgageDays})

        conn.commit()
        conn.close()

    @staticmethod
    def saveData(balance, id):
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        c.execute("UPDATE clients SET balance = :balance WHERE id = :id",
                  {'balance': balance, 'id': id})

        conn.commit()
        conn.close()

    @staticmethod
    def saveSecondaryData(id, loan, mortgage, savingsacc, date, mortgageDays):
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        c.execute("UPDATE secData SET loan = :loan, mortgage = :mortgage, savingsacc = :savingsacc, ldate = :curdate, mortgageDate = :mortgageDays WHERE id = :id",
                  {'loan': loan, 'mortgage': mortgage, 'savingsacc': savingsacc, 'id': id, 'curdate': date, 'mortgageDays': mortgageDays})

        conn.commit()
        conn.close()

    @staticmethod
    def getIDs():  # Gets a list of all the IDs of users for login purposes
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        id_list = [id[0] for id in c.execute("SELECT id FROM clients")]

        conn.close()
        return id_list

    @staticmethod
    def getPasswords():  # Gets a list of all the passwords
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        pass_list = [passw[0] for passw in c.execute("SELECT password FROM clients")]

        conn.close()
        return pass_list

    @staticmethod
    def getData(idin):  # Gets row of data for specific user once they login
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        c.execute("SELECT * FROM clients WHERE id=:id", {'id': idin})
        data = c.fetchone()

        conn.close()
        return data

    @staticmethod
    def getSecondaryData(idin):  # Gets row of their secondary data for specific user once they login
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()

        c.execute("SELECT * FROM secData WHERE id=:id", {'id': idin})
        data = c.fetchone()

        conn.close()
        return data


# def alterTable():
#     conn = sqlite3.connect('clients.db')
#     c = conn.cursor()
#
#     c.execute("DELETE FROM clients")
#
#     conn.commit()
#     conn.close()
# alterTable()


# def alterTable():
#     conn = sqlite3.connect('clients.db')
#     c = conn.cursor()
# 
#     c.execute("ALTER TABLE secData ADD mortgageDays integer")
# 
#     conn.commit()
#     conn.close()
# alterTable()
