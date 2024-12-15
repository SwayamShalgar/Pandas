import pandas as pd

#creating a normal list
l = [1,4,2,3]
d = {
    'name': ['Pyhton','C','Java'],
    'por': [12,32,43,12],
    'rank': [1,2,4,3]
}

#Creating a series Pandas Data Structures

var = pd.Series(l)
print(var)

# some modifications
var = pd.Series(l, index=['a','b','c','d'],dtype='float',name='python')
print(var)

var1 = pd.Series(d)
print(var1)

s = pd.Series(12,index=[1,2,3,4,5,6,7,8])
print(s)

s1 = pd.Series(12,index=[1,2,3,4])
s2 = pd.Series(12,index=[1,2,3,4,5,6,7])

print(s1+s2)