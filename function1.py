def is_prime(num):
    ''' INPUT: NO
        Output:prints whether a no is prime nos 
    '''
    for n in range(2,num):
        if num%n==0:
            print("Not Prime")
            break
    else:
        print("No is Prime")

is_prime(2)

print("Default Function:")

def default1(a,b=5):
	return(a*a + b*b)
print("The square of sum :", default1(5))
print("The square of sum :", default1(10,20))
print(is_prime.__dict__)
