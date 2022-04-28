def averager(*args):
     sum = 0
     for i in args:
            sum += i
     print(sum/len(args))


def aveger_gen():
    total = 0.0
    count = 0
    avg = None
    while True:
        temp = yield avg
        total += temp
        count += 1
        avg = total/count
