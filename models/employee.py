import repositories.sales_repository as sales_repository

class Employee:
    def __init__(self, name, surname, position, branch_id, id = None):
        self.name = name
        self.surname = surname
        self.position = position
        self.branch_id = branch_id 
        self.id = id

    
    # Return total sales quantity per employee by using employee_id
    def total_sales(self, employee_id):
    # Create variable to hold total
        total = 0
    # Get list of sales from sales repository    
        sales = sales_repository.select_all()
    # Iterate through each sale object in list of sales and check if
    # employee_id matches sale.employee_id. If it matches add quantity
    # to total.
        for sale in sales:
            if employee_id == sale.employee_id:
                total += sale.quantity
    # return total    
        return total
    





    

    