from db.run_sql import run_sql

from models.sale import Sale

def save(sales):
    sql = "INSERT INTO sales (product_id, employee_id, branch_id, quantity) VALUES (%s,%s,%s, %s) returning id"
    values = [sales.product_id, sales.employee_id, sales.branch_id, sales.quantity]
    results = run_sql(sql, values)
    sales.id = results[0]['id']
    return sales

def update(sale):
    sql = "UPDATE sales SET (product_id, employee_id, branch_id, quantity) = (%s,%s,%s,%s) WHERE id = %s"
    values = [sale.product_id, sale.employee_id, sale.branch_id, sale.quantity, sale.id]
    run_sql(sql, values)  

def select_all():
    sql = "SELECT * FROM sales"
    results = run_sql(sql)

    sales = []

    for row in results:
        sale = Sale(row["product_id"], row["employee_id"], row['branch_id'], row['quantity'], row["id"])
        sales.append(sale)
        
    return sales        

# def sales_by_employee(employee_id):
#     sql = "SELECT sales.*, products.purchase_price, products.selling_price FROM sales INNER JOIN products ON sales.product_id = products.id WHERE employee_id = %s"  
#     values = [employee_id]
#     return run_sql(sql, values)

def sales_by_employee(employee_id):
    sql = "SELECT * FROM sales WHERE employee_id = %s"
    values = [employee_id]
    results = run_sql(sql, values)

    sales = []

    for row in results:
        sale = Sale(row["product_id"], row["employee_id"], row["branch_id"], row["quantity"], row["id"])
        sales.append(sale)
        
    return sales  

def sales_by_branch(id):
    sales = []

    sql = "SELECT * FROM sales WHERE branch_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        sale = Sale(row["product_id"], row["employee_id"], row["branch_id"], row["quantity"], row["id"])
        sales.append(sale)   
        
    return sales

def sale_by_product(id):

    sale = None     

    sql = "SELECT * FROM sales WHERE product_id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        sale = Sale(result["product_id"], result["employee_id"], result["branch_id"], result["quantity"], result["id"])       

    return sale    