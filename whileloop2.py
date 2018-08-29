print("program to find prime nos between 1 to 100")

num=2



while num<=100:
    f = True
    i = 2
    while i<=num/2:
        if num%i==0:
            f=False
            break
        i+=1
    if f==True:
        print(num)
    num+=1
