li=[1323,32,32454,213,323,121,4]
print(max(li))

max_find=lambda x,y: x if x>y else y

from _functools import reduce
p=reduce(max_find,li)
print(p)

import n