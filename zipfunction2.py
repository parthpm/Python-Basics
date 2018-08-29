a=[1,2,3,4]
b=[5,6,7,8,9]
c=list(zip(a,b))
print(c)

dic1={'k1':1,'k2':2}
dic2={'k3':3,'k4':4}
print('dic1:',dic1,'dic2',dic2)
z=list(zip(dic1,dic2))
print('Zipping will only zip the keys:',z)

z2=list(zip(dic1.values(),dic2.values()))
print(z2)