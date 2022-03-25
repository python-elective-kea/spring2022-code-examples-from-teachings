# encaptiolattion

class P:

    def __init__(self, name, amount):
        pass

        # self.amount = amount # this has changed into a property

    @property # getter
    def amount(self):
        return self.__amount

    @amount.setter # setter
    def amount(self, x):
        
        self.__amount = x
        
        """
        if amount < 0:
            self.__amount = 0
        elif amount > 1000:
            self.__amount = 1000
        else:
            self.__amount = amount
        """
