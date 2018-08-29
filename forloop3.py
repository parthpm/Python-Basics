st='Print only the words that start with s in this sentence'
for word in  st.split():
    if(word[0]=='s'):
        print(word )


st='Print only the words that start with s in this sentence'
for s in  st.split(' '):
    if(len(s)%2==0):
        print(s+' length is even')



