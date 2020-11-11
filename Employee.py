# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

from User import User
from Database import Database

"""
Class: Employee
Purpose: Defines the attributes and methods to create the Employee class.
This class is a sub class of User class.
"""


class Employee(User):
    def __init__(self, user_id, password, first_name, last_name, birth_date, address, user_type, user_status,
                 emp_id, dept, title, start_date, salary):
        super().__init__(user_id, password, first_name, last_name, birth_date, address, user_type, user_status)
        self.emp_id = emp_id
        self.dept = dept
        self.title = title
        self.start_date = start_date
        self.salary = salary

    def add_employee_record(self, branch_id):
        db = Database("bank.db")
        db.execute("insert into employee values(:emp_id, :dept, :title, :start_date, :salary, :user_id, :branch_id)",
                   {'emp_id': self.emp_id, 'dept': self.dept, 'title': self.title, 'start_date': self.start_date,
                    'salary': self.salary, 'user_id': self.user_id, 'branch_id': branch_id})
        db.close(commit=True)

    def set_employee_id(self, emp_id):
        self.emp_id = emp_id
        return self.emp_id

    def set_employee_dept(self, dept):
        self.dept = dept
        return self.dept

    def set_employee_title(self, title):
        self.title = title
        return self.title

    def set_employee_start_date(self, start_date):
        self.start_date = start_date
        return self.start_date

    def set_employee_salary(self, salary):
        self.salary = salary
        return self.salary


