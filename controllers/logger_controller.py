from flask import Blueprint, Flask, render_template, redirect, request, url_for

import repositories.employee_repository as employee_repository
import repositories.branch_repository as branch_repository
import repositories.sales_repository as sales_repository
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
    sale = Sale(int(quantity), product_id, employee_id)
    sales_repository.save(sale)
    return redirect("/logger")

@logger_blueprint.route("/logger/<id>/view")
def view(id):
    employee_id = int(id)
    employee = employee_repository.select(employee_id)
    employee_sales = employee.total_sales(employee_id) 
    branches = branch_repository.select_all()
    return render_template("logger/view.html", employee = employee, sales = employee_sales, branches = branches)    
    