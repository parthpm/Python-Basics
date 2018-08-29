'''
Membership Operators:
in and not in are the membership operators in Python. They are used to
test whether a value or variable is found in a sequence (string, list, tuple,
set and dictionary).

'''

#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def fun(li):
    x=[]
    for l in li:
        if l not in x:
            x.append(l)
    return x

li=[1,2,3,2,3,4,56,4,3,5]
print(li)
x=fun(li)
print(x)

#function to check whether a given no is in the range of 2 nos
def fun1(high,low,no):
    return no in range(low,high+1)
print(fun1(2,1,0))