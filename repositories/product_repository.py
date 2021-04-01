from db.run_sql import run_sql

from models.product import Product

def save(product):
    sql = "INSERT INTO products(name, description, quantity, purchase_price, selling_price) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values = [product.name, product.description, product.quantity, product.purchase_price, product.selling_price]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product




