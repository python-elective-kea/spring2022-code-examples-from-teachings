
# private vs public attributes

class P:
   def __init__(self, name, alias):
      self.name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)



class Account:

    def __init__(self, x):
        #self.set_x(x)
        self.__x = x

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x


