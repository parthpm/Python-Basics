list=['a','e','z','c','f','b']
print(list)
list.reverse()
print(list)
list.sort()
print(list)
print(''.join(list))

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
m=[l1,l2,l3]
print(m)
print(m[0])
print(m[0][0])

l=[1,2,3,4]
l.append([5,6])
print(l)
l=[1,2,3,4]
l.extend([5,6])
print(l)
l.insert(2,"inserted at index 2")
print(l)

l=['a']*10
print(l)