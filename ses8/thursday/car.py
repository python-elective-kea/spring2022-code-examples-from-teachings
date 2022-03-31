class Car:
    def __init__(self, make):
        self.make = make 
   
    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, x):
        if type(x) == str:
            self.__make = x
        else:
            print('NO no no')
