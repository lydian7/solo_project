from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.branch_repository as branch_repository
from models.manufacturer import Manufacturer

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route('/manufacturers')
def show():
    return render_template('manufacturers/show.html')