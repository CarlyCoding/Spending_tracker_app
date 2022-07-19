from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models import merchant
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.type_repository as type_repository

# Consider changing this all to the word tags (word change)


types_blueprint = Blueprint("type", __name__)

@types_blueprint.route("/type")
def types():
    types = type_repository.select_all()
    return render_template("pages/types.html", all_types = types)


# GET 'types/new'
@types_blueprint.route("/types/new", methods = ['GET'])
def new_type():
    # Add a line here for something once html working. 
    return render_template("types/new.html")
    # Above add another line for what it's returning. 

# CREATE 
# POST '/types'
@types_blueprint.route("/types", methods = ['POST'])
def create_type():
    name = request.form['name']
    # Possibly require something here from other classes. 
    type_repository.save(type)
    return redirect('/types')

# SHOW
# GET '/transactions'
@types_blueprint.route('/types/<id>', methods=['GET'])
def show_type(id)
    type = type_repository.select(id)
    return render_template('types/show.html', type = type)


# EDIT
# GET '/TASKS/<id>/edit
@types_blueprint.route("/types/<id>/edit", methods= ['GET'])
def edit_type(id):
    # more lines here for other classes if required
    return render_template('types/edit.html', type = type)

# UPDATE 
# Debate whether this one is needed.

# DELETE 
@types_blueprint.route("/types/<id>/delete", methods=['POST'])
def delete_type(id):
    type_repository.delete(id)
    return redirect('/types')

