# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from Bank import Bank
from Bank import view_bank_records
from Menu import add_bank_menu, add_branch_menu, add_user_menu, bank_selection
from Menu import add_employee_menu, open_account_menu, deposit_menu, build_txn
from Branch import Branch
from Branch import get_branch_info
from User import User, get_user_info
from Employee import Employee
from Customer import Customer
from Account import Account, get_accounts
from Transaction import Transaction
from datetime import date
import logging
from Banklog import bank_log

"""
Banking Application - Main Program.
This file contains the main menu for the application. 
The various menu functions are invoked from this file. 
"""

logger = bank_log('MyBank.log', logging.getLogger(__name__))


def main_menu():
    print("Bank Menu")
    print("1 - Bank Admin")
    print("2 - Customer")
    print("0 - Exit")
    menu_selected = input("Enter your selection: ")
    try:
        if int(menu_selected) == 0:
            print("You have successfully logged out.")
            exit(0)
        elif int(menu_selected) == 1:
            bank_admin_menu()
        elif int(menu_selected) == 2:
            customer_menu()
        else:
            print("Invalid Selection.")
            main_menu()
    except ValueError:
        logger.error("Error: Invalid Menu Selection")
        print("Invalid Menu Selection..")
        main_menu()


def bank_admin_menu():
    print("1 - Add New Bank")
    print("2 - List Banks")
    print("3 - Add New Branch")
    print("4 - List Branches")
    print("5 - Add User")
    print("6 - List Users")
    print("7 - On-board Employee/Customer")
    print("0 - Main Menu")
    try:
        menu_selected = input("Enter your selection: ")
        if int(menu_selected) == 1:
            bank_id, name, public, exchange, ceo, coo, cfo, address = add_bank_menu()
            bank = Bank(bank_id, name, public, exchange, ceo, coo, cfo, address)
            bank.add_bank_record()
            print("Successfully created new Bank.")
            input("Press Enter to return to the Main Menu.. ")
            main_menu()
        elif int(menu_selected) == 2:
            view_bank_records()
            input("Press Enter to return to the Main Menu.. ")
            main_menu()
        elif int(menu_selected) == 3:
            invalid_selection, bank_dict = add_branch_menu()
            if not invalid_selection:
                branch = Branch(bank_dict['bank_id'], bank_dict['name'], bank_dict['public'], bank_dict['exchange'],
                                bank_dict['ceo'], bank_dict['coo'], bank_dict['cfo'], bank_dict['address'],
                                bank_dict['branch_id'], bank_dict['location'], bank_dict['phone'],
                                bank_dict['br_address'])
                branch.add_branch_record()
                print("Successfully created new Branch.")
                input("Press Enter to return to the Main Menu.. ")
                main_menu()
            else:
                input("Invalid Selection. Press Enter to return to the Main Menu.. ")
                main_menu()
        elif int(menu_selected) == 4:
            get_branch_info()
            input("Press Enter to return to the Main Menu.. ")
            main_menu()
        elif int(menu_selected) == 5:
            invalid_selection, user_dict = add_user_menu()
            if not invalid_selection:
                bank = Bank(user_dict['bank_id'], user_dict['name'], user_dict['public'], user_dict['exchange'],
                            user_dict['ceo'], user_dict['coo'], user_dict['cfo'], user_dict['address'])
                user = User(user_dict['user_id'], user_dict['password'], user_dict['first_name'],
                            user_dict['last_name'],
                            user_dict['birth_date'], user_dict['address'], user_dict['user_type'],
                            user_dict['user_status'])
                user.add_user_record(bank)
                print("Successfully created new User.")
                input("Press Enter to return to the Main Menu.. ")
                main_menu()
            else:
                input("Invalid Selection. Press Enter to return to the Main Menu.. ")
                main_menu()
        elif int(menu_selected) == 6:
            bank_dict, invalid_selection = bank_selection()
            if not invalid_selection:
                users = get_user_info(bank_dict['bank_id'])
                input("Press Enter to return to the Main Menu.. ")
                main_menu()
            else:
                print("Invalid Selection. Please try again.. ")
                input("Press Enter to return to the Main Menu.. ")
                main_menu()
        elif int(menu_selected) == 7:
            sub_menu = int(input("Press 1 for Employee, 2 for Customer: "))
            invalid_selection, emp_dict = add_employee_menu(sub_menu)
            if invalid_selection:
                print("Invalid Selection. Please try again.. ")
                input("Press Enter to return to the Main Menu.. ")
                main_menu()
            else:
                if sub_menu == 1:
                    employee = Employee(emp_dict['user_id'], emp_dict['password'], emp_dict['first_name'],
                                        emp_dict['last_name'], emp_dict['birth_date'], emp_dict['address'],
                                        emp_dict['user_type'], emp_dict['user_status'],
                                        emp_dict['emp_id'], emp_dict['dept'], emp_dict['title'], emp_dict['start_date'],
                                        emp_dict['salary'])
                    employee.add_employee_record(emp_dict['branch_id'])
                    print("Successfully created new Employee.")
                else:
                    customer = Customer(emp_dict['user_id'], emp_dict['password'], emp_dict['first_name'],
                                        emp_dict['last_name'], emp_dict['birth_date'], emp_dict['address'],
                                        emp_dict['user_type'], emp_dict['user_status'],
                                        emp_dict['customer_id'], emp_dict['ssn'], emp_dict['govt_id'])
                    customer.add_customer_record()
                    print("Successfully created new Customer.")
                input("Press Enter to return to the Main Menu.. ")
                main_menu()
        elif int(menu_selected) == 0:
            main_menu()
        else:
            print("Invalid selection.")
            bank_admin_menu()
    except ValueError:
        logger.error("Error: Invalid Menu Selection")
        print("Error: Invalid Menu Selection..")
        bank_admin_menu()


def customer_menu():
    print("1 - Open Account")
    print("2 - List Accounts")
    print("3 - Deposit")
    print("4 - Withdraw")
    print("0 - Main Menu")
    try:
        menu_selected = input("Enter your selection: ")
        if int(menu_selected) == 1:
            acc_dict, tran_dict = open_account_menu()
            account = Account(acc_dict['ac_num'],
                              acc_dict['ac_type'],
                              acc_dict['open_date'],
                              acc_dict['close_date'],
                              acc_dict['balance'],
                              acc_dict['status'], )
            account.add_account_record(acc_dict['customer_id'])
            transaction = Transaction(tran_dict['tran_id'], tran_dict['tran_date'], tran_dict['post_date'],
                                      tran_dict['amount'], tran_dict['merchant_cat'], tran_dict['tran_type'],
                                      tran_dict['description'])
            transaction.add_transaction_record(acc_dict['ac_num'])
            print("Successfully opened new account!")
            print("Successfully completed transaction for: " + str(tran_dict['amount']))
            input("Press Enter to return to main menu..")
            main_menu()
        elif int(menu_selected) == 2:
            get_accounts()
            input_key = input("Press Enter to return to main menu..")
            input_key = str(input_key)
            if input_key.isalpha():
                main_menu()
            else:
                main_menu()
        elif int(menu_selected) == 3:
            account_dict, amount = deposit_menu()
            try:
                account = Account(account_dict['ac_num'], account_dict['ac_type'], account_dict['open_date'],
                                  account_dict['close_date'], account_dict['balance'], account_dict['status'])
                account.deposit(amount)

                today = date.today().strftime("%m/%d/%y")
                tran_dict = build_txn(today, amount, account_dict['ac_num'])
                transaction = Transaction(tran_dict['tran_id'], tran_dict['tran_date'], tran_dict['post_date'],
                                          tran_dict['amount'], tran_dict['merchant_cat'], tran_dict['tran_type'],
                                          tran_dict['description'])
                transaction.add_transaction_record(account_dict['ac_num'])
            except KeyError:
                logger.error("Error: Invalid Account Number.")
                print("Error: Invalid Account Number.")
                main_menu()
            else:
                print("Successfully completed transaction for: " + str(tran_dict['amount']))
                print("Current Account Balance: " + str(account.balance))
                input("Press Enter to return to the Main Menu..")
                main_menu()
        elif int(menu_selected) == 4:
            account_dict, amount = deposit_menu()
            try:
                account = Account(account_dict['ac_num'], account_dict['ac_type'], account_dict['open_date'],
                                  account_dict['close_date'], account_dict['balance'], account_dict['status'])
                account.withdraw(amount)
                today = date.today().strftime("%m/%d/%y")
                tran_dict = build_txn(today, float(amount) * -1, account_dict['ac_num'])
                transaction = Transaction(tran_dict['tran_id'], tran_dict['tran_date'], tran_dict['post_date'],
                                          tran_dict['amount'], tran_dict['merchant_cat'], tran_dict['tran_type'],
                                          tran_dict['description'])
                transaction.add_transaction_record(account_dict['ac_num'])
            except KeyError:
                logger.error("Error: Invalid Account Number.")
                print("Error: Invalid Account Number.")
                main_menu()
            else:
                print("Successfully completed transaction for: " + str(tran_dict['amount']))
                print("Current Account Balance: " + str(account.balance))
                input("Press Enter to return to the Main Menu..")
                main_menu()
        elif int(menu_selected) == 0:
            main_menu()
        else:
            print("Invalid selection.")
            customer_menu()
    except ValueError:
        logger.error("Error: Invalid Menu Selection")
        print("Error: Invalid Menu Selection..")
        customer_menu()


main_menu()
