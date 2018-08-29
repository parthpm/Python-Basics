dict2={'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5'}
dict3={'key1':1,2:'value2',"three":3.00,4.0:[1,2,3,4]}


d={}
print(d)
d["animal"]="Zebra"
print(d)

d1={"k1":{'nestkey':{'subnestkey':'value'} }}
print(d1)
#FOR PRINTING VALUE
print(d1['k1']['nestkey']['subnestkey'].upper())
print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(dict3.pop('key1'))
print(dict3)