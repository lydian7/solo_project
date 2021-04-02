from flask import Flask, render_template, request, redirect
from flask import Blueprint

branches_blueprint = Blueprint("branches", __name__)

# @branch_blueprint.route("/branches/<id>")
# def index(id):