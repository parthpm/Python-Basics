dict1 ={1:'PArth',2:"Manan",3:"Jeet"}
dict2={'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5'}
dict3={'key1':1,2:'value2',"three":3.00,4.0:[1,2,3,4]}

print( "dict1:",dict1)
print("dict2:",dict2)
print("dict3:",dict3)
print(dict1.items())

print("dict1 1st value:",dict1[1]) #by [] operator
print(dict1[1][0])
print(dict1[1][::-1])
print(dict1[1].upper())
print(dict1[1].isalpha())
print(dict1[1].capitalize())
print(dict1[1].split('r'))
print(dict1[1])
print("dict3 3rd value:",dict3['three'])
