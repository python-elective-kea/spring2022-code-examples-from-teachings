class S:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return f'This object has 1 attribut {self.name}'

    def __add__(self, other):
        return self.name + other.name



s = S('Claus')
repr(s)
