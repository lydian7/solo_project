from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.branch_repository as branch_repository
import repositories.manufacturer_repository as manufacturer_repository

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/home")
def menu():
    manufacturers = manufacturer_repository.select_all()
    branches = branch_repository.select_all()
    return render_template("home.html", branches = branches, manufacturers = manufacturers)

@home_blueprint.route("/login")
def login():
    branches = branch_repository.select_all()
    return render_template("login.html", branches = branches)

@home_blueprint.route("/ms")
def exit():
    return render_template("ms.html")
