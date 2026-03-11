# ---------------- Polynomial Regression Model ----------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\emp_sal.csv")

# Independent variable (Position level) and dependent variable (Salary)
x = dataset.iloc[:, 1:2].values   # Position level column
y = dataset.iloc[:, 2].values     # Salary column

# tree algorithme model
# decision tree regression

# intervies quisten (how to build tree from the dataset)

# Import DecisionTreeRegressor from sklearn
from sklearn.tree import DecisionTreeRegressor

# Create a Decision Tree Regressor model
# criterion='absolute_error' means it will minimize mean absolute error
# random_state=0 ensures reproducibility of results
dt_reg = DecisionTreeRegressor(criterion='absolute_error', random_state=0)

# Fit the model on training data (x = features, y = target values)
dt_reg.fit(x, y)

# Predict the target value for input [[6.5]]
dt_pred = dt_reg.predict([[6.5]])
print(dt_pred)   # Print the prediction from Decision Tree

