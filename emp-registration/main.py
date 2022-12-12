from employee import Employee
import employee_dao as ed
import mysql.connector as ms


def save_employee():
    """
    insert into employees(emp_code,firstname,lastname,gender,mail,contact,address,position,
date_of_birth, date_of_joining, country)
values('INEMP000001', 'Sivakumar', 'Revuri',
'Male','srevuri@gmail.com','9876013491', 'Bangalore', 'Software Enginner', date('1996-12-09'), date('2022-12-05'), 'India');
    :return:
    """
    cntry = 'in'
    emp_uid = 1415
    emp_code = (cntry.upper()) + 'EMP' + str(emp_uid).zfill(6)
    print(emp_code)
    employee = Employee()
    employee.set_firstname = emp_code
    print(employee, employee.get_firstname)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    save_employee()
    cur = None
    try:
        cur = ed.get_connection()
        print(cur[0])
    except ms.DatabaseError as err:
        print(err.msg)
