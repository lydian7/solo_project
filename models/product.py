class Product:
    def __init__(self, name, description, quantity, purchase_price, selling_price, manufacturer_id, branch_id, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.manufacturer_id = manufacturer_id
        self.branch_id = branch_id
        self.id = id
