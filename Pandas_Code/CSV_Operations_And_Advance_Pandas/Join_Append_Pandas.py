import pandas as pd

# Creating two DataFrames: `var1` and `var2`
var1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]})  # DataFrame with columns 'A' and 'B'
var2 = pd.DataFrame({"C": [10, 20, 30, 40], "D": [11, 22, 33, 44]})  # DataFrame with columns 'C' and 'D'

# Joining `var1` and `var2` along their indices (default join type is 'left')
print(var1.join(var2))  # Combines `var1` and `var2` side-by-side (column-wise) using index alignment

# Changing `var2` to have fewer rows than `var1`
var2 = pd.DataFrame({"C": [10, 20], "D": [11, 22]})

# Joining DataFrames with different index sizes will raise an error unless explicitly handled
# Uncomment the following lines to observe behavior:

# print(var1.join(var2))  # Throws an error due to mismatched indices
# print(var2.join(var1))  # Throws an error as well
# print(var2.join(var1, how="right"))  # Throws an error since `var1` is larger than `var2`

# To handle mismatched sizes, specify join types (`left`, `right`, `outer`, `inner`):
# Note: The `join` method only works for DataFrames with aligned indices, so this won't work in mismatched cases.

# Appending rows of `var2` to `var1`
# `_append()` is used to concatenate rows from one DataFrame to another, ignoring columns mismatch
print(var1._append(var2, ignore_index=True))  # Appends `var2` to `var1` and resets the index
