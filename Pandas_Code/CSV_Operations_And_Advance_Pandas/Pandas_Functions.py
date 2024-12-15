import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
csv_1 = pd.read_csv("Test_new_CSV1.csv")
print("Original DataFrame:")
print(csv_1)

# 1. Provide index range: Start, end, and steps
# Uncomment to display the index object of the DataFrame
# print("\nIndex range of the DataFrame:")
# print(csv_1.index)

# 2. Provide column names
# Uncomment to display column names
# print("\nColumn names in the DataFrame:")
# print(csv_1.columns)

# 3. Provide statistical summary: mean, max, min, etc.
# Uncomment to display summary statistics for numerical columns
# print("\nStatistical summary of numerical columns in the DataFrame:")
# print(csv_1.describe())

# 4. Returns the first 2 rows
print("\nFirst 2 rows of the DataFrame:")
print(csv_1.head(2))

# 5. Returns the last 2 rows
print("\nLast 2 rows of the DataFrame:")
print(csv_1.tail(2))

# 6. Returns rows through slicing (e.g., first 3 rows)
# Uncomment to display the first 3 rows
# print("\nFirst 3 rows of the DataFrame using slicing:")
# print(csv_1[:3])

# 7. Returns index as an array
# Uncomment to display the index as an array
# print("\nIndex array of the DataFrame:")
# print(csv_1.index.array)

# 8. Return the DataFrame data as a Numpy array
# Uncomment to display the DataFrame as a Numpy array
# print("\nDataFrame data as a Numpy array:")
# print(csv_1.to_numpy())

# Convert the DataFrame to a Numpy array using `np.asarray`
# Uncomment to use numpy's asarray function
# v = np.asarray(csv_1)
# print("\nNumpy array of the DataFrame:")
# print(v)

# 9. Sort the DataFrame by index
# Uncomment to sort rows in descending order by their index
# print("\nDataFrame sorted by index in descending order:")
# print(csv_1.sort_index(axis=0, ascending=False))  # Sort rows by index in descending order

# 10. Modify a specific value in the DataFrame
# Uncomment to set the value of cell at index 0 and column 'A' to 5
# csv_1.loc[0, "A"] = 5
# print("\nModified DataFrame after changing value at index 0, column 'A':")
# print(csv_1)

# 11. Use the `loc` function for label-based selection
# Select rows with indices 2 and 3 and columns 'A' and 'B'
print("\nSelected rows (2, 3) and columns ('A', 'B') using loc:")
print(csv_1.loc[[2, 3], ["A", "B"]])

# Select all rows and specific columns ('A' and 'B')
print("\nAll rows and columns ('A', 'B') using loc:")
print(csv_1.loc[:, ["A", "B"]])

# Select rows with indices 2 and 3 and all columns
print("\nRows (2, 3) and all columns using loc:")
print(csv_1.loc[[2, 3], :])

# 12. Use the `iloc` function for position-based selection
# Uncomment to select the value at the 0th row and 1st column
# print("\nValue at row 0, column 1 using iloc:")
# print(csv_1.iloc[0, 1])

# 13. Drop a column or row using the `drop` function
# Drop column 'A' (axis=1 refers to columns)
# Uncomment to drop column 'A'
# print("\nDataFrame after dropping column 'A':")
# print(csv_1.drop("A", axis=1))

# Drop row with index 1 (axis=0 refers to rows)
# Uncomment to drop row with index 1
# print("\nDataFrame after dropping row with index 1:")
# print(csv_1.drop(1, axis=0))
