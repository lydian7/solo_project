from db.run_sql import run_sql

from models.product import Product

def save(product):
    sql = "INSERT INTO products(name, description, quantity, purchase_price, selling_price, manufacturer_id) VALUES (%s,%s,%s,%s,%s, %s) RETURNING id"
    values = [product.name, product.description, product.quantity, product.purchase_price, product.selling_price, product.manufacturer.id]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)    




