#NUMPY Arrays
import numpy as np
list=[1,2,3]
arr=np.array(list)
print(arr)


matrix=[[1,2,3],[4,5,6]]
mat=np.array(matrix)
print(mat.shape)
print(type(mat))

# arrange same range
x=np.arange(0,11)
print(x)

p=np.zeros(2)
q=np.zeros((2,3))
print(p)
print(q)

#linspace for equaly spaced n numbers between 2 nos
s=np.linspace(0,100,7)
print(s)

a=np.eye(3) #
print(a)# identity matrix
a=np.random.rand(2) #random
print(a)
a=np.random.rand(3,3)
print(a)
a=np.random.rand(3,3,3)
print(a)
x=np.random.randint(2,5,4)
print(x)

