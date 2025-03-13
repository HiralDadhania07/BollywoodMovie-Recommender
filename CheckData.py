import pandas as pd

# Load the dataset
file_path = 'BollywoodMovies.csv'
movies = pd.read_csv(file_path)

# Check the shape and columns
print("Dataset Shape:", movies.shape)
print("\nColumn Names:\n", movies.columns.tolist())

# View first 5 rows
print("\nSample Data:\n", movies.head())

# Check for missing values
print("\nMissing Values:\n", movies.isnull().sum())
