
books =[1,2,3,4,5,6,7,8,9,10]
books2=[1,2,3,4,5,6,7,8,9,10]
# print(books*books2)
print (books[:])
print(type(books[:]))
print(books)
print(books[1])
print(type(books))
print("Printing second indexed element:",books[2])
print("Printing index of value 3",books.index(3))
print(books[:6])  #excluding 6 index
print(books[2:])
books[5]=50 #Mutability of list
print(books)
print("Books*2 =",books*2)
print("No of otimes 2 occurs in list:",books.count(2))

print("Concatenation of Lists:")
print("Intially books contain",books,"\nAfter concatenation:")


b1=books+[11,12,13]
print(b1)

books.append("Append me!")
print(books)

b1[:10]=[] #blank element till 10th index of list
print(b1)

books[1:]=[] #all blank except 0
print(books)
del books