from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products/<id>/new")
def new(id):
    return render_template("products/new.html", id = id)

