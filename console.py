from datetime import datetime
from models.merchant import Merchant
from models.spend_type import Spend_type
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.spend_type_repository as spend_type_repository
import repositories.transaction_repository as transaction_repository

# Delete lines should go here. Check if requrired. 
# If there are issues here it might be from the order of these. 

transaction1 = Transaction("A lovely cheese pizza, just for me", 13.40, datetime(1990,12,7),)
transaction_repository.save(transaction1)

