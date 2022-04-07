class Car:

    def __init__(self, make):
        self.make = make 
  
    @property # getter
    def make(self):
        return self.__make

    @make.setter
    def make(self, x):
        self.__make = x


    def info(self):
        return f'The variable of this class is {self.__dict__}'
