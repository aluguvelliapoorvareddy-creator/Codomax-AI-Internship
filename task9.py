import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. GENERATE DATASET (Study Hours vs Student Scores)
data = {
    'Study_Hours': [
        2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 
        7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 
        2.7, 4.8, 3.8, 6.9, 7.8
    ],
    'Student_Score': [
        21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 
        85, 62, 41, 42, 17, 95, 30, 24, 67, 69, 
        30, 54, 35, 76, 86]
}
df = pd.DataFrame(data)

# 2. DAY 8 TASK: PREPARE AND TRAIN THE MODEL
X = df[['Study_Hours']]  # Feature matrix
y = df['Student_Score']  # Target vector

model = LinearRegression()
model.fit(X, y)
print("✅ Day 8 Complete: Linear Regression model trained successfully.")

# 3. DAY 9 TASK: GENERATE NEW PREDICTIONS 
# Custom input values for testing prediction accuracy
new_hours = pd.DataFrame({'Study_Hours': [2.0, 4.0, 6.5, 8.0, 9.5]})
predicted_scores = model.predict(new_hours)

# Create the final submission dataframe
submission_df = pd.DataFrame({
    'Study_Hours': new_hours['Study_Hours'],
    'Predicted_Score': np.round(predicted_scores, 2)
})

print("\n--- Day 9 Complete: Generated Predictions ---")
print(submission_df)

# 4. SAVE SUBMISSION DATA
submission_df.to_csv('day9_predictions.csv', index=False)
print("\n💾 Submission file saved as 'day9_predictions.csv'")

# 5. VISUALIZATION (Plotting results for your report documentation)
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Original Training Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(new_hours, predicted_scores, color='green', marker='X', s=120, label='Day 9 Predictions')

plt.title('Study Hours vs Student Scores (Prediction Model)')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()