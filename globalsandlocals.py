s='this is a global variable'

def fun():
    print(locals())

print(globals())  #a dictionary with all global names as keys and values as values of dictionary
print('\n\n')
print(globals()['s'])
fun()
print('\n\n')

