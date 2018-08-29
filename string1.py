str=" I am Parth Maheshwari "
print('printing 2nd index:', str[2])
print('printing 2-4 index by slicing operator:',str[2:4]) #starting and ending
print('printing everything upto 10 :',str[:10])
print('printing negative -1 index:', str[-1])
print(str[3:])
print(str[3:8:2])   # starting and ending + step size
print("Reversing the string:",str[::-1])

print(str.upper())
print("Splitting into list till e is found",str.split('e'))

print(str)
#trip() is an inbuilt function in Python programming language that returns a copy of the string with both
#  leading and trailing characters removed (based on the string argument passed).
#by default blank space is stripped
print(str.strip())
#for left lstrip and vicevcersa
print(str.lstrip())
print(str.rstrip())
print(str)
