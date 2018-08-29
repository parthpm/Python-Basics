s="This is Parth Maheshwari"
x="Another string"
z=25.455

print(x," and ",s)
print("This is positional argument example:")
print("{0} is first string and {1} is second string {2} is the third no".format('hi',s,z))
print("{} is first string and {} is second string {:5.2f} is the third no".format('hi',s,z))

print("{x:1.1f} first {y} second {x} third".format(x=25.222,y='hello'))