from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.branch_repository as branch_repository
from models.product import Product

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def show_all():
    products = product_repository.select_all()
    branches = branch_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/show.html", products = products, manufacturers = manufacturers, branches = branches)

@products_blueprint.route("/products/<id>")
def view(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    branches = branch_repository.select_all()
    return render_template("products/view.html", product = product, manufacturers = manufacturers, branches = branches)

@products_blueprint.route("/products/new")
def new():
    manufacturers = manufacturer_repository.select_all()
    branches = branch_repository.select_all()
    return render_template("products/new.html", branches = branches, manufacturers = manufacturers)

@products_blueprint.route("/products", methods=["POST"])
def add():
    name = request.form['name']
    description = request.form['description']
    quantity = request.form['quantity']
    purchase_price = request.form['purchase_price']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form['manufacturer_id']
    branch_id = request.form['branch_id']
    product = Product(name, description, quantity,purchase_price, selling_price, manufacturer_id, branch_id)
    product_repository.save(product)
    return redirect("/products")

@products_blueprint.route("/products/delete/<id>", methods=["POST"])
def delete(id):
    product_repository.delete(id)
    return redirect("/products")

@products_blueprint.route("/products/<id>/edit", methods=["GET"])
def edit(id):
    product = product_repository.select(id)
    return render_template('products/edit.html', product = product)

@products_blueprint.route("/products/<id>", methods=["POST"])
def update(id):
    name = request.form['name']
    description = request.form['description']
    quantity = request.form['quantity']
    purchase_price = request.form['purchase_price']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form['manufacturer_id']
    branch_id = request.form['branch_id']
    product = Product(name, description, quantity,purchase_price, selling_price, manufacturer_id, branch_id)
    product_repository.update(product)
    return redirect("/products")
