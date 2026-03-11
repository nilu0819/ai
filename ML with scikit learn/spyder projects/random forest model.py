# ---------------- Polynomial Regression Model ----------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\emp_sal.csv")

# Independent variable (Position level) and dependent variable (Salary)
x = dataset.iloc[:, 1:2].values   # Position level column
y = dataset.iloc[:, 2].values     # Salary column


# Random Forest Regressor Example
# -------------------------------

# Import RandomForestRegressor from sklearn
from sklearn.ensemble import RandomForestRegressor

# Create a Random Forest Regressor model
# random_state=0 ensures reproducibility
# n_estimators=200 means the forest will have 200 decision trees
# max_depth=10 limits the depth of each tree to avoid overfitting
# min_samples_split=5 requires at least 5 samples to split a node
# min_samples_leaf=2 requires at least 2 samples in each leaf node
rf_reg = RandomForestRegressor(
    random_state=0,
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2
)

# Fit the Random Forest model on training data
rf_reg.fit(x, y)

# Predict the target value for input [[6.5]]
rf_pred = rf_reg.predict([[6.5]])
print(rf_pred)   # Print the prediction from Random Forest

