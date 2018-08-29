#counter

from collections import Counter
list=[1,2,3,4,2,32,32,435,5,32,12,1,32,3112,311,1,1,3]
print(Counter(list))
s='fdfshdsaofpjmapodjpsajspoadu'
print(Counter(s))

#to find no of words appeared in a string
st="the no of the words words are repeated the words are the is of"
words=st.split()
print(Counter(words))

#methods of Counter
c=Counter(words)
print(c.most_common(2))
print(c.values())