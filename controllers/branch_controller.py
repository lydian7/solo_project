from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.branch_repository as branch_repository
import repositories.manufacturer_repository as manufacturer_repository

branches_blueprint = Blueprint("branches", __name__)

@branches_blueprint.route("/branches")
def show():
    branches = branch_repository.select_all()
    return render_template("branches/show.html", branches = branches)

@branches_blueprint.route("/branches/products", methods = ["POST"])
def products():
    id = int(request.form['branch'])
    branch = branch_repository.select(id)
    inventory = branch_repository.branch_inventory(branch.id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("branches/products.html", inventory = inventory, branch = branch, manufacturers = manufacturers)

    

