from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.type import Type
from repositories import merchant_repository, type_repository


# SAVE
def save(transaction):
    sql = "INSERT INTO transactions (description, amount, merchant_id, type_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [transaction.description, transaction.amount, transaction.merchant.id, transaction.spend_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

# SELECT ALL
def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        spend_type_object = type_repository.select(row['type_id'])
        merchant_object = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['description'], row['amount'], merchant_object, spend_type_object, row['id'])
        transactions.append(transaction)
    return transactions

# SELECT
def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        spend_type_object = type_repository.select(result['type_id'])
        merchant_object = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(result['description'], result['amount'], merchant_object, spend_type_object, result['id'] )
    return transaction

# DELETE ALL 
def delete_all():
    sql = "DELETE * FROM transactions"
    run_sql(sql)


# DELETE
def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql)


# UPDATE
def update (transaction):
    sql = "UPDATE transactions SET (description, amount) = (%s, %s) WHERE id = %s"
    values = [transaction.description, transaction.amount, transaction.id]
    run_sql(sql, values)


# MERCHANT
