import pandas as pd

# Creating two DataFrames with some common and different columns
var1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 22, 33, 44]})  # First DataFrame
var2 = pd.DataFrame({"A": [1, 2, 3, 4], "C": [21, 12, 13, 14]})  # Second DataFrame

# Merging var1 and var2 on column 'A' (common column)
print(pd.merge(var1, var2, on="A"))  # Default is an inner join

# Modifying var2 to have a mismatch in column 'A'
var2 = pd.DataFrame({"A": [1, 2, 3, 5], "C": [21, 12, 13, 14]})

# Performing a left join (all rows from var1, matching rows from var2)
print(pd.merge(var1, var2, how="left"))

# Performing a right join (all rows from var2, matching rows from var1)
print(pd.merge(var1, var2, how="right"))

# Performing an outer join (all rows from both DataFrames, missing values filled with NaN)
# The `indicator=True` argument adds a column showing the source of each row ('both', 'left_only', or 'right_only')
print(pd.merge(var1, var2, how="outer", indicator=True))

# Changing var2 to have the same column name ('B') but different data
var2 = pd.DataFrame({"A": [1, 2, 3, 5], "B": [21, 12, 13, 14]})

# Merging DataFrames by index instead of columns
# `suffixes` are added to differentiate overlapping column names
print(pd.merge(var1, var2, left_index=True, right_index=True, suffixes=("name", "id")))

# Concat examples
# Creating two Series
sr1 = pd.Series([1, 2, 3, 4])  # First Series
sr2 = pd.Series([11, 21, 31, 41])  # Second Series

# Concatenating the two Series along the default axis (vertical stacking)
print(pd.concat([sr1, sr2]))

# Concatenating two DataFrames horizontally (column-wise) with `axis=1`
var1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 22, 33, 44]})  # First DataFrame
var2 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [21, 12, 31, 41]})  # Second DataFrame

# Concatenating along axis=1, preserving only matching indices ('inner join')
print(pd.concat([var1, var2], axis=1, join="inner"))

# Concatenating with keys to distinguish DataFrames in a multi-index structure
print(pd.concat([var1, var2], axis=1, keys=['D1', 'D2']))
