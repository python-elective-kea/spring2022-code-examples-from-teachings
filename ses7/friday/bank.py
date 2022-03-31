class Bank:
     def __init__(self):
        self.__accounts = []
     
     # getter
     @property
     def accounts(self):
         return self.__accounts

     @accounts.setter
     def accounts(self, x):
         if type(x) == Account:
             self.__accounts.append(x)
         elif type(x) == list:
             for i in x:
                 if type(i) == Account:
                    self.__accounts.append(i)
                 else:
                     pass



class Account:
     def __init__(self, no, cust):
        self.no = no
        self.cust = cust

     def __repr__(self):
         return self.no

class Customer:
     def __init__(self, name):
        self.name = name
