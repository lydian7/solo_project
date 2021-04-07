from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
import repositories.branch_repository as branch_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.employee_repository as employee_repository
import repositories.sales_repository as sales_repository
import repositories.product_repository as product_repository
from models.sale import Sale

dashboard_blueprint = Blueprint("dashboard", __name__)

# @dashboard_blueprint.route('/dashboard')
# def login():
#     branches = branch_repository.select_all()
#     return render_template("dashboard/login.html", branches = branches)

@dashboard_blueprint.route("/dashboard", methods = ["POST"])
def index():
    # branches = branch_repository.select_all()
    id = int(request.form['location'])
    branch = branch_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    password = request.form['password']
    # branch = None
    inventory = None
    # for br in branches:
    #     if br.manager == manager:
    #         branch = br   

    if password == str(branch.password):
        inventory = branch_repository.branch_inventory(branch.id)
        employees = employee_repository.select_all()
        sales = sales_repository.sales_by_branch(id)
        return render_template("dashboard/dash.html", inventory = inventory, branch = branch, manufacturers = manufacturers, employees = employees, branch_id = id, sales = sales)
    else:
        return redirect("/login")    

@dashboard_blueprint.route("/dashboard/sales", methods = ["POST"])
def add_sale():
    quantity = request.form['quantity']
    product_id = request.form['product_id']
    employee_id = request.form['employee_id']
    product = product_repository.select(product_id)
    stock_check = product.quantity - int(quantity)
    if stock_check >= 0: 
        branch = branch_repository.get_branch_by_employee(employee_id)
        sale = sales_repository.sale_by_product(product_id)
        sale_update = Sale(product_id, employee_id, branch.id, quantity, sale.id)
        sales_repository.update(sale_update)
        return redirect(url_for("dashboard.index", ))
    else:
        difference = stock_check * -1
        print(f"Not enough stock for product, you need to order {difference} more")    
