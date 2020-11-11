# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from Database import Database

"""
Class: Transactions
Purpose: Defines the attributes and methods to create the Transaction class.
"""


class Transaction:
    def __init__(self, tran_id, tran_date, post_date, amount, merchant_cat, tran_type, description):
        self.tran_id = tran_id
        self.tran_date = tran_date
        self.post_date = post_date
        self.amount = amount
        self.merchant_cat = merchant_cat
        self.tran_type = tran_type
        self.description = description

    def add_transaction_record(self, ac_num):
        db = Database("bank.db")
        db.execute("insert into transactions values(:tran_id, :tran_date, :post_date, "
                   ":amount, :merchant_cat, :tran_type, :description, :ac_num)",
                   {'tran_id': self.tran_id, 'tran_date': self.tran_date, 'post_date': self.post_date,
                    'amount': float(self.amount), 'merchant_cat': self.merchant_cat, 'tran_type': self.tran_type,
                    'description': self.description, 'ac_num': ac_num})
        db.close(commit=True)

    def set_transaction_id(self, tran_id):
        self.tran_id = tran_id
        return self.tran_id

    def set_transaction_date(self, tran_date):
        self.tran_date = tran_date
        return self.tran_date

    def set_transaction_post_date(self, post_date):
        self.post_date = post_date
        return self.post_date

    def set_transaction_amount(self, amount):
        self.amount = amount
        return self.amount

    def set_transaction_merchant_cat(self, merchant_cat):
        self.merchant_cat = merchant_cat
        return self.merchant_cat

    def set_transaction_type(self, tran_type):
        self.tran_type = tran_type
        return self.tran_type

    def set_transaction_description(self, description):
        self.description = description
        return self.description


