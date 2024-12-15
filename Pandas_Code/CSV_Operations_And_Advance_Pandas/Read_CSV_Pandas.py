import pandas as pd

# Load the CSV file into a DataFrame (default settings)
# csv_1 = pd.read_csv("Test_new_CSV.csv")
# print(csv_1)

# Returns only the first `nrows` rows of the CSV file
# csv_2 = pd.read_csv("Test_new_CSV.csv", nrows=3)
# print(csv_2)

# Loads only the specified columns (by index) using `usecols`
# csv_3 = pd.read_csv("Test_new_CSV.csv", usecols=[1, 2])
# print(csv_3)

# Skips the specified rows (row indices to skip) while reading the file
# csv_4 = pd.read_csv("Test_new_CSV.csv", skiprows=[1])
# print(csv_4)

# Uses a specific column as the index of the DataFrame
# csv_1 = pd.read_csv("Test_new_CSV.csv", index_col=0)
# print(csv_1)

# Uses the specified row (given by the `header` argument) as the column headers
# csv_1 = pd.read_csv("Test_new_CSV.csv", header=2)
# print(csv_1)

# Assigns custom column names to the DataFrame, ignoring the existing ones
# csv_1 = pd.read_csv("Test_new_CSV.csv", names=["Col1", "Col2", "Col3", "Col4"])
# print(csv_1)

# Converts the data in specified columns to a defined datatype (e.g., float, int, etc.)
# csv_1 = pd.read_csv("Test_new_CSV.csv", dtype={"A": "float"})
# print(csv_1)
