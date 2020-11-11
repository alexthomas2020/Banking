# Banking Application
# Author: Alex Thomas
# Updated: 11/10/2020

import unittest
from Account import get_account, get_accounts, Account

"""
Banking Application - Unit tests for Account class.
"""


class TestAccount(unittest.TestCase):
    def test_get_account(self):
        # check if the function returns account details.
        ac_num = 'A1469'
        ac_dict = get_account(ac_num)
        self.assertGreater(len(ac_dict), 0)

    def test_get_accounts(self):
        # check if the function returns 1 or more account records.
        accounts = get_accounts()
        self.assertGreater(len(accounts.shape), 0)

    def test_add_account_record(self):
        # check if the function inserts account record into database.
        ac_num = 'A_TEST1'
        ac_type = 'C'
        open_date = '12/12/2020'
        close_date = ""
        balance = int(10.00)
        status = 'A'
        customer_id = "C_TEST123"
        account = Account(ac_num, ac_type, open_date, close_date, balance, status)
        account.add_account_record(customer_id)
        ac_dict = get_account(ac_num)
        self.assertGreater(len(ac_dict), 0)

    def test_deposit(self):
        # check if the function deposit adds money to the account.
        ac_num = 'A1469'
        acc_dict = get_account(ac_num)
        balance = acc_dict['balance']
        account = Account(ac_num, "", "", "", balance, "")
        deposit_amount = 99.00
        new_balance = account.deposit(deposit_amount)
        self.assertGreater(new_balance, deposit_amount)

    def test_withdrawal(self):
        # check if the function withdraws amount from the account.
        ac_num = 'A1469'
        acc_dict = get_account(ac_num)
        balance = acc_dict['balance']
        account = Account(ac_num, "", "", "", balance, "")
        withdraw_amount = 99.00
        new_balance = account.withdraw(withdraw_amount)
        self.assertGreater(new_balance, withdraw_amount)


if __name__ == '__main__':
    unittest.main()
