from flask import Blueprint, Flask, render_template, redirect, request, url_for

import repositories.employee_repository as employee_repository
import repositories.branch_repository as branch_repository
import repositories.sales_repository as sales_repository
import repositories.product_repository as product_repository
from models.sale import Sale
from models.employee import Employee

logger_blueprint = Blueprint("logger", __name__)

@logger_blueprint.route("/logger")
def index():
    employees = employee_repository.select_all()
    return render_template("logger/index.html", employees = employees)

@logger_blueprint.route("/logger/<id>")
def new(id):
    branch_id = int(id)
    inventory = branch_repository.branch_inventory(branch_id)
    employees = employee_repository.select_all()
    return render_template("logger/new.html", branch_id = branch_id, inventory = inventory, employees = employees)

@logger_blueprint.route("/logger/<id>", methods = ["POST"])
def add(id):
    employee_id = request.form["employee_id"]
    product_id = request.form["product_id"]
    quantity = request.form["quantity"]
    product = product_repository.select(product_id)
    stock_check = product.quantity - int(quantity)
    check = False
    branch_sales = sales_repository.sales_by_branch(id)
    for sale in branch_sales:
        if sale.product_id == int(product_id):
            check = True
    if stock_check >= 0:
        # employee = employee_repository.select() 
        branch_id = int(id)
        # sale = sales_repository.sale_by_product(product_id)
        if check:
            sale = sales_repository.sale_by_product(product_id)
            sale_update = Sale(product_id, employee_id, branch_id, quantity, sale.id)
            sales_repository.update(sale_update)
            product.quantity -= int(quantity)
            product_repository.update(product)
            return redirect(url_for("logger.index"))
        else:
            new_sale = Sale(product_id, employee_id, id, quantity)
            sales_repository.save(new_sale)
            return redirect(url_for("logger.index"))    
    else:
        difference = stock_check * -1
        return f"Not enough stock for product, you need to order {difference} more"   


@logger_blueprint.route("/logger/<id>/view")
def view(id):
    employee_id = int(id)
    employee = employee_repository.select(employee_id)
    employee_sales = employee.total_sales(employee_id) 
    branches = branch_repository.select_all()
    return render_template("logger/view.html", employee = employee, sales = employee_sales, branches = branches)    
    