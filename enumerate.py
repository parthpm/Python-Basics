#Enumerate allows you to keep a count as you iterate through an object.
#It does this by returning a tuple in the form (count,element)

li=['a','b','c']

count=0

for item in li:
    print(count)
    print(item)
    count+=1

for count,item in enumerate(li):
    print(count,item)