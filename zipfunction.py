x=[1,2,3]
y=[4,5,6]
z=[7,8,9]
li=zip(x,y,z)
print(list(li))

#returns iterators therfore casting to list
a=[1,2,3,4,5]
b=[2,2,10,1,1]
print('a = {} b ={}'.format(a,b))
print('zip of a and b', list(zip(a,b)))

# to create a list which includes the largest no in a given index using zip function
z=[]
for pair in list(zip(a,b)):
    z.append(max(pair))
print('Max in a & b',z)

#another way
z2=map(lambda pair:max(pair),zip(a,b))
print(list(z2))


# just to print
for x,y in list(zip(a,b)):
    print(x,y)

