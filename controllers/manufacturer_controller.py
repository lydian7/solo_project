from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.branch_repository as branch_repository
from models.manufacturer import Manufacturer

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route('/manufacturers')
def show():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/show.html', manufacturers = manufacturers)

@manufacturers_blueprint.route('/manufacturers/<id>')
def view(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/view.html', manufacturer = manufacturer)    

@manufacturers_blueprint.route('/manufacturers/new')
def new():
    return render_template("manufacturers/new.html")

@manufacturers_blueprint.route('/manufacturers', methods = ["POST"])
def add():
    name = request.form['name']
    type = request.form['type']
    address = request.form['address']
    email = request.form['email']
    contact_person = request.form['contact_person']
    telephone = request.form['telephone']
    manufacturer = Manufacturer(name, type, address, email, contact_person, telephone)
    manufacturer_repository.save(manufacturer)
    return redirect(url_for('manufacturers.show'))

@manufacturers_blueprint.route('/manufacturers/<id>/edit')
def edit(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/edit.html", manufacturer = manufacturer)   

@manufacturers_blueprint.route('/manufacturers/<id>', methods = ["POST"])
def update(id):
    name = request.form['name']
    type = request.form['type']
    address = request.form['address']
    telephone = request.form['telephone']
    email = request.form['email']
    contact_person = request.form['contact_person']
    active = request.form['active']
    manufacturer = Manufacturer(name, type, address, email, contact_person, telephone, active, id)
    manufacturer_repository.update(manufacturer)
    return redirect(url_for('manufacturers.view', id = id))

@manufacturers_blueprint.route('/manufacturers/delete/<id>', methods = ['POST'])
def delete(id):
    manufacturer_repository.delete(id)
    return redirect(url_for('manufacturers.show'))

@manufacturers_blueprint.route('/manufacturers/products', methods = ['POST'])
def products():
       id = int(request.form['manufacturer'])
       inventory = manufacturer_repository.manufacturer_inventory(id)
       branches = branch_repository.select_all()
       manufacturers = manufacturer_repository.select_all()
       return render_template("manufacturers/products.html", inventory = inventory, branches = branches, manufacturers = manufacturers)
