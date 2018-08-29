l=[]
for letter in 'Word':
    l.append(letter)
print(l)
w=tuple(l)
print(w)
# With list comprehension        similar to maths x: x belongs to R+
l=[letter for letter in 'Hello World']
print(l)

l2=[x**2 for x in range(1,11)]
print(l2)

l3=[number for number in range(11) if number%2==0].sum()
print("l3 is equal to:",l3)

#nesting list comprehension

l4=[ (num**3) for num in   [numb**2 for numb in range(11) ]]
print(l4)

#create list that are divisible by 3 in 1 to 50
li=[num for num in range(1,51) if num%3==0]
print(li)

