from db.run_sql import run_sql

from models.employee import Employee

def save(employee):
    sql = "INSERT INTO employees (name, surname, position, branch_id) VALUES (%s,%s,%s,%s) returning id"
    values = [employee.name, employee.surname, employee.position, employee.branch_id]
    results = run_sql(sql, values)
    employee.id = results[0]['id']
    return employee 


def select_all():
    sql = "SELECT * FROM employees"
    results = run_sql(sql)

    employees = []

    for row in results:
        employee = Employee(row['name'], row['surname'], row['position'], row['branch_id'], row['id'])
        employees.append(employee)
        
    return employees

def select(employee_id):
    sql = "SELECT * FROM employees WHERE id = %s"
    values = [employee_id]
    result = run_sql(sql, values)[0]
    employee = Employee(result['name'], result['surname'], result['position'], result['branch_id'], result['id'])
    return employee

