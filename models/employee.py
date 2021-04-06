import repositories.sales_repository as sales_repository

class Employee:
    def __init__(self, name, surname, position, branch_id, id = None):
        self.name = name
        self.surname = surname
        self.position = position
        self.branch_id = branch_id 
        self.id = id

    def total_sales(self, employee_id):
        total = 0
        sales = sales_repository.select_all()

        for sale in sales:
            if employee_id == sale.employee_id:
                total += sale.quantity
        
        return total

    # def total_revenue(self, employee_id):
    #     total = 0


    