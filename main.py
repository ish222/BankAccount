"""
Todo:
Fix class DONE
Find a way to make a global instance of class DONE
Complete service functions
Add new services.
"""

import string
import random
from database import Database
from datetime import date
import time

curDate = date.today()
intCurDate = int(curDate.strftime('%Y%m%d'))


class BankAccount:
    def __init__(self, id):
        self.data = Database.getData(id)  # Data is ('john', 'smith', 2500, 2369149726456860, 'johnJYSvY', 'I=HO1G)y')
        self.secData = Database.getSecondaryData(id)  # id, loan, mortgage, savingsacc, date, mortgageDays
        self.fname = self.data[0]
        self.lname = self.data[1]
        self.balance = self.data[2]
        self.credit_card = self.data[3]
        self.id = id
        self.password = self.data[5]
        self.loan = self.secData[1]
        self.mortgage = self.secData[2]
        self.savingsacc = self.secData[3]
        self.LastDate = str(self.secData[4])
        self.lastDate = date(year=int(self.LastDate[0:4]), month=int(self.LastDate[4:6]), day=int(self.LastDate[6:8]))
        self.dateDelta = (curDate - self.lastDate).days
        self.interestRate = 0
        self.mortgageDays = self.secData[5]
        if self.loan != 0:
            self.loanInterest()
        if self.savingsacc != 0:
            self.savingsInterest()
        if self.mortgage != 0 and self.dateDelta != 0:
            self.mortgageInterest()
            self.payMortgage()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def loanInterest(self):
        if self.loan != 0:
            self.interestRate = float(0.15 / 365)
            self.loan *= ((1 + self.interestRate) * self.dateDelta)

    def savingsInterest(self):
        if self.savingsacc != 0:
            self.interestRate = float(0.02 / 365)
            self.savingsacc *= ((1 + self.interestRate) * self.dateDelta)

    def mortgageInterest(self):
        if self.mortgage != 0:
            self.interestRate = float(0.0354 / 365)
            self.mortgage *= ((1 + self.interestRate) * self.dateDelta)

    def payMortgage(self):
        self.changeBalance = self.mortgage / (self.mortgageDays / self.dateDelta)
        self.balance -= self.changeBalance
        self.mortgage -= self.changeBalance
        self.mortgageDays -= self.dateDelta


class NewAccount:
    def __init__(self, fname, lname, init_deposit):
        self.fname = fname.lower()
        self.lname = lname.lower()
        self.balance = init_deposit
        self.credit_card = self.newcreditCard()
        self.password = self.newpassword()
        self.id = self.newid()
        self.loan = 0
        self.mortgage = 0
        self.savingsacc = 0
        self.date = intCurDate
        self.mortgageDays = 0
        Database.initSaveData(self.fname, self.lname, self.balance, self.credit_card, self.id, self.password)
        Database.secondaryFuncData(self.id, self.loan, self.mortgage, self.savingsacc, self.date, self.mortgageDays)

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


class InitSwitches:
    @staticmethod
    def switch1():
        """
        Deposit
        :return: New balance
        """
        deposit = int(input("How much would you like to deposit?"))
        id_class.deposit(deposit)
        main()

    @staticmethod
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

    @staticmethod
    def switch3():
        """
        Get Credit card number
        :return: Credit card number
        """
        print(f"Your credit card number is: {id_class.credit_card}")
        main()

    @staticmethod
    def switch4():
        """
        Choose service
        :return:call function of service
        """

        to_do = input(
            "What would you like to do? \n"
            "Press 1 to request or repay a loan.\n"
            "Press 2 to request or see your mortgage.\n"
            "Press 3 to deposit to or withdraw from your savings account.\n"
            "Press 4 to report a fraud.\n"
            "Press 5 to go back.\n")
        if to_do == "1":
            SecondarySwitches.loan()
        elif to_do == "2":
            SecondarySwitches.mortgage()
        elif to_do == "3":
            SecondarySwitches.savings()
        elif to_do == "4":
            SecondarySwitches.fraud()
        elif to_do == "5":
            main()
        else:
            print("Invalid input, please try again!")
            InitSwitches.switch4()

    @staticmethod
    def switch5():
        """
        Log out
        :return: None
        """
        Database.saveData(id_class.balance, id_class.id)
        Database.saveSecondaryData(id_class.id, id_class.loan, id_class.mortgage, id_class.savingsacc, intCurDate, id_class.mortgageDays)
        print("Thank you for using this program!")
        quit()


class SecondarySwitches:
    @staticmethod
    def loan():
        def addLoanFunc():
            try:
                addLoan = int(
                    input("The interest rate we offer for loans is 15% APR. \nHow much would you like to take out: "))
            except Exception as e:
                print("Invalid input ", e)
                SecondarySwitches.loan()
            if addLoan < 0:
                print("Invalid input, you input a negative, please try again!")
                addLoanFunc()
            id_class.loan += addLoan
            print(f"Your new loan is: {id_class.loan}")
            time.sleep(1)

        print(f"Your total current outstanding loan is: {id_class.loan}")
        if id_class.loan == 0:
            addLoanFunc()
            time.sleep(1)
            InitSwitches.switch4()
        to_do = input("Press 1 to repay your loan\nPress 2 to take out a new one\nPress 3 to go back\n")
        if to_do == "1":
            addLoanFunc()
        elif to_do == "2":
            try:
                payLoan = int(
                    input("How much would you like to pay back: "))
            except Exception as e:
                print("Invalid input ", e)
                SecondarySwitches.loan()
            if id_class.balance > payLoan or id_class.loan > payLoan:
                id_class.balance -= payLoan
                id_class.loan -= payLoan
            elif payLoan < 0:
                print("Invalid input, you input a negative, please try again!")
                time.sleep(1)
                SecondarySwitches.loan()
            else:
                print("Your input was either more than your available balance or "
                      "more than your outstanding loan. Please try again!")
                time.sleep(1)
                SecondarySwitches.loan()
        else:
            print("Invalid input, please try again!")
            time.sleep(1)
            SecondarySwitches.loan()
        InitSwitches.switch4()

    @staticmethod
    def savings():
        def addSavings():
            try:
                amount = int(input("How much would you like to add to your savings account: "))
            except Exception as e:
                print(f"Invalid input: {e}\nTry again!")
                time.sleep(1)
                addSavings()
            if amount > id_class.balance:
                print(
                    "You don't have that much money in your account! Please input a value equal to or lower than your current balance!")
                addSavings()
            elif amount < 0:
                print("Invalid input, you input a negative, please try again!")
                time.sleep(1)
                addSavings()
            else:
                id_class.savingsacc += amount
                id_class.balance -= amount
                print(f"Success, your new savings balance is: {id_class.savingsacc}\n"
                      f"Your new balance is: {id_class.balance}")
                time.sleep(1)
                InitSwitches.switch4()

        def withdraw():
            try:
                amount = int(input("How much would you like to withdraw from your savings account?"))
            except Exception as e:
                print(f"Invalid input: {e}\nTry again!")
                time.sleep(1)
                withdraw()
            if amount > id_class.savingsacc:
                print("You dont have that much in your savings account, please try again!")
                withdraw()
            elif amount < 0:
                print("Invalid input, you input a negative, please try again!")
                time.sleep(1)
                withdraw()
            else:
                id_class.savings -= amount
                id_class.balance += amount

        if id_class.savingsacc == 0:
            print("You have no money in your savings account. Please add some.")
            addSavings()
            InitSwitches.switch4()

        else:
            print(f"Your current savings are: {id_class.savingsacc}")
            to_do = input(
                "Press 1 to transfer to your savings account\nPress 2 to withdraw from your savings account\nPress 3 to go back\n")
            if to_do == "1":
                addSavings()
            elif to_do == "2":
                withdraw()
            elif to_do == "3":
                InitSwitches.switch4()
            else:
                print("Invalid input please try again!")
                time.sleep(1)
                SecondarySwitches.savings()
        InitSwitches.switch4()

    @staticmethod
    def mortgage():
        def addMortgage():
            try:
                amount = int(input(
                    "We offer 10 year mortgage deals at 3.54% APR interest!\nPlease input how much mortgage you want to take out: "))
            except Exception as e:
                print(f"Invalid input: {e}\nPlease try again!")
                addMortgage()
            if amount <= 0:
                print("Invalid input, you input 0 or a negative number! Please try again.")
                addMortgage()
            else:
                id_class.mortgage = amount
                id_class.mortgageDays = 365
            print(f"Your new mortgage is: {id_class.mortgage}")
            time.sleep(1)

        print(f"You current outstanding mortgage is: {id_class.mortgage}")
        time.sleep(1)
        if id_class.mortgage == 0:
            addMortgage()
        else:
            InitSwitches.switch4()
        InitSwitches.switch4()

    @staticmethod
    def fraud():
        text = input("Please, in as much detail as possible, write the details of the fraud you want to report:\n"
                     "Please press enter at the END of your message.\nMessage: ")
        with open("reports.txt", 'a') as f:
            f.write(f"Id = {id_class}, Date = {curDate}, Report message = {text}\n")
        time.sleep(1)
        print("Thanks, we've received your message. We appreciate your assistance.")
        time.sleep(1.5)
        InitSwitches.switch4()


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
    try:
        initdep = int(input("Please input your initial deposit (input 0 for no deposit): "))
    except Exception as e:
        print("Invalid input!", e)
        newAcc()
    newid_class = NewAccount(fname, lname, initdep)
    print(f"Your initial balance is {newid_class.balance}")
    print(f"You new credit card number is: {newid_class.credit_card}")
    print(f"The ID you will use to login to this service again is: {newid_class.id}")
    print(f"Your password is {newid_class.password}. Please ensure you store it in a password manager.")
    with open('id.txt', 'a') as f:  # Saves the username and password data temporarily for testing purposes
        f.write(newid_class.id + " ")
        f.write(newid_class.password + "\n")
    print("Please restart the program and login with your new credentials!")
    quit()


def login():
    u_name = input("Welcome to your banking service.\nPlease input your banking ID: (type 'New' if you are a new customer!) ")
    if u_name.lower == "new":
        newAcc()
    id_list = Database.getIDs()
    pass_list = Database.getPasswords()
    id_dict = {}
    for i in range(len(id_list)):
        id_dict[id_list[i]] = pass_list[i]
    if u_name in id_dict:
        password = input("Please input your password: ")
        if id_dict[u_name] == password:
            instance(u_name)
            name = id_class.fname + " " + id_class.lname
            print(f"Welcome {name.capitalize()}!\n\nYou've logged in!\n")
            print(f"Your current balance is {id_class.balance}\n")
            main()
        else:
            print("Wrong password, please try again!")
            login()
    elif u_name == "":
        login()
    else:
        print("Invalid username, please try again!")
        login()


def main():
    time.sleep(1)
    to_do = input("What would you like to do? \nPress 1 to deposit.\nPress 2 to withdraw.\n"
                  "Press 3 to get your credit card number.\nPress 4 for a service.\nPress 5 to log out.\n")

    def toDo(switch):
        """
        Functionality of a switch statement, didnt want to use too many conditional statements
        :param switch: switch number
        :return: None
        """
        func = "InitSwitches."  "switch" + str(switch)
        eval(func + "()")

    toDo(to_do)


# Loan, mortgage, savings account, report a fraud.
login()
