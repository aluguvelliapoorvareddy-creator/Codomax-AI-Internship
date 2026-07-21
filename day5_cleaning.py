import pandas as pd

# 1. LOAD THE DIRTY DATA
print("--- 1. Original Dataset ---")
df = pd.read_csv("dataday5.csv")
print(df)


# 2. IDENTIFY MISSING VALUES AND DUPLICATES
print("\n--- 2. Checking for Issues ---")
print("Missing values per column:")
print(df.isnull().sum())

print(f"\nNumber of duplicate rows found: {df.duplicated().sum()}")


# 3. CLEAN THE DATASET
print("\n--- 3. Cleaning Process ---")

# Fix 1: Drop identical duplicate rows
df_cleaned = df.drop_duplicates()

# Fix 2: Fill missing values with column defaults (Age with median, Salary with mean)
df_cleaned["Age"] = df_cleaned["Age"].fillna(df_cleaned["Age"].median())
df_cleaned["Salary"] = df_cleaned["Salary"].fillna(df_cleaned["Salary"].mean())

print("Cleaned Dataset:")
print(df_cleaned)


# 4. SAVE THE CLEAN DATA
df_cleaned.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data successfully saved to 'cleaned_data.csv'!")