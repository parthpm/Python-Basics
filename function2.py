#function to check whether a given no is in the range of 2 nos
'''
Membership Operators:
in and not in are the membership operators in Python. They are used to
test whether a value or variable is found in a sequence (string, list, tuple,
set and dictionary).

'''

def fun(high,low,no):
    for number in range(low,high+1):
        if number==no:
            return True
    else:
        return False

x=fun(10,2,11)
print(x)

def fun1(high,low,no):
    return no in range(low,high+1)
print(fun1(2,1,0))