#creating string as iterator ,string is itearble but it is not iterator

s="Hello World"

# next(s) will give error that str is not an iterator
# to convert objects that are iterable into iterators themselves!

s_iter=iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


