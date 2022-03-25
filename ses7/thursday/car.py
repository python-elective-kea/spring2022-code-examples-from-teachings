class Car:

    def __init__(self, make, model):
        self.make = make # property
        self.model = model # public variable

    @property  # getter
    def make(self):
        return self.__make

    @make.setter   # setter
    def make(self, value):
        if type(value) == str:
            self.__make = value
        else:
            print('WERONG type')
