###############################################
#f = open('testfiles/bohr.txt', 'r')
#print(f.readline())
#f.close()


################################################
#try:
#    f = open('testfiles/bohr.txt', 'r')
#    print(f.readline())
#finally:
#    f.close()




###############################################
#with open('testfiles/bohr.txt', 'r') as f:
#    print(f.readline())

















###############################################

# with expects a context manager protocol to be followed
# Context manager protocol: __enter__ , __exit__

class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        print('__exit__')
        self.file.close()

















# Exercise 2
