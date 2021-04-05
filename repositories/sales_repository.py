from db.run_sql import run_sql

from models.sale import Sale

def save(sales):
    sql = "INSERT INTO sales (quantity, product_id, employee_id) VALUES (%s,%s,%s) returning id"
    values = [sales.quantity, sales.product_id, sales.employee_id]
    results = run_sql(sql, values)
    sales.id = results[0]['id']
    return sales

def select_all():
    sql = "SELECT * FROM sales"
    results = run_sql(sql)

    sales = []

    for row in results:
        sale = Sale(row["quantity"], row["product_id"], row["employee_id"], row["id"])
        sales.append(sale)
        
    return sales        