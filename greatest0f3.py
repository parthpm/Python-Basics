# Python program to find the largest number among the three input numbers

num1,num2,num3 = input("Enter 3 numbers: ").split()
num1=int(num1)
num2=int(num2)
num3=int(num3)



if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)