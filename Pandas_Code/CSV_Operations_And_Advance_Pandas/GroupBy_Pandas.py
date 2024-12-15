import pandas as pd

# Creating a DataFrame with columns 'Name', 'S_1', and 'S_2'
var = pd.DataFrame({
    "Name": ["a", "b", "c", "d", "a", "b", "a", "b", "c", "c"],  # Name column with repeated values
    "S_1": [11, 22, 33, 44, 55, 66, 77, 43, 12, 34],  # Column S_1 contains numerical values
    "S_2": [32, 23, 11, 43, 54, 23, 11, 23, 44, 32]   # Column S_2 contains numerical values
})

print(var)  # Display the original DataFrame

# Grouping the DataFrame by the 'Name' column
var_new = var.groupby("Name")  # Groups rows by unique values in the 'Name' column
print(var_new)  # Prints information about the GroupBy object (not the grouped data itself)

# Uncommenting the following loop would iterate through each group in 'var_new'
# The loop prints the group name (i) and the corresponding DataFrame (j)
# for i, j in var_new:
#     print(i)  # Group name (e.g., 'a', 'b', 'c', etc.)
#     print(j)  # Subset of DataFrame corresponding to the group
#     print()   # Prints a blank line between groups for better readability

# Getting the subset of rows where the 'Name' column is 'a'
print(var_new.get_group("a"))  # Retrieves rows where 'Name' == 'a'

# Aggregating operations on the grouped data:
# 'min()' calculates the minimum value for each column within each group
print(var_new.min())

# 'max()' calculates the maximum value for each column within each group
print(var_new.max())

# 'mean()' calculates the average value for each column within each group
print(var_new.mean())

# Converting the GroupBy object to a list of tuples
# Each tuple contains the group name and the corresponding subset of the DataFrame
li = list(var_new)
print(li)  # Prints the list of tuples
