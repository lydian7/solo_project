from db.run_sql import run_sql

from models.product import Product

def save(product):
    sql = "INSERT INTO products(name, description, quantity, purchase_price, selling_price, manufacturer_id, branch_id) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [product.name, product.description, product.quantity, product.purchase_price, product.selling_price, product.manufacturer_id, product.branch_id]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)    

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)    

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        product = Product(row['name'], row['description'], row['quantity'], row['purchase_price'], row['selling_price'], row['manufacturer_id'], row['branch_id'], row['id'])
        products.append(product)

    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['description'], result['quantity'], result['purchase_price'], result['selling_price'], result['manufacturer_id'], result['branch_id'], result['id'])

    return product   

def update(product):
    sql = "UPDATE products SET (name, description, quantity, purchase_price, selling_price, manufacturing_id, branch_id) WHERE product.id = %s"
    values = [product.name, product.description, product.quantity, product.purchase_price, product.selling_price, product.manufacturer_id, product.branch_id, product.id]     
    run_sql(sql, values)




