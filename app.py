from flask import Flask, render_template, redirect
from controllers.branch_controller import branches_blueprint
from controllers.product_controller import products_blueprint
from controllers.home_controller import home_blueprint
from models.branch import Branch
import repositories.branch_repository as branch_repository

app = Flask(__name__)

app.register_blueprint(branches_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(home_blueprint)


@app.route('/')
def index():
    return redirect("/home")


if __name__ == '__main__':
    app.run(debug=True)
