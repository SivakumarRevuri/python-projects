import mysql.connector as ms


def get_connection():
    con = ms.connect(host='localhost', database='sql_practice', username='shiv', password='root')
    cur = con.cursor()
    print("Connection Established Successfully!!!")
    cur.execute('select max(emp_uid) from employees')
    res = cur.fetchone()
    print(res)
    return res
