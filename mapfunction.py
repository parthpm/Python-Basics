def fahrenheit(t):
    return 9/5*t + 32
temp=[0,-40,100]

x=map(fahrenheit,temp)
print(list(x))

#or

y=map(lambda t:9/5*t +32 , temp)
print(list(y))

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]

z=map(lambda x,y,z:x+y+z,a,b,c)
print(list(z))