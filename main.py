"""
Todo:
Fix class
Find a way to make a global instance of class
Complete service functions
Add new services.
"""

import string
import random
from database import *


class BankAccount:
    def __init__(self, id, fname, lname, init_deposit):
        if self.id == "":
            self.id = self.newid()
            self.fname = fname.lower()
            self.lname = lname.lower()
            self.credit_card = self.newcreditCard()
            self.password = self.newpassword()
            self.balance += init_deposit
        else:
            data = getData(id)  # Data is ('john', 'smith', 2500, 2369149726456860, 'johnJYSvY', 'I=HO1G)y')
            self.fname = data[0]
            self.lname = data[1]
            self.balance = data[2]
            self.credit_card = data[3]
            self.id = id
            self.password = data[5]

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def newcreditCard(self):
        num_list = string.digits
        self.credit_card = int(''.join(random.choice(num_list) for i in range(16)))
        return self.credit_card

    def newid(self):
        char_list_id = string.ascii_letters + string.digits
        id_rand = ''.join(random.choice(char_list_id) for j in range(5))
        self.id = self.fname.lower() + id_rand
        return self.id

    def newpassword(self):
        char_list_pass = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(char_list_pass) for k in range(8))
        return self.password

    def saveToDatabase(self):
        return self.fname, self.lname, self.balance, self.credit_card, self.id, self.password

    def getFromDatabase(self):
        pass


def newAcc():
    fname = input("As you are a new customer, you should open a new account. Please input your first name: ")
    lname = input("Please input your last name: ")
    try:
        initdep = int(input("Please input your initial deposit (input 0 for no deposit): "))
    except Exception as e:
        print("Invalid input!", e)
        newAcc()
    id_class = BankAccount("")
    
    print(f"Your initial balance is {id_class.balance}")
    print(f"You new credit card number is: {id_class.creditCard()}")
    print(f"The ID you will use to login to this service again is: {id_class.id()}")
    print(f"Your password is {id_class.password()}. Please ensure you store it in a password manager.")
    with open('id.txt', 'a') as f:  # Saves the username and password data temporarily for testing purposes
        f.write(id_class.id + " ")
        f.write(id_class.password + "\n")
    cdata = id_class.saveToDatabase()
    saveData(cdata[0], cdata[1], cdata[2], cdata[3], cdata[4], cdata[5])


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
            main(u_name)
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
    deposit = input("How much would you like to deposit?")
    id_class.deposit(deposit)
    


def switch2():
    """
    Withdraw
    :return: New balance
    """

    print("This is switch 2")


def switch3():
    """
    Get Credit card number
    :return: Credit card number
    """

    print("This is switch 3")


def switch4():
    """
    Choose service
    :return:call function of service
    """

    print("This is switch 4")


def switch5():
    """
    Log out
    :return: None
    """
    print("Thank you for using this program!")
    quit()


def main(id):
    # data = getData(id)  # Data is ('john', 'smith', 2500, 2369149726456860, 'johnJYSvY', 'I=HO1G)y')
    id_class = BankAccount(id, "", "", 0)
    name = id_class.fname
    print(f"Welcome {name.capitalize()}!\n\nYou've logged in!\n")
    to_do = input("What would you like to do? \nPress 1 to deposit.\nPress 2 to withdraw.\nPress 3 to get your credit card number.\nPress 4 for a service.\nPress 5 to log out.\n")

    def toDo(switch):
        func = "switch" + str(switch)
        eval(func + "()")
    toDo(to_do)


# Loan, mortgage, savings account, report a fraud.
firstFunction()

