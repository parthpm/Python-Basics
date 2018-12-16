#arrays attributes and methods
import numpy as np
arr = np.arange(25)
print(arr.shape)
ranarr = np.random.randint(0,50,10)
print(arr.reshape(5,5))
print(arr.shape)
arr=arr.reshape(1,25)
print(arr)
print(arr.shape)
print(arr.dtype)

# array indexing and selection
arr = np.arange(0,11)
print(arr[0:5])
#broadcasting
sliceofarray=arr[:6]
print(sliceofarray)
sliceofarray[:]=99
print(sliceofarray)
print(arr) #arr changed beacuse of memory optimizations in numpy

#2d array
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
print(arr_2d[1][1],arr_2d[1,1])

print(arr_2d[1:,1:3])

arr=np.zeros((10,10))
print(np.average(ranarr))