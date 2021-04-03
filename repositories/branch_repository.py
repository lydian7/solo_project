from db.run_sql import run_sql

from models.branch import Branch
from models.product import Product

def save(branch):
    sql = "INSERT INTO branches(location, manager, password) VALUES (%s,%s, %s) RETURNING id"
    values = [branch.location, branch.manager, branch.password]
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
        branch = Branch(row['location'], row['manager'], row ['password'], row['id'])
        branches.append(branch)

    return branches

def select(id):
    branch = None
    sql = "SELECT * FROM branches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        branch = Branch(result['location'], result['manager'], result ['password'], result['id'])

    return branch    

def branch_inventory(id):
    inventory = []

    sql = "SELECT * FROM products WHERE branch_id = %s"
    
    values = [id]
    results = run_sql(sql, values)        

    for row in results:
        product = Product(row['name'], row['description'], row['quantity'], row['purchase_price'], row['selling_price'], row['manufacturer_id'], row['branch_id'], row['id'])
        inventory.append(product)

    return inventory

# SELECT products.name, products.quantity, manufacturers.name, branches.location, branches.manager FROM ((products INNER JOIN branches ON products.branch_id = branches.id) INNER JOIN manufacturers ON products.manufacturer_id = manufacturers.id) WHERE branches.id = 1;        