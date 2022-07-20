from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import transaction
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository 
import repositories.merchant_repository as merchant_repository
import repositories.type_repository as type_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    merchants = merchant_repository.select_all()
    types = type_repository.select_all()
    return render_template("pages/transactions.html", all_transactions = transactions, merchants = merchants, types = types)


# GET 'transactions/new'
@transactions_blueprint.route("/transactions/new", methods =['POST'])
def new_transaction():
    spend_type = request.form["Type"]
    merchant = request.form["Merchant"]
    description = request.form["Description"]
    amount = request.form["Amount"]
    spend_type_object = type_repository.select(spend_type)
    merchant_object = merchant_repository.select(merchant)
    transaction = Transaction(description,amount,merchant_object,spend_type_object)
    transaction_repository.save(transaction)
    return redirect("/transactions")



# CREATE 
# POST '/transactions'
@transactions_blueprint.route("/tasks", methods= ['POST'])
def create_transaction():
    description = request.form['description']
    amount = request.form['amount']
    # Need something here for merchant
    # Need something here for type
    transaction_repository.save(transaction)
    return redirect('/transactions')

# SHOW 
# GET '/transactions
@transactions_blueprint.route('/transactions/<id>', methods=['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/show.html', transaction = transaction)

# EDIT 
# GET '/TASKS/<id>/edit 
@transactions_blueprint.route("/transactions/<id>/edit", methods= ['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    # put in a line here for merchant
    # put in a line here for type
    return render_template('transactions/edit.html', transaction= transaction)
    # INSERT MORE IN RETURN STATEMENT FOR OTHER CLASSES. 

# UPDATE 
# PUT '/tasks/<id>'


# DELETE 
# DELETE '/tasks/<id>'
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')
