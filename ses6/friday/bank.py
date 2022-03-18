class Bank:
    def __init__(self):
        self.accounts = []

class Account:
    def __init__(self, accno, cust):
        self.accno = accno
        self.cust = cust

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'The account has a account number of {self.accno}'

class Custormer:
    def __init__(self, name):
        self.name = name
