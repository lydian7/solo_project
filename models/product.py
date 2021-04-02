class Product:
    def __init__(self, name, description, quantity, purchase_price, selling_price, manufacturer, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.id = id
