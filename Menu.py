# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

import random
from Bank import get_bank_info
from User import get_user_info, check_user
from Branch import get_branch_id
from Customer import get_customer_list
from datetime import date
from Account import get_accounts, get_account


"""
This file defines helper functions for each of the menu items.
Helper functions gather data from users and crate a dictionary 
or list object, which will be returned to the main menu to help
build the necessary objects and to execute DML statements.
"""


def add_bank_menu():
    bank_id = random.choice(range(1000, 10000))
    bank_id = "bank" + str(bank_id)
    name = input("Enter Bank Name: ")
    public = input("Select 1 - public, 0 - private: ")
    exchange = input("Enter Listing Exchange: ")
    ceo = input("Enter CEO Name: ")
    coo = input("Enter COO Name: ")
    cfo = input("Enter CFO Name: ")
    address = input("Enter Bank Address: ")
    return bank_id, name, public, exchange, ceo, coo, cfo, address


def bank_selection():
    # retrieve all bank records from database as a data frame
    banks = get_bank_info()

    # display the bank id and bank name
    for index in banks.index:
        print(banks['bank_id'][index] + " - " + banks['name'][index])
    bank_id = input("Enter your Bank's ID from the list above: ")

    # find details of the bank id selected by the user as a dictionary
    banks.query('bank_id == @bank_id', inplace=True)
    invalid_bank = True
    bank_dict = {}
    if not banks.empty:
        bank_list = banks.to_dict('records')  # bank record as a list result in dict format
        bank_dict = bank_list[0]  # convert list into dictionary object
        invalid_bank = False
    return bank_dict, invalid_bank


def add_branch_menu():
    bank_dict, invalid_selection = bank_selection()
    if not invalid_selection:
        # collect branch details and add to bank_dict
        branch_id = random.choice(range(1000, 10000))
        branch_id = "branch" + str(branch_id)
        location = input("Enter Branch Location: ")
        phone = input("Enter Branch Ph: ")
        br_address = input("Enter Branch Address: ")
        bank_dict['branch_id'] = branch_id
        bank_dict['location'] = location
        bank_dict['phone'] = phone
        bank_dict['br_address'] = br_address
        return invalid_selection, bank_dict
    else:
        invalid_selection = True
        return invalid_selection, bank_dict


def add_user_menu():
    user_dict, invalid_selection = bank_selection()

    if not invalid_selection:
        # collect user details and add to user dict
        user_id = random.choice(range(1000, 10000))
        user_id = "U" + str(user_id)
        password = input("Enter initial password: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        birth_date = input("Enter birth date: ")
        address = input("Enter address: ")
        user_type = input("Enter user type (C - Customer, E - Employee): ")
        user_status = "A"
        user_dict['user_id'] = user_id
        user_dict['password'] = password
        user_dict['first_name'] = first_name
        user_dict['last_name'] = last_name
        user_dict['birth_date'] = birth_date
        user_dict['address'] = address
        user_dict['user_type'] = user_type
        user_dict['user_status'] = user_status
        return invalid_selection, user_dict
    else:
        return invalid_selection, user_dict

    # if not banks.empty:
    #     bank_list = banks.to_dict('records')  # bank record as a list result in dict format
    #     bank_dict = bank_list[0]  # convert list into dictionary object


def add_employee_menu(sub_menu):
    print("Enter your bank: ")
    user_dict, invalid_selection = bank_selection()
    emp_dict = {}
    if not invalid_selection:
        users = get_user_info(user_dict['bank_id'])
        user_id = input("Enter the user id for on-boarding: ")
        invalid_user_selection = check_user(user_id)
        selected_user_dict = {}
        if not invalid_user_selection:
            users.query('user_id == @user_id', inplace=True)
            if not users.empty:
                selected_user_list = users.to_dict('records')
                selected_user_dict = selected_user_list[0]
            if sub_menu == 1:  # Employee
                get_branch_id(user_dict['bank_id'])
                branch_id = input("Assign employee's branch: ")
                emp_id = random.choice(range(1000, 10000))
                emp_id = "E" + str(emp_id)
            else:
                emp_id = ""
                branch_id = ""
            emp_dict['password'] = selected_user_dict['password']
            emp_dict['first_name'] = selected_user_dict['first_name']
            emp_dict['last_name'] = selected_user_dict['last_name']
            emp_dict['birth_date'] = selected_user_dict['birth_date']
            emp_dict['address'] = selected_user_dict['address']
            emp_dict['user_type'] = selected_user_dict['user_type']
            emp_dict['user_status'] = selected_user_dict['user_status']
            emp_dict['emp_id'] = emp_id
            customer_id = ""
            ssn = ""
            govt_id = ""
            if sub_menu == 1:  # Employee
                emp_dict['dept'] = input("Enter Employee Dept: ")
                emp_dict['title'] = input("Enter Employee's Title: ")
                emp_dict['start_date'] = input("Enter Employee Start Date: ")
                emp_dict['salary'] = input("Enter Employee's Salary: ")
            elif sub_menu == 2:  # Customer
                customer_id = random.choice(range(1000, 10000))
                customer_id = "C" + str(customer_id)
                ssn = input("Enter SSN: ")
                govt_id = input("Enter Driver's License#: ")
            emp_dict['user_id'] = user_id
            emp_dict['branch_id'] = branch_id
            emp_dict['customer_id'] = customer_id
            emp_dict['ssn'] = ssn
            emp_dict['govt_id'] = govt_id
            return invalid_user_selection, emp_dict
        else:
            return invalid_user_selection, emp_dict
    else:
        return invalid_selection, emp_dict


def open_account_menu():
    # display list of customers:
    get_customer_list()
    # collect account info:
    customer_id = input("Select Customer ID: ")
    ac_num = random.choice(range(1000, 10000))
    ac_num = "A" + str(ac_num)
    ac_type = input("Enter Account Type: C - Checking, S - Savings: ")
    today = date.today()
    today = today.strftime("%m/%d/%y")
    open_date = today
    close_date = ""
    balance = input("Enter initial deposit amount: ")
    status = "A"
    acc_dict = {'ac_num': ac_num, 'ac_type': ac_type, 'open_date': open_date, 'close_date': close_date,
                'balance': balance, 'status': status, 'customer_id': customer_id}
    tran_dict = build_txn(today, balance, ac_num)
    return acc_dict, tran_dict


def build_txn(today, balance, ac_num):
    # build transaction data:
    tran_id = random.choice(range(1000, 10000))
    tran_id = "A" + str(tran_id)
    tran_date = today
    post_date = today
    amount = balance
    merchant_cat = "Customer Initiated"
    tran_type = "CREDIT"
    description = "Customer Deposit"
    if int(balance) < 0:
        tran_type = "DEBIT"
        description = "Customer Withdrawal"
    tran_dict = {'tran_id': tran_id, 'tran_date': tran_date, 'post_date': post_date, 'amount': amount,
                 'merchant_cat': merchant_cat, 'tran_type': tran_type, 'description': description, 'ac_num': ac_num}
    return tran_dict


def deposit_menu():
    get_accounts()
    ac_num = input("Enter Account Number: ")
    amount = input("Enter the Deposit Amount: ")
    account_dict = get_account(ac_num)
    return account_dict, amount




