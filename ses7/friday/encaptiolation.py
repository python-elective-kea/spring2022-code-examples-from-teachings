
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
        self.x = x # this is changed into a property

    @property  # getter
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


    """
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    def get_x(self):
        return self.__x

    """
