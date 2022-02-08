# Strongly typed language
# Dynamicly typed
a = 'Hello world 33'
print(   type(a)   )
#a = 12
print(   a.upper() )

print( len(a))

#len = 67

#pint( len(a) )

def foo():
    return 1+1


class A:
    def __len__(self):
        return 6


a = A()

print( len(a) )





# len() -> __len__()
# Person() -> __init__
# + -> __add__()
# * -> __mul__()
# () -> __call__()



