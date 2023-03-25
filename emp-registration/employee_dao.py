import mysql.connector as ms
from employee import Employee

def get_connection():
    con = ms.connect(host='localhost', database='sql_practice', username='shiv', password='root')
    print("Connection Established Successfully!!!")
    return con

"""
insert into employees(emp_code,firstname,lastname,gender,mail,contact,address,position,date_of_birth, date_of_joining, country)
values('INEMP000001', 'Sivakumar', 'Revuri',
'Male','srevuri@gmail.com','9876013491', 'Bangalore', 'Software Enginner', date('1996-12-09'), date('2022-12-05'), 'India');
"""
def save_employee(emp: Employee):
    print('Called!!!')