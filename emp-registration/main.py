from employee import Employee
import employee_dao as ed
import mysql.connector as ms


def save_employee():
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
    except ms.DatabaseError as err:
        print(err.msg)
