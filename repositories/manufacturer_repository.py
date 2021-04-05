from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

def save(manufacturer):
    sql = "INSERT INTO manufacturers(name, type, address, email, contact_person, telephone, active) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [manufacturer.name, manufacturer.type, manufacturer.address, manufacturer.email, manufacturer.contact_person, manufacturer.telephone, manufacturer.active]
    results = run_sql(sql, values)
    manufacturer.id = results[0]['id']
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)   

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)    

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['type'], row['address'], row['email'], row['contact_person'], row['telephone'], row['active'], row['id'])
        manufacturers.append(manufacturer)

    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['type'], result['address'], result['email'], result['contact_person'], result['telephone'], result['active'], result['id'])

    return manufacturer

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, type, address, email, contact_person, telephone, active) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.type, manufacturer.address, manufacturer.email, manufacturer.contact_person, manufacturer.telephone, manufacturer.active, manufacturer.id]
    run_sql(sql, values)

def manufacturer_inventory(id):
    inventory = []

    sql = "SELECT * FROM products WHERE manufacturer_id = %s"
    values = [id]    
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['description'], row['quantity'], row['purchase_price'], row['selling_price'], row['manufacturer_id'], row['branch_id'], row['id'])
        inventory.append(product)

    return inventory    
            