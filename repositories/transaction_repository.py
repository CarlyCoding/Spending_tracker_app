from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.type import Type

# SAVE
def save(transaction):
    sql = "INSERT INTO transactions (_description, _amount, _date) VALUES (%s, %s, %s) RETURNING *"
    values = [transaction._description, transaction._amount, transaction._date]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

# SELECT ALL
def select_all():
    transactions = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        transaction = Transaction(row['_description'], row['_amount'], row['_date'], row['id'] )
        transactions.append(transaction)
    return transactions

# SELECT
def select(id):
    transaction = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        transaction = Transaction(result['_description'], result['_amount'], result['_date'], result['id'] )
    return transaction

# DELETE ALL 
def delete_all():
    sql = "DELETE * FROM transactions"
    run_sql(sql)
# added the all here, may be source of future errors

# DELETE
def delete(id):
    sql = "DELETE  FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql)
# no star for all here, should be fine as delete with id. Check with testing. 

# UPDATE
def update (transaction):
    sql = "UPDATE transactions SET (_description, _amount, _date) = (%s, %s, %s) WHERE id = %s"
    values = [transaction._description, transaction._amount, transaction._date, transaction._id]
    run_sql(sql, values)
# This might cause errors it's not written very nicely. 

# MERCHANT
