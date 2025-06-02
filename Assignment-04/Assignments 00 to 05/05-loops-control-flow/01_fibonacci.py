

def fib():

    MAX_VALUE = 10000

    a = 0
    b = 1

    while True:
        if MAX_VALUE > a:
           
           print(a, end=' ')

           a, b = b, b + a
        if a >= MAX_VALUE:
            break


fib()
