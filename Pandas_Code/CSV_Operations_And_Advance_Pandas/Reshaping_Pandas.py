import pandas as pd

# Creating a DataFrame `var1` with columns 'days', 'eng', and 'maths'
var1 = pd.DataFrame({
    "days": [1, 2, 3, 4, 5, 6],  # Day numbers
    "eng": [12, 12, 14, 17, 12, 18],  # English scores
    "maths": [19, 18, 17, 18, 16, 19]  # Maths scores
})

# Uncomment the following line to display `var1`
# print(var1)

# Using `melt` to reshape the DataFrame `var1` from wide format to long format
# 'id_vars' specifies which column to keep as is ('days' in this case)
# 'var_name' gives the new column name for the reshaped variable (e.g., 'python')
# 'value_name' gives the name for the reshaped values (e.g., 'Swayam')
# Uncomment the line below to see the reshaped DataFrame
# print(pd.melt(var1, id_vars="days", var_name="python", value_name="Swayam"))

# Creating another DataFrame `var2` with additional column 'st_name'
var2 = pd.DataFrame({
    "days": [1, 2, 3, 4, 5, 6],  # Day numbers
    "st_name": ["a", "b", "c", "a", "b", "c"],  # Student names
    "eng": [12, 12, 14, 17, 12, 18],  # English scores
    "maths": [19, 18, 17, 18, 16, 19]  # Maths scores
})

# Using `pivot` to reshape `var2` from long to wide format
# 'index' specifies the rows (here, 'days')
# 'columns' specifies the new columns created from a specific column (here, 'st_name')
# 'values' (optional) specifies which column's values to display in the pivoted DataFrame
print(var2.pivot(index="days", columns="st_name"))  # Default pivot with all values
print(var2.pivot(index="days", columns="st_name", values="eng"))  # Pivot using only 'eng' values

# Using `pivot_table` to summarize and aggregate data
# 'index' specifies the rows (here, 'st_name')
# 'columns' specifies the new columns (here, 'days')
# 'aggfunc' defines the aggregation function (e.g., 'sum', 'mean', etc.)
# 'margins=True' adds an "All" column and row to show overall summaries
print(var2.pivot_table(index="st_name", columns="days", aggfunc="sum", margins=True))
