mylist=[1,"Hello World",22.4,"Parth Maheshwari",5,6,7,8,'p']
print("Printing mylist:",mylist)
print("Lists are mutuable unlike strings:")
print("Length of list is ",len(mylist))

print("mylist before popping:",mylist)
x=mylist.pop() #default will be last element
print("Popped element is:",x," \nMy list after popping:",mylist)
x=mylist.pop(3)
print(mylist)
mylist.remove('Hello World') #removes first occurencew of value passed
print(mylist)
mylist.sort()
print(mylist)
