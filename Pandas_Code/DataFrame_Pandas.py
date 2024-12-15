import pandas as pd

l = [1,2,3,4,5,6]

var = pd.DataFrame(l)
print(var)

# both length of the dict key must be same !
d = {
    'a':[1,2,3,4,5],
    'b':[1,2,3,4,5]
}

var1 = pd.DataFrame(d)

# Will give 'a' column
var2 = pd.DataFrame(d,columns=['a'])

print(var1)

print(f"\n{var1['a'][3]}")

# multi-dimentional list
l2 = [[1,2,3,4,5],[6,7,8,9,0]]

var3 = pd.DataFrame(l2)

print(f"\n{var3}")

sr = {
    "S1":  pd.Series([1,2,3,4]),
    "S2": pd.Series([5,6,7,8])
    }

var4 = pd.DataFrame(sr)
print(f"\n{var4}")