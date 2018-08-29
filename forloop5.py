#fibonacci series

n=input("Enter the numbers in Fibonacci Series:")
n=int(n)

if n==1:
    print('0')
elif n==2:
    print('0\n1')
else:
    a=0
    b=1
    c=1
    count=3
    print('0\n1')
    while count<=n:
        print(c)
        a=b
        b=c
        c=a+b
        count+=1