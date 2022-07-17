from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.type import Type

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

    if results:
        result = results[0]
        merchant = Merchant(result['_merchant_name'], result['id'] )
    return merchant

# DELETE ALL 
def delete_all(id):
    sql = "DELETE * FROM merchants"
    run_sql(sql)
# Added the star for delete all

# DELETE
def delete(id):
    sql = "DELETE * FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update(merchant):
    sql = "UPDATE merchants SET (_merchant_name) = (%s) WHERE id = %s"
    values = [merchant._merchant_name, merchant.id]
    run_sql(sql, values)

# May need a def here- run functions first. 
