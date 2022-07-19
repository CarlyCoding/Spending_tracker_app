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
    return render_template("pages/transactions.html", all_transactions = transactions)


# GET 'transactions/new'
@transactions_blueprint.route("/transactions/new", methods =['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", all_merchants = merchants)
# Think this might be wrong change later


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
# more crap here

# DELETE 
# DELETE '/tasks/<id>'
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')
