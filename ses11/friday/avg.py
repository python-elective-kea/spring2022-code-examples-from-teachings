def averager(*args):
     sum = 0
     for i in args:
            sum += i
     print(sum/len(args))

def avg():
    total = 0.0
    count = 0
    average = 0
    
    while True:
        temp = yield average
        total += temp
        count += 1
        average = total/count


def x():
    x = yield 12
    y = yiekd
