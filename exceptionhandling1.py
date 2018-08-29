try:
    f=open('filesample.txt','r')
    f.write('hello')
except:
    print("Exception caught")
else:
    print("No exception")
finally:
    print("It is always executed\n\n")


# 2nd problem
try:
    f=open('filesample.txt','w')
    f.write('hello')
except IOError:
    print("Exception caught")
else:
    print("No exception")
finally:
    print("It is always executed")



