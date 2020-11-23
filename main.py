"""
Todo:
Fix class DONE
Find a way to make a global instance of class DONE
Complete service functions
Add new services.
"""

import string
import random
from database import *


class BankAccount:
    def __init__(self, id):
        self.data = getData(id)  # Data is ('john', 'smith', 2500, 2369149726456860, 'johnJYSvY', 'I=HO1G)y')
        self.fname = self.data[0]
        self.lname = self.data[1]
        self.balance = self.data[2]
        self.credit_card = self.data[3]
        self.id = id
        self.password = self.data[5]

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def saveToDatabase(self):
        return self.fname, self.lname, self.balance, self.credit_card, self.id, self.password

    def getFromDatabase(self):
        pass


class NewAccount:
    def __init__(self, fname, lname, init_deposit):
        self.fname = fname.lower()
        self.lname = lname.lower()
        self.balance = init_deposit
        self.credit_card = self.newcreditCard()
        self.password = self.newpassword()
        self.id = self.newid()

    def newcreditCard(self):
        num_list = string.digits
        self.credit_card = int(''.join(random.choice(num_list) for i in range(16)))
        return self.credit_card

    def newid(self):
        char_list_id = string.ascii_letters + string.digits
        id_rand = ''.join(random.choice(char_list_id) for j in range(5))
        self.id = self.fname + id_rand
        return self.id

    def newpassword(self):
        char_list_pass = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(char_list_pass) for k in range(8))
        return self.password

    def saveToDatabase(self):
        return self.fname, self.lname, self.balance, self.credit_card, self.id, self.password


def instance(id):
    """
    Creates a global instance of the BankAccount class
    :param id: User id
    :return: None
    """
    global id_class
    id_class = BankAccount(id)


def newAcc():
    fname = input("As you are a new customer, you should open a new account. Please input your first name: ")
    lname = input("Please input your last name: ")
    # try:
    initdep = int(input("Please input your initial deposit (input 0 for no deposit): "))
    # except Exception as e:
    #     print("Invalid input!", e)
    #     newAcc()
    newid_class = NewAccount(fname, lname, initdep)
    print(f"Your initial balance is {newid_class.balance}")
    print(f"You new credit card number is: {newid_class.credit_card}")
    print(f"The ID you will use to login to this service again is: {newid_class.id}")
    print(f"Your password is {newid_class.password}. Please ensure you store it in a password manager.")
    with open('id.txt', 'a') as f:  # Saves the username and password data temporarily for testing purposes
        f.write(newid_class.id + " ")
        f.write(newid_class.password + "\n")
    cdata = newid_class.saveToDatabase()
    initSaveData(cdata[0], cdata[1], cdata[2], cdata[3], cdata[4], cdata[5])
    print("Please restart the program and login with your new credentials!")
    quit()


def login():
    u_name = input("Please input your banking ID: (or leave empty to go back). ")
    id_list = getIDs()
    pass_list = getPasswords()
    id_dict = {}
    for i in range(len(id_list)):
        id_dict[id_list[i]] = pass_list[i]
    if u_name in id_dict:
        password = input("Please input your password: ")
        if id_dict[u_name] == password:
            instance(u_name)
            name = id_class.fname + " " + id_class.lname
            print(f"Welcome {name.capitalize()}!\n\nYou've logged in!\n")
            main()
        else:
            print("Wrong password, please try again!")
            login()
    elif u_name == "":
        firstFunction()
    else:
        print("Invalid username, please try again!")
        login()



def firstFunction():
    new = input("Welcome to your banking service.\nAre you a new or returning customer? Please type 'New' for new or 'old' for returning customer. ")
    if new.lower() == "new":
        newAcc()
    elif new.lower() == "old":
        login()
    else:
        print("Invalid input please try again.")
        firstFunction()


def switch1():
    """
    Deposit
    :return: New balance
    """
    deposit = int(input("How much would you like to deposit?"))
    id_class.deposit(deposit)
    main()
    


def switch2():
    """
    Withdraw
    :return: New balance
    """
    withdraw = int(input("How much would you like to withdraw?"))
    if id_class.balance > withdraw:
        id_class.withdraw(withdraw)
        print(f"Your new balance is {id_class.balance}")
    else:
        print(f"You have insufficient funds for this transaction. Your current balance is {id_class.balance}")
    main()


def switch3():
    """
    Get Credit card number
    :return: Credit card number
    """
    print(f"Your credit card number is: {id_class.credit_card}")
    main()


def switch4():
    """
    Choose service
    :return:call function of service
    """

    print("Services are still in progress! Please come back soon.")
    main()


def switch5():
    """
    Log out
    :return: None
    """
    saveData(id_class.balance, id_class.id)
    print("Thank you for using this program!")
    quit()


def main():
    print(f"Your current balance is {id_class.balance}")
    to_do = input("What would you like to do? \nPress 1 to deposit.\nPress 2 to withdraw.\nPress 3 to get your credit card number.\nPress 4 for a service.\nPress 5 to log out.\n")
    def toDo(switch):
        """
        Functionality of a switch statement, didnt want to use too many conditional statements
        :param switch: switch number
        :return: None
        """
        func = "switch" + str(switch)
        eval(func + "()")
    toDo(to_do)


# Loan, mortgage, savings account, report a fraud.
firstFunction()

