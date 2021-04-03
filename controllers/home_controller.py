from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.branch_repository as branch_repository

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/home")
def login():
    return render_template("home.html")