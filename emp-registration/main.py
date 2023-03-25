from employee import Employee
import employee_dao as emp_dao
import mysql.connector as ms
from datetime import datetime
from faker import Faker


# collecting emp_info to add the employee
def get_emp_info() -> Employee:
    faker = Faker()
    emp = Employee()
    firstname,lastname = faker.name().split(' ')
    emp.set_firstname(firstname); emp.set_lastname(lastname)
    emp.set_position(faker.random_element(elements={'Assoicate','Developer','Tester', 'Manager', 'Lead'}))
    emp.set_gender(faker.random_element(elements={'male', 'female', 'others'}))
    emp.set_mail(faker.email())
    emp.set_address(faker.city())
    emp.set_dob(faker.date())
    emp.set_doj(datetime.now())
    # emp = Employee(firstname=firstname, lastname=lastname,position= position,gender=gender,mail=mail,
    #                address=address,dob=dob,doj=doj)
    return emp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('''
          we have differnt options with us,
                    get: Fetching employee data
                    add: Adding Employee
                    modify: Updating Employee
                    del: Deleting Employee
          ''')
    
    usr_input = input('Enter your mode of operation: ')
    match usr_input.lower():
        case 'add':
            emp = get_emp_info()
            emp.__str__()
            emp_dao.save_employee(emp)
        case 'get':
            pass
        case 'modify':
            pass
        case 'delete':
            pass
