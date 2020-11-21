import string
import random
from database import *


class BankAccount:
    def __init__(self, fname, lname, initdep):
        self.fname = fname.lower()
        self.lname = lname.lower()
        self.name = fname + lname
        self.balance = initdep

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def creditCard(self):
        num_list = string.digits
        self.credit_card = int(''.join(random.choice(num_list) for i in range(16)))
        return self.credit_card

    def id(self):
        char_list_id = string.ascii_letters + string.digits
        id_rand = ''.join(random.choice(char_list_id) for j in range(5))
        self.id = self.fname.lower() + id_rand
        return self.id

    def password(self):
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
    client1 = BankAccount(fname, lname, initdep)
    print(f"Your initial balance is {client1.balance}")
    print(f"You new credit card number is: {client1.creditCard()}")
    print(f"The ID you will use to login to this service again is: {client1.id()}")
    print(f"Your password is {client1.password()}. Please ensure you store it in a password manager.")
    with open('id.txt', 'a') as f:  # Saves the username and password data temporarily for testing purposes
        f.write(client1.id + " ")
        f.write(client1.password + "\n")
    cdata = client1.saveToDatabase()
    saveData(cdata[0], cdata[1], cdata[2], cdata[3], cdata[4], cdata[5])


def login():
    u_name = input("Please input your banking ID: (or leave empty to go back). ")
    id_list = getIDs()
    pass_list = getPasswords()
    if u_name in id_list:
        password = input("Please input your password: ")
        if password in pass_list:
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
    new = input("Welcome to your banking service.\nAre you a new or returning customer? Please type 'New' for new or 'old' for returning customer ")
    if new.lower() == "new":
        newAcc()
    elif new.lower() == "old":
        login()
    else:
        print("Invalid input please try again.")
        firstFunction()


def main(id):
    pass


firstFunction()
