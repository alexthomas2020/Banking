# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from Bank import Bank
from Database import Database
import pandas as pd

"""
Class: Branch
Purpose: Defines the attributes and methods to create the Branch class.
This class is a child class of Bank class.
"""


def get_branch_id(bank_id):
    db = Database("bank.db")
    branches = pd.read_sql("select * from branch", db.connection)
    branches.query('bank_id == @bank_id', inplace=True)
    print("\tBranch ID - Branch Location")
    for index in branches.index:
        print("\t" + branches['branch_id'][index] + " - " + branches['location'][index])


def get_branch_info():
    db = Database("bank.db")
    branches = pd.read_sql("select * from branch", db.connection)
    print("List of Branches...:")
    for index in branches.index:
        print("Location: " + branches['location'][index])
        print("\tBranch ID: " + branches['branch_id'][index])
        print("\tBranch Phone: " + branches['phone'][index])
        print("\tBranch Address: " + branches['br_address'][index])
        print("\tBank ID: " + branches['bank_id'][index])
    db.close()
    return branches


class Branch(Bank):
    def __init__(self, bank_id, name, public, exchange, ceo, coo, cfo, address, branch_id, location, phone, br_address):
        super().__init__(bank_id, name, public, exchange, ceo, coo, cfo, address)
        self.branch_id = branch_id
        self.location = location
        self.phone = phone
        self.br_address = br_address

    def add_branch_record(self):
        db = Database("bank.db")
        db.execute("insert into branch values(:branch_id, :location, :phone, :br_address, :bank_id)",
                   {'branch_id': self.branch_id, 'location': self.location, 'phone': self.phone,
                    'br_address': self.br_address, 'bank_id': self.bank_id})
        db.close(commit=True)

    def set_branch_id(self, branch_id):
        self.branch_id = branch_id
        return self.branch_id

    def set_branch_location(self, location):
        self.location = location
        return self.location

    def set_branch_phone(self, phone):
        self.phone = phone
        return self.phone

    def set_branch_br_address(self, br_address):
        self.br_address = br_address
        return self.br_address


