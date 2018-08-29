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


def needofdecorator():
    print("Needs an decorator")

needofdecorator=decorator(needofdecorator)

needofdecorator()