from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.spend_type import Spend_type

# SAVE
def save(merchant):
    sql = "INSERT INTO merchants (_merchant_name) VALUES (%s) RETURNING *"
    values = [merchant._merchant_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id 
    return merchant

# SELECT ALL
def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['_merchant_name'], row['id'] )
        merchants.append(merchant)
    return merchants

# SELECT
def select(id):
    merchant = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql
# DELETE ALL 
# DELETE
# UPDATE
# TASKS