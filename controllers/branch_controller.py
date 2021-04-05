from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
import repositories.branch_repository as branch_repository
import repositories.manufacturer_repository as manufacturer_repository
from models.branch import Branch

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

@branches_blueprint.route("/branches/<id>")
def view(id):
    branch = branch_repository.select(id)
    return render_template("branches/view.html", branch = branch)    

@branches_blueprint.route("/branches/<id>/edit")
def edit(id):
    branch = branch_repository.select(id)
    return render_template("branches/edit.html", branch = branch)
    
@branches_blueprint.route("/branches/<id>", methods = ["POST"])
def update(id):
    location = request.form["location"]
    manager = request.form["manager"]
    password = branch_repository.select(id).password
    branch = Branch(location, manager, password, id)
    branch_repository.update(branch)
    return redirect(url_for('branches.view', id = id))

@branches_blueprint.route("/branches/delete/<id>", methods = ["POST"])
def delete(id):
    branch_repository.delete(id)
    return redirect(url_for("branches.show"))


@branches_blueprint.route("/branches/new")
def new():
    return render_template("branches/new.html")    

@branches_blueprint.route("/branches", methods = ["POST"])
def add():
    location = request.form["location"]
    manager = request.form["manager"]
    password = request.form["password"]
    branch = Branch(location, manager, password)
    branch_repository.save(branch)
    return redirect(url_for("branches.show"))    