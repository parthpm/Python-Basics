f=open('filesample2.txt','r')
print(f.readlines()) #f.readlines returns list of strings
f.seek(0)
print(list(f.read()))  #f.read  returns iterator   of characters
for line in open('filesample2.txt'):
    print(line.rstrip())
f.seek(0)

for line in open('filesample2.txt'):
    print(line)