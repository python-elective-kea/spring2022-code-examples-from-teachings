class Car:
    def __init__(self, make):
        self.make = make  # self.make is now a property

    # getter
    @property
    def make(self):
        return self.__make

    # setter
    @make.setter
    def make(self, x):
        if type(x) == str:
            self.__make = x
        else:
            print('WROONG TYPE!!')
