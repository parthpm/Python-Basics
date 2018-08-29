#create a genrator that generates squares of numbers upto n:

def sq_gen(n):
    for i in range(n):
        yield i**2


for num in sq_gen(3):
    print(num)

print('\n\n')

#create a genrator that yields n random numbers between high and low number that are inputs

from random import randint

def rand_generator(low ,high,n):
    for i in range(n):
        yield  randint(low,high)

for numb in rand_generator(2,10,5):
    print(numb)