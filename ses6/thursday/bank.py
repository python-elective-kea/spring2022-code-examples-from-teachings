class Bank:
    
    def __init__(self):
        self.accounts = []

class Account:
    def __init__(self, *args):
        self.number = args[0]
        if len(args) > 1:
            self.cust = args[1]


class Custormer:
    
    def __init__(self, name):
        self.name = name


