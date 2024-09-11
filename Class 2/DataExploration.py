# Install required packages
# Run this in the terminal if pandas is not installed: pip install pandas

import pandas as pd

# Load the Titanic dataset (make sure to provide the correct path to your CSV file)
df = pd.read_csv('titanic (1).csv')
print(df)

# Display the first 5 rows of the dataset
print(df.head(5))

# Display the last 3 rows of the dataset
print(df.tail(3))

# Display basic statistical descriptions of the dataset
print(df.describe())

# Display dataset information (columns, types, etc.)
print(df.info())

# Shape of the dataset
print(f'Dataset Shape: {df.shape}')

# Column names of the dataset
print(f'Column Names: {df.columns}')

# Check for missing values in each column
print(f'Missing Values:\n{df.isnull().sum()}')

# Display the number of unique values in each column
print(f'Unique Values:\n{df.nunique()}')

# Isolating a single column (example: 'name')
print(df['name'].head())

# Isolating multiple columns (example: 'name', 'sex', 'age')
print(df[['name', 'sex', 'age']].head())

# Isolating a single row by index (example: row 5)
print(df.loc[5])

# Isolating multiple rows using a range (example: rows 5 to 20)
print(df.loc[5:20].head())

# Isolating multiple rows with a list of indices (example: rows 1, 5, 10, 6)
print(df.loc[[1, 5, 10, 6]])

# Create a copy of rows 5 to 20
dft = df.loc[5:20].copy()
print(dft.head())

# Try accessing an element using .loc and .iloc, handle errors
try:
    print(dft.loc[0])
except:
    print("There is an error with loc")

try:
    print(dft.iloc[0])
except:
    print("There is an error with iloc")
        