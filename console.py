import pdb
from datetime import datetime
from models.merchant import Merchant
from models.type import Type
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.type_repository as type_repository

# Delete lines should go here. Check if requrired. 
# If there are issues here it might be from the order of these. 

merchant1 = Merchant("Little Ceasers Pizza")
merchant_repository.save(merchant1)
merchant2 = Merchant("Subway")
merchant_repository.save(merchant2)
merchant3 = Merchant("Scottish Gas")
merchant_repository.save(merchant3)


type1 = Type("Household Bills")
type_repository.save(type1)
type2 = Type("Rent/ Mortgage")
type_repository.save(type2)
type3 = Type("Food/Groceries")
type_repository.save(type3)
type4 = Type("Transportation")
type_repository.save(type4)
type5 = Type("Entertainment")
type_repository.save(type5)
type6 = Type("Subscriptions")
type_repository.save(type6)
type7 = Type("Repayments")
type_repository.save(type7)
type8 = Type("Miscellaneous")
type_repository.save(type8)
all_selected = type_repository.select_all()
print(all_selected)


transaction1 = Transaction("A lovely cheese pizza, just for me", 13.40, datetime(2021,12,7))
transaction_repository.save(transaction1)
transaction2 = Transaction("Subway", 12.00, datetime(2022,7,7))
transaction_repository.save(transaction2)
transaction3 = Transaction("Electric bills for the month", 430.50, datetime(2022,7,1))
transaction_repository.save(transaction3)

# There is a select all here. Add at later date if required. 


pdb.set_trace()

