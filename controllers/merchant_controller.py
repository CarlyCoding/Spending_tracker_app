from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models import merchant
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.type_repository as type_repository

merchants_blueprint = Merchant("merchant", __name__)

merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("pages/merchants.html", all_merchants = merchants)
    
# GET 'merchants/new'
@merchants_blueprint.route("/merchants/new", methods= ['GET'])
def new_merchant():
    # put in the main code about merchants here. 
    return render_template("merchants/new.html", all_merchants = merchants)
# This block needs more work

# CREATE
# POST 'merchants'
@merchants_blueprint.route("/merchants", methods= ['POST'])
def create_transaction():
    name = request.form['name']
    merchant_repository.save(merchant)
    return redirect('/merchants')

# SHOW
# GET '/merchants'
@merchants_blueprint.route('/merchants/<id>', methods= ['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/show.html', merchant = merchant)

# EDIT
# GET '/merchants'
@merchants_blueprint.route("/merchants/<id>/edit", methods = ['GET'])
def merchant_transaction(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant = merchant)
# Potentially insert more here. 

# UPDATE 
# Put something here for updating a merchant
# something something code 

# DELETE 
# For deleting a merchant 
@merchants_blueprint.route("merchants/<id>./delete", methods = ['POST'])
def delete_merchants(id):
    merchant_repository.delete(id)
    return redirect('/merchants')