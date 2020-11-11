# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

import sqlite3

# db = Database("bank.db")
# sql = "select * from bank"
# print(db.query(sql))
# db.commit()
# db.close()


conn = sqlite3.connect("bank.db")
c = conn.cursor()
# c.execute("drop table transactions")


# tran_id = 'T12122'
# tran_date = '12/12/12'
# post_date = '12/12/21/'
# amount = 100
# merchant_cat = 'Customer'
# tran_type = 'Credit'
# description = 'Customer Dep'
# ac_num = 'A11212'
#
# c.execute("insert into transactions values(:tran_id, :tran_date, :post_date, "
#           ":amount, :merchant_cat, :tran_type, :description, :ac_num)",
#           {'tran_id': tran_id, 'tran_date': tran_date, 'post_date': post_date,
#            'amount': amount, 'merchant_cat': merchant_cat, 'tran_type': tran_type,
#            'description': description, 'ac_num': ac_num})

# balance = 200
# ac_number = 'A6000'
# c.execute("UPDATE account SET balance = :balance where ac_num = :ac_num", {'ac_num': ac_number, 'balance': balance})
#
#
# c.execute("select * from account where ac_num = :ac_num", {'ac_num': ac_number})
# print(c.fetchall())


# c.execute("select a.ac_num, a.ac_type, a.open_date, a.balance, a.status, "
#           "u.first_name, u.last_name, u.bank_id from account a, customer c, user u where a.customer_id = "
#           "c.customer_id and c.user_id = u.user_id")
# print(c.fetchall())


# c.execute("select c.customer_id, u.user_id, u.first_name, u.last_name, u.bank_id, u.user_type from customer c, "
#           "user u where c.user_id = u.user_id")
# print(c.fetchall())

# c.execute("select * from account")
# print(c.fetchall())


# c.execute("""CREATE TABLE IF NOT EXISTS bank(
#     bank_id	TEXT PRIMARY KEY,
#     name TEXT NOT NULL,
#     public TEXT NOT NULL,
#     exchange TEXT,
#     ceo	TEXT NOT NULL,
#     coo	TEXT,
#     cfo	TEXT,
#     address	TEXT
#     )""")
#
# c.execute("""CREATE TABLE IF NOT EXISTS branch(
#     branch_id TEXT PRIMARY KEY,
#     location TEXT NOT NULL,
#     phone TEXT NOT NULL,
#     br_address TEXT NOT NULL,
#     bank_id TEXT NOT NULL,
#     FOREIGN KEY (bank_id)
#         REFERENCES bank(bank_id)
#     )""")
#
#
# c.execute("""CREATE TABLE IF NOT EXISTS user(
#     user_id TEXT NOT NULL,
#     password TEXT NOT NULL,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     birth_date TEXT NOT NULL,
#     address TEXT NOT NULL,
#     user_type TEXT NOT NULL,
#     user_status TEXT NOT NULL,
#     bank_id TEXT NOT NULL,
#     FOREIGN KEY (bank_id)
#         REFERENCES bank(bank_id)
#     )""")
#
#
# c.execute("""CREATE TABLE IF NOT EXISTS employee(
#     emp_id	TEXT NOT NULL,
#     dept TEXT  NOT NULL,
#     title TEXT NOT NULL,
#     start_date TEXT NOT NULL,
#     salary REAL NOT NULL,
#     user_id TEXT NOT NULL,
#     branch_id TEXT NOT NULL,
#     FOREIGN KEY (user_id)
#         REFERENCES user(user_id)
#     FOREIGN KEY (branch_id)
#         REFERENCES branch(branch_id)
#     )""")

# c.execute("""CREATE TABLE IF NOT EXISTS customer(
#     customer_id TEXT NOT NULL,
#     ssn	TEXT NOT NULL,
#     govt_id	TEXT NOT NULL,
#     user_id	TEXT NOT NULL,
#     FOREIGN KEY (user_id)
#         REFERENCES user(user_id)
#     )""")
#
# c.execute("""CREATE TABLE IF NOT EXISTS account(
#     ac_num	TEXT NOT NULL,
#     ac_type	TEXT NOT NULL,
#     open_date TEXT NOT NULL,
#     close_date TEXT,
#     balance	REAL NOT NULL,
#     status TEXT NOT NULL,
#     customer_id TEXT NOT NULL,
#     FOREIGN KEY (customer_id)
#         REFERENCES customer(customer_id)
#     )""")
#
#
# c.execute("""CREATE TABLE IF NOT EXISTS transactions(
#     tran_id	TEXT NOT NULL,
#     tran_date TEXT NOT NULL,
#     post_date TEXT NOT NULL,
#     amount REAL NOT NULL,
#     merchant_cat TEXT NOT NULL,
#     tran_type TEXT NOT NULL,
#     description	TEXT NOT NULL,
#     ac_num TEXT NOT NULL,
#     FOREIGN KEY (ac_num)
#         REFERENCES account(ac_num)
#     )""")

# c.execute("SELECT * FROM employees WHERE last = :last", {'last': last})
# c.execute("select name from sqlite_master where type = 'table'")
# print(c.fetchall())

# c.execute("INSERT INTO employees values(:first, :last, :pay)", {'first': emp_2.first,
#                                                                 'last': emp_2.last, 'pay': emp_2.pay})
# exit(0)
# c.execute("drop table branch")


# bank_id = "bank100"
# name = "JP Morgan Chase"
# public = "Yes"
# exchange = "NYSE"
# ceo = "Carly Scarf"
# coo = "John Doe"
# cfo = "Jane Doe"
# address = "123 Montgomery St San Francisco CA 94588"
# c.execute("insert into bank values(:bank_id, :name, :public, :exchange, :ceo, :coo, :cfo, :address)",
#           {'bank_id': bank_id, 'name': name, 'public': public, 'exchange': exchange,
#            'ceo': ceo, 'coo': coo, 'cfo': cfo, 'address': address})

# c.execute("select * from transactions")
# print(c.fetchall())
#
# branch_id = "branch3"
# location = "Milpitas"
# phone = "408-999-1233"
# br_address = "124 South Main St Milpitas CA 95035"
# bank_id = "bank100"
#
# c.execute("insert into branch values(:branch_id, :location, :phone, :br_address, :bank_id)",
#             {'branch_id': branch_id, 'location': location, 'phone': phone, 'br_address': br_address, 'bank_id': bank_id})
#
# c.execute("select * from branch")
# print(c.fetchmany(5))
# c.execute("select count(*) from branch")
# print(c.fetchall())

conn.commit()
conn.close()
