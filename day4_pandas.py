import pandas as pd

# 1. LOAD THE DATASET
print("--- 1. Loading Dataset ---")
# Reading the CSV file we created into a Pandas DataFrame
df = pd.read_csv("student_score.csv")
print("Dataset loaded successfully!\n")


# 2. EXPLORE ROWS AND COLUMNS
print("--- 2. Exploring Rows and Columns ---")
# Display the first 3 rows of the data
print("First 3 rows of the dataset:")
print(df.head(3))

# Display all column names
print("\nDataset Column Names:")
print(df.columns.tolist())

# Display the total number of rows and columns (shape)
print(f"\nDataset Shape (Rows, Columns): {df.shape}\n")


# 3. UNDERSTAND DATASET STATISTICS
print("--- 3. Dataset Statistics ---")
# Display a summary of the data types and missing values
print("Data Information Summary:")
print(df.info())

# Display descriptive mathematical statistics for numeric columns
print("\nStatistical Summary (Mean, Min, Max, etc.):")
print(df.describe())