#Function Definiton
def square1(num):
    square=num**2
    return  square

square2=lambda x1: x1*x1 # can assign to create name
print(lambda x1: x1*x1)

#Calling square as a function
print("Square of number is",square1(10),square2(10))

add=lambda  x,y:x+y
print(add(1,2))