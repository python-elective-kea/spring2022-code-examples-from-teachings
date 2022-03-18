class Person:
    
    type = 'Mammel'


    def __init__(self, name):
        self.name = name
        # self.type = 'Reptile'


    def __len__(self):
        return 12


    def msg(self):
        return 'Hello'
