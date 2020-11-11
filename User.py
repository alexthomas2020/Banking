# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from Database import Database
import pandas as pd

"""
Class: User
Purpose: Defines the attributes and methods to create the User class.
"""


def get_user_info(bank_id):
    db = Database("bank.db")
    users = pd.read_sql("select * from user", db.connection)
    users.query('bank_id == @bank_id', inplace=True)
    print("List of Users...:")
    for index in users.index:
        print("User ID: " + users['user_id'][index])
        print("\tFirst Name: " + users['first_name'][index])
        print("\tLast Name: " + users['last_name'][index])
        print("\tBirth Date: " + users['birth_date'][index])
        print("\tAddress: " + users['address'][index])
        print("\tUser Type: " + users['user_type'][index])
        print("\tUser Status: " + users['user_status'][index])
        print("\tBank ID: " + users['bank_id'][index])
    db.close()
    return users


def check_user(user_id):
    db = Database("bank.db")
    users = pd.read_sql("select * from user", db.connection)
    users.query('user_id == @user_id', inplace=True)
    invalid_selection = False
    if users.empty:
        invalid_selection = True
    return invalid_selection


class User:
    def __init__(self, user_id, password, first_name, last_name, birth_date, address, user_type, user_status):
        self.user_id = user_id
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.user_type = user_type
        self.user_status = user_status

    def add_user_record(self, bank):
        db = Database("bank.db")
        db.execute("insert into user values(:user_id, :password, :first_name, :last_name, :birth_date, "
                   ":address, :user_type, :user_status, :bank_id)",
                   {'user_id': self.user_id, 'password': self.password, 'first_name': self.first_name,
                    'last_name': self.last_name, 'birth_date': self.birth_date, 'address': self.address,
                    'user_type': self.user_type, 'user_status': self.user_status, 'bank_id': bank.bank_id})
        db.close(commit=True)

    def set_user_id(self, user_id):
        self.user_id = user_id
        return self.user_id

    def set_user_password(self, password):
        self.password = password
        return self.password

    def set_user_first_name(self, first_name):
        self.first_name = first_name
        return self.first_name

    def set_user_last_name(self, last_name):
        self.last_name = last_name
        return self.last_name

    def set_user_birth_date(self, birth_date):
        self.birth_date = birth_date
        return self.birth_date

    def set_user_address(self, address):
        self.address = address
        return self.address

    def set_user_type(self, user_type):
        self.user_type = user_type
        return self.user_type

    def set_user_status(self, user_status):
        self.user_status = user_status
        return self.user_status
