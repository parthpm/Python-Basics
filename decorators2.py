# a decorator is a function that takes another function and
# extends the behavior of the latter function without explicitly modifying it.

#Decorators provide a simple syntax for calling higher-order functions.
# function that does at least one of the following:
#----takes one or more functions as arguments (i.e. procedural parameters),
#-----returns a function as its result.


def decorator(func):

    def wrapper():

        print("This will be printed before execution ")

        func()

        print("This will be printed after the execution of function which is going to be decorated ")

    return wrapper

@decorator
def needofdecorator():
    print("Needs an decorator")



needofdecorator()
# practical example of decorator
import time


def timing_function(some_function):
    """
    Outputs the time a function takes
    to execute.
    """
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " +  str((t2 - t1)) + "\n" + str(t1)
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 1000000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())