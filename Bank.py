# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from Database import Database
import pandas as pd

"""
Class: Bank
Purpose: Defines the attributes and methods to create the Bank class.
"""


def get_bank_info():
    db = Database("bank.db")
    banks = pd.read_sql("select * from bank", db.connection)
    db.close()
    return banks


def view_bank_records():
    db = Database("bank.db")
    banks = db.query("select * from bank")
    db.close()
    count = 0
    for bank in banks:
        print("\n Bank ID: %s \n\t Bank Name: %s \n\t Public: %s \n\t Exchange: %s \n\t "
              "CEO: %s \n\t COO: %s \n\t CFO: %s \n\t Address: %s" % banks[count])
        count += 1


class Bank:
    def __init__(self, bank_id, name, public, exchange, ceo, coo, cfo, address):
        self.bank_id = bank_id
        self.name = name
        self.public = public
        self.exchange = exchange
        self.ceo = ceo
        self.coo = coo
        self.cfo = cfo
        self.address = address

    def add_bank_record(self):
        db = Database("bank.db")
        db.execute("insert into bank values(:bank_id, :name, :public, :exchange, :ceo, :coo, :cfo, :address)",
                   {'bank_id': self.bank_id, 'name': self.name, 'public': self.public, 'exchange': self.exchange,
                    'ceo': self.ceo, 'coo': self.coo, 'cfo': self.cfo, 'address': self.address})
        db.close(commit=True)

    def set_bank_id(self, bank_id):
        self.bank_id = bank_id
        return self.bank_id

    def set_bank_name(self, name):
        self.name = name
        return self.name

    def set_bank_public(self, public):
        self.public = public
        return self.public

    def set_bank_exchange(self, exchange):
        self.exchange = exchange
        return self.exchange

    def set_bank_ceo(self, ceo):
        self.ceo = ceo
        return self.ceo

    def set_bank_coo(self, coo):
        self.coo = coo
        return self.coo

    def set_bank_cfo(self, cfo):
        self.cfo = cfo
        return self.cfo

    def set_bank_address(self, address):
        self.address = address
        return self.address
