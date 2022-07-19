from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.type import Type

# SAVE
def save(transaction):
    sql = "INSERT INTO transactions (description, amount) VALUES (%s, %s) RETURNING *"
    values = [transaction.description, transaction.amount]
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
        transaction = Transaction(row['description'], row['amount'], row['id'] )
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
        transaction = Transaction(result['description'], result['amount'], result['id'] )
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
