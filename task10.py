import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split # standard for machine learning splits

# 1. Generate Dummy Data (Study Hours vs Exam Score)
# X = Study Hours (1 to 10 hours)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
# y = Actual Exam Scores (with a bit of realistic random variance)
y = np.array([45, 50, 58, 62, 68, 75, 80, 83, 92, 95])

# 2. Split into Training and Testing Sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the Day 8 Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Generate Day 9 Predictions on Test Data
y_pred = model.predict(X_test)

# 5. Day 10 Evaluation Metrics Calculation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 6. Output the Results
print("--- Day 10 Evaluation Results ---")
print(f"Actual Test Scores:   {y_test}")
print(f"Predicted Test Scores: {y_pred.round(2)}")
print("-" * 33)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score:                 {r2:.2f}")
import matplotlib.pyplot as plt

# 1. Compute your metrics (assuming y_test and y_pred exist from your script)
mae_val = mean_absolute_error(y_test, y_pred)
mse_val = mean_squared_error(y_test, y_pred)
rmse_val = np.sqrt(mse_val)  # RMSE is the square root of MSE

# 2. Set up data for plotting
metrics = ['MAE', 'MSE', 'RMSE']
values = [mae_val, mse_val, rmse_val]
colors = ['#3498db', '#e74c3c', '#2ecc71']  # Blue, Red, Green

# 3. Create the Bar Chart
plt.figure(figsize=(8, 5))
bars = plt.bar(metrics, values, color=colors, width=0.5, edgecolor='black')

# 4. Add Value Labels on Top of Each Bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height + (height * 0.01), 
             f'{height:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

# 5. Styling
plt.title('Model Performance Evaluation Errors (Lower is Better)', fontsize=14, fontweight='bold', pad=15)
plt.ylabel('Error Value', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 6. Display the Chart
plt.tight_layout()
plt.show()