import pdb
from datetime import datetime
from models.merchant import Merchant
from models.spend_type import Spend_type
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.spend_type_repository as spend_type_repository
import repositories.transaction_repository as transaction_repository

# Delete lines should go here. Check if requrired. 
# If there are issues here it might be from the order of these. 
merchant1 = Merchant("Little Ceasers Pizza")
merchant_repository.save(merchant1)
merchant2 = Merchant("Subway")
merchant_repository.save(merchant2)
merchant3 = Merchant("Scottish Gas")
merchant_repository.save(merchant3)

# This is a comment to separate out the lines because frankly it looks a wee bit ugulay

transaction1 = Transaction("A lovely cheese pizza, just for me", 13.40, datetime(2021,12,7))
transaction_repository.save(transaction1)
transaction2 = Transaction("Subway", 12.00, datetime(2022,7,7))
transaction_repository.save(transaction2)
transaction3 = Transaction("Electric bills for the month", 430.50, datetime(2022,7,1))
transaction_repository.save(transaction3)

# There is a select all here. Add at later date if required. 


pdb.set_trace()
