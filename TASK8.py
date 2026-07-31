import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ==========================================
# STEP 1: CREATE THE DATASET (Generated for you)
# ==========================================
# Creating 25 rows of sample student data
data = {
    'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 
              7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 
              2.7, 4.8, 3.8, 6.9, 7.8],
    'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 
               85, 62, 41, 42, 17, 95, 30, 24, 67, 69, 
               30, 54, 35, 76, 86]
}

# Convert dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Save it to a CSV file (useful for your Day 4 & 5 folder structure)
df.to_csv('student_scores.csv', index=False)
print("Dataset created and saved as 'student_scores.csv' successfully!")


# ==========================================
# STEP 2: PREPARE AND SPLIT DATA
# ==========================================
# Extracting features (X) and target (y)
X = df[['Hours']].values
y = df['Scores'].values

# Splitting data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# ==========================================
# STEP 3: TRAIN THE LINEAR REGRESSION MODEL
# ==========================================
# Initialize the model
model = LinearRegression()

# Train the model on training data
model.fit(X_train, y_train)

# Final confirmation output
print("\n--- Day 8 Expected Outcome ---")
print("Model trained successfully!")
print(f"Model Formula: Score = {model.coef_[0]:.2f} * Hours + {model.intercept_:.2f}")