import pandas as pd

# Create a DataFrame
var = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [9, 8, 7, 6, 5]})
print("Original DataFrame:")
print(var)

# Inserting a new column at a specific position
# The inserted column must have the same length as the DataFrame
var.insert(0, "M", var["A"])  # Insert column "M" (copy of column "A") at position 0
print("\nDataFrame after inserting column 'M':")
print(var)

# Inserting a new column at the end
# This example adds a new column "N", but with a slice of the "A" column (only first 3 values)
var["N"] = var["A"][:3]  # Remaining rows in column "N" will be filled with NaN
print("\nDataFrame after inserting column 'N' with partial data:")
print(var)

# Deleting a column using `pop`
# The `pop` method removes the specified column and also returns it as a Series
var1 = var.pop("M")  # Removes column "M" and assigns it to var1
print("\nDataFrame after using pop to remove column 'M':")
print(var)
print("\nPopped column 'M':")
print(var1)

# Deleting a column using `del`
# The `del` statement removes the specified column in place
del var["A"]  # Deletes column "A"
print("\nDataFrame after deleting column 'A' using del:")
print(var)

# Adding related methods and explanations:
# 1. Adding a constant column:
var["Constant"] = 100  # Adds a new column with the same value in all rows
print("\nDataFrame after adding a constant column:")
print(var)

# 2. Adding a column with calculations:
var["Sum_B_Constant"] = var["B"] + var["Constant"]  # Adds a column as the sum of existing columns
print("\nDataFrame after adding a column with calculations:")
print(var)

# 3. Dropping multiple columns:
var = var.drop(["N", "Constant"], axis=1)  # Removes multiple columns
print("\nDataFrame after dropping multiple columns ('N', 'Constant'):")
print(var)

# 4. Resetting the index:
var = var.reset_index(drop=True)  # Resets the index to start from 0, drops the old index
print("\nDataFrame after resetting the index:")
print(var)

# 5. Renaming columns:
var.rename(columns={"B": "New_B", "Sum_B_Constant": "New_Sum"}, inplace=True)  # Renames columns
print("\nDataFrame after renaming columns:")
print(var)

# 6. Adding a row:
# Create a new row with data for all columns
new_row = {"New_B": 20, "New_Sum": 30}
var.loc[len(var)] = new_row  # Append the new row
print("\nDataFrame after adding a new row:")
print(var)

# 7. Dropping rows:
var = var.drop(0)  # Drops the first row (index 0)
print("\nDataFrame after dropping the first row:")
print(var)

# 8. Filling missing values:
var["New_B"].iloc[3:] = None  # Introduce missing values
var.fillna(0, inplace=True)  # Fills all NaN values with 0
print("\nDataFrame after filling missing values with 0:")
print(var)
