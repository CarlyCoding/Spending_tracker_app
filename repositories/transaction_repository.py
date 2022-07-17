from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.spend_type import Spend_type

# SAVE
def save(transaction):
    sql = "INSERT INTO transactions (_description, _amount, _date) VALUES (%s, %s, %s) RETURNING *"
    values = [transaction._description, transaction._amount, transaction._date]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

# SELECT ALL

# SELECT
# DELETE ALL 
# DELETE
# UPDATE
# TASKS
