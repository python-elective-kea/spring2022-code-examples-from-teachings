##################################
# Coroutines (generators)
##################################

class Api:
    
    def do_this_first(self):
        pass
    
    def do_this_second(self):
        pass
    
    def do_this_third(self):
        pass


    def run(self):
        self.do_this_first()
        self.do_this_second()
        self.do_this_third()



#############################################
# genrators is perfect for this type of task
#############################################
def api():
    yield 'do_this_first'
    yield 'do_this_second'
    yield 'do_this_third'




####################################################
# Send information back to the coroutine with send()
####################################################

def simple_coroutine():
    print('-> coroutine started')
    x=yield
    print(f'-> coroutine received: {x}')

# exercise 1


