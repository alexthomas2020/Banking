# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from User import User
from Database import Database
import pandas as pd

"""
Class: Customer
Purpose: Defines the attributes and methods to create the Customer class.
This class is a sub class of User class.
"""


def get_customer_list():
    db = Database("bank.db")
    customers = pd.read_sql('select c.customer_id, u.user_id, u.first_name, u.last_name, u.bank_id, u.user_type from '
                            'customer c, user u where c.user_id = u.user_id and c.customer_id != ""', db.connection)
    print("List of Customers...:")
    for index in customers.index:
        print("Customer ID: " + customers['customer_id'][index])
        print("\tUser ID: " + customers['user_id'][index])
        print("\tFirst Name: " + customers['first_name'][index])
        print("\tLast Name: " + customers['last_name'][index])
        print("\tBank ID: " + customers['bank_id'][index])
        print("\tUser Type: " + customers['user_type'][index])
    db.close()


class Customer(User):
    def __init__(self, user_id, password, first_name, last_name, birth_date, address, user_type, user_status,
                 customer_id, ssn, govt_id):
        super().__init__(user_id, password, first_name, last_name, birth_date, address, user_type, user_status)
        self.customer_id = customer_id
        self.ssn = ssn
        self.govt_id = govt_id

    def add_customer_record(self):
        db = Database("bank.db")
        db.execute("insert into customer values(:customer_id, :ssn, :govt_id, :user_id)",
                   {'customer_id': self.customer_id, 'ssn': self.ssn, 'govt_id': self.govt_id, 'user_id': self.user_id})
        db.close(commit=True)

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
        return self.customer_id

    def set_customer_ssn(self, ssn):
        self.ssn = ssn
        return self.ssn

    def set_customer_govt_id(self, govt_id):
        self.govt_id = govt_id
        return self.govt_id
