import repositories.sales_repository as sales_repository

class Sale:
    def __init__(self, product_id, employee_id, branch_id, quantity = 0, id = None):
        self.quantity = quantity
        self.product_id = product_id
        self.employee_id = employee_id
        self.branch_id = branch_id
        self.id = id

