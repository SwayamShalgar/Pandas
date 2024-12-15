import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
csv_1 = pd.read_csv("Test_new_CSV2.csv")
print("Original DataFrame:")
print(csv_1)

# Add a new row with actual NaN values (use np.nan to represent missing data)
new_row = {"1": np.nan, "2": np.nan, "3": np.nan, "4": np.nan}  # Ensure keys match column names
csv_1.loc[len(csv_1)] = new_row  # Append the new row at the end of the DataFrame
# Print the DataFrame after adding the new row
print("\nDataFrame after adding a new row:")
print(csv_1)

# Uncomment the following blocks to explore various ways of handling NaN values in the DataFrame:

# # Drop rows with any NaN values
# print("\nDataFrame after dropping rows with any NaN values (axis=0):")
# print(csv_1.dropna(axis=0))  # Removes any row with at least one NaN value

# # Drop columns with any NaN values
# print("\nDataFrame after dropping columns with any NaN values (axis=1):")
# print(csv_1.dropna(axis=1))  # Removes any column with at least one NaN value

# # Drop rows where all values are NaN
# print("\nDataFrame after dropping rows where all values are NaN:")
# print(csv_1.dropna(how="all"))  # Removes rows where **all** values are NaN

# # Drop rows where a specific column ('3') contains NaN
# print("\nDataFrame after dropping rows where column '3' contains NaN:")
# print(csv_1.dropna(subset=['3']))  # Removes rows where column '3' has NaN values

# # Permanently remove rows with any NaN values in the DataFrame
# csv_1.dropna(inplace=True)  # Inplace=True modifies the DataFrame directly
# print("\nDataFrame after permanently dropping rows with any NaN values:")
# print(csv_1)

# # Keep rows that have at least 3 non-NaN values
# print("\nDataFrame after keeping rows with at least 3 non-NaN values:")
# print(csv_1.dropna(thresh=3))  # Retains rows with at least `thresh` non-NaN values

# Fill NaN values with a specified value or mapping:
# Replace all NaN values with the string "Hi"
# print("\nDataFrame after filling NaN values with 'Hi':")
# print(csv_1.fillna("Hi"))

# Fill NaN values with different values for specific columns
# print("\nDataFrame after filling NaN values with different values for columns:")
# print(csv_1.fillna({"1": "Hi", "2": "Hello"}))

# Forward fill (propagate the last valid value forward row-wise)
# print("\nDataFrame after forward filling NaN values (row-wise):")
# print(csv_1.ffill(axis=0))

# Backward fill (propagate the next valid value backward column-wise)
# print("\nDataFrame after backward filling NaN values (column-wise):")
# print(csv_1.bfill(axis=1))

# Fill a limited number of NaN values with a specified value
print("\nDataFrame after filling a limited number of NaN values (limit=2) with 'Hi':")
print(csv_1.fillna("Hi", limit=2))  # Replace up to 2 NaN values with 'Hi'
