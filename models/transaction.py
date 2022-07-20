class Transaction:
    def __init__(self, _description, _amount, _merchant, _spend_type, _id = None):
        self.description = _description
        self.amount = _amount
        self.id = _id
        self.merchant = _merchant
        self.spend_type = _spend_type

