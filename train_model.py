import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
data = pd.read_csv("student_data.csv")

# Input features
X = data[
    ["Attendance", "Study_Hours", "Assignment_Score",
     "Mid_Marks", "Previous_GPA"]
]

# Target
y = data["Final_Score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Check accuracy
score = model.score(X_test, y_test)

print("Model trained successfully!")
print("Model R² Score:", round(score, 2))

# Save model
joblib.dump(model, "student_performance_model.pkl")

print("Model saved successfully!")