from db.run_sql import run_sql

from models.branch import Branch

def save(branch):
    sql = "INSERT INTO branches(location, manager) VALUES (%s,%s) RETURNING id"
    values = [branch.location, branch.manager]
    results = run_sql(sql, values)
    branch.id = results[0]['id']
    return branch

def delete_all():
    sql = "DELETE FROM branches"
    run_sql(sql)   

def delete(id):
    sql = "DELETE FROM branches WHERE id = %s"
    values = [id]
    run_sql(sql, values)    

def select_all():
    branches = []

    sql = "SELECT * FROM branches"
    results = run_sql(sql)

    for row in results:
        branch = Branch(row['location'], row['manager'], row['id'])
        branches.append(branch)

    return branches

def select(id):
    branch = None
    sql = "SELECT * FROM branches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        branch = Branch(result['location'], result['manager'], result['id'])

    return branch        