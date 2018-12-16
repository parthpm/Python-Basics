import numpy as np
arr=np.arange(0,11)

#selecting a particular part of
bool_arr=arr>4
print(bool_arr)
print(arr[bool_arr])
print(arr[arr>4])

#arithmetic operations

print(arr+arr)
print(arr**2)
print(arr/arr)
print(1/arr)

#universal array operations
print(np.sqrt(arr))
print(np.max(arr))
print(np.sort(arr,axis=0))


#sum of all columns
arr=np.arange(1,26).reshape(5,5)
print(arr)
print(arr.sum(axis=0))

import tensorflow as tf
