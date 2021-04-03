from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.branch_repository as branch_repository
import repositories.manufacturer_repository as manufacturer_repository

branches_blueprint = Blueprint("branches", __name__)

# @branches_blueprint.route("/branches")
# def login():
#     branches = branch_repository.select_all()
#     return render_template("branches/login.html", branches = branches)

@branches_blueprint.route("/branches", methods = ["POST"])
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
        return render_template("branches/branch.html", inventory = inventory, branch = branch, manufacturers = manufacturers)
    else:
        return redirect("/login")    

@branches_blueprint.route("/branches/<id>")
def branch(id):
    branch = branch_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("branches/branch.html", branch = branch)        

