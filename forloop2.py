li=[(1,2,3),(4,5,6),(7,8,9)]

for l in li:
    for s in l:
        print(s)

print('\n')

for t1,t2,t3 in li:
    print(t1,t2,t3) 

print("for loop in dictionary:")

dic={'k1':12,'k2':13,'k3':14}

for d in dic:
    print(d)

#dic.items returns a list of tuples as keys and values in one tuple
for k,v in dic.items():  # or for(k,v) in dic.items():
    print(k)
    print(v)