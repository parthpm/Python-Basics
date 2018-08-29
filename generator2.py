#generator for fibonacci no

def fibo(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b

print(list(fibo(10)))

for num in fibo(3):
    print(num)

#next function
def sample_gen():
    for i in range(4):
        yield i
p=sample_gen()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
