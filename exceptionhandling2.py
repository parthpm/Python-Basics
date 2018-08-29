try:
    print(1/0)
    print('this will be excuted if only no error has occured above')
except ZeroDivisionError:
    print("Caught an exception")
else:
    print('no exception caught')
finally:
    print('we are in finally block it is always executed')

try:
    print('\n\n1')
    print('this will be excuted if only no error has occured above')
except:
    print("Caught an exception")
else:
    print('no exception caught')
finally:
    print('we are in finally block it is always executed')







