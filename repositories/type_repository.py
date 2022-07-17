from db.run_sql import run_sql

from models.merchant import Merchant
from models.transaction import Transaction
from models.type import Type

def save(type):
    sql = "INSERT INTO types ( name ) VALUES ( %s ) RETURNING id"
    values = [type.name]
    results = run_sql( sql, values)
    type.id = results[0]['id']
    return type

def select_all():
    types = []

    sql = "SELECT * FROM types"
    results = run_sql(sql)

    for row in results:
        type = Type(row['name'], ['id'])
        types.append(type)
    return type

def select(id):
    type = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        type = Type(result['name'], result['id'])
    return type

# Enter the inner join relationship here. 

def delete_all():
    sql = "DELETE FROM types"
    run_sql(sql)

    
