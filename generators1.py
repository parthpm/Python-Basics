#this is genarator
def gencube(n):
    for num in range(n):
        yield num**3

#this is equivalent function composing of list
def gcube(n):
    li=[]
    for num in range(n):
        li.append(num**3)
    return li

for num in gencube(4):
    print(num)

for num in gcube(4):
    print(num)

print(gcube(5))

#generator expression
#the expression which genrates an genrator is called generator expression

g= (n for n in range(2,4))
print(next(g))
print(next(g))
