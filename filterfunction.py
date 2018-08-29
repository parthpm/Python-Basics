#   filter(function name which returns boolean value, iterable)

def evencheck(x):
    if x%2==0:
        return True
    else:
        return False
print(evencheck(10))

p=filter(lambda x:x%2==0,range(1,11))
print(list(p))


# another example to find filter the list which is greater than 3
li=[1,2,4,3,100,2,6,34,6,7,4,6,4]

q=filter(lambda x:x>3,li)
print(list(q))
