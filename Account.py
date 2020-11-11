# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from Database import Database
import pandas as pd

"""
Class: Account
Purpose: Defines the attributes and methods to create the Account class.
"""


def get_account(ac_num):
    db = Database("bank.db")
    account = pd.read_sql("select * from account where ac_num = :ac_num", db.connection, params={'ac_num': ac_num})
    account_dict = {}
    if not account.empty:
        account_list = account.to_dict('records')
        account_dict = account_list[0]
    return account_dict


def get_accounts():
    db = Database("bank.db")
    accounts = pd.read_sql("select a.ac_num, a.ac_type, a.open_date, a.balance, a.status, "
                           "u.first_name, u.last_name, u.bank_id from account a, customer c, user u where "
                           "a.customer_id = c.customer_id and c.user_id = u.user_id", db.connection)
    print("List of Accounts...:")
    for index in accounts.index:
        print("Account Number: " + accounts['ac_num'][index])
        print("\tFirst Name: " + accounts['first_name'][index])
        print("\tLast Name: " + accounts['last_name'][index])
        print("\tAccount Balance: " + str(accounts['balance'][index]))
        print("\tAccount Status: " + accounts['status'][index])
        print("\tAccount Type: " + accounts['ac_type'][index])
        print("\tOpen Date: " + accounts['open_date'][index])
        print("\tBank ID: " + accounts['bank_id'][index])
    db.close()
    return accounts


class Account:
    def __init__(self, ac_num, ac_type, open_date, close_date, balance, status):
        self.ac_num = ac_num
        self.ac_type = ac_type
        self.open_date = open_date
        self.close_date = close_date
        self.balance = int(balance)
        self.status = status

    def add_account_record(self, customer_id):
        db = Database("bank.db")
        db.execute("insert into account values(:ac_num, :ac_type, :open_date, "
                   ":close_date, :balance, :status, :customer_id )",
                   {'ac_num': self.ac_num, 'ac_type': self.ac_type, 'open_date': self.open_date,
                    'close_date': self.close_date, 'balance': self.balance, 'status': self.status,
                    'customer_id': customer_id})
        db.close(commit=True)

    def set_account_num(self, ac_num):
        self.ac_num = ac_num
        return self.ac_num

    def set_account_type(self, ac_type):
        self.ac_type = ac_type
        return self.ac_type

    def set_account_open_date(self, open_date):
        self.open_date = open_date
        return self.open_date

    def set_account_close_date(self, close_date):
        self.close_date = close_date
        return self.close_date

    def set_account_balance(self, balance):
        self.balance = balance
        return self.balance

    def set_account_status(self, status):
        self.status = status
        return self.status

    def deposit(self, amount):
        self.balance += int(amount)
        db = Database("bank.db")
        db.execute("UPDATE account SET balance = :balance where ac_num = :ac_num",
                   {'ac_num': self.ac_num, 'balance': self.balance})
        db.close(commit=True)
        return self.balance

    def withdraw(self, amount):
        self.balance -= int(amount)
        db = Database("bank.db")
        db.execute("UPDATE account SET balance = :balance where ac_num = :ac_num",
                   {'ac_num': self.ac_num, 'balance': self.balance})
        db.close(commit=True)
        return self.balance
