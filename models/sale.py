import repositories.sales_repository as sales_repository

class Sale:
    def __init__(self, quantity, product_id, employee_id, id = None):
        self.quantity = quantity
        self.product_id = product_id
        self.employee_id = employee_id
        self.id = id

    def employee_total(self, employee_id):
        total = 0
        sales = sales_repository.select_all()

        for sale in sales:
            if employee_id == sale.employee_id:
                total += sale.quantity
        
        return total