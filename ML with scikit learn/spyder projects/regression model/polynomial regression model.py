# ---------------- Polynomial Regression Model ----------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\emp_sal.csv")

# Independent variable (Position level) and dependent variable (Salary)
x = dataset.iloc[:, 1:2].values   # Position level column
y = dataset.iloc[:, 2].values     # Salary column

# ---------------- Linear Regression ----------------
# Fit a simple linear regression model (degree = 1)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# ---------------- Polynomial Regression ----------------
# Fit a polynomial regression model (degree = 5 initially)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)
x_poly = poly_reg.fit_transform(x)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# ---------------- Prediction Example ----------------
# Predict salary for position level 6.5 using linear model
lin_model_pred = lin_reg.predict([[6.5]])
print("Linear model prediction (6.5):", lin_model_pred)

# ---------------- Visualization: Linear Regression ----------------
plt.scatter(x, y, color='red')                        # Actual data points
plt.plot(x, lin_reg.predict(x), color='blue')         # Linear regression line
plt.title('Linear Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')                                  # <-- fixed typo (ylable → ylabel)
plt.show()

# ---------------- Higher Degree Polynomial Regression ----------------
# Try polynomial regression with degree = 6
poly_reg = PolynomialFeatures(degree=6)
x_poly = poly_reg.fit_transform(x)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# Visualization: Polynomial Regression
plt.scatter(x, y, color='red')                                        # Actual data points
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color='blue') # Polynomial regression curve
plt.title('Polynomial Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Predict salary for position level 6.5 using polynomial model
poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print("Polynomial model prediction (6.5):", poly_model_pred)

# ---------------- Hyperparameter Tuning Notes ----------------
# By changing the polynomial degree, the prediction for position level 6.5 changes:
# degree 1 → ~330k
# degree 2 → ~189k
# degree 3 → ~133k
# degree 4 → ~158k
# degree 5 → ~174.8k
# degree 6 → ~174.1k
# This shows how polynomial degree affects model flexibility and prediction accuracy.

#support vector regression

# Import Support Vector Regression model from sklearn
from sklearn.svm import SVR

# Create SVR model with polynomial kernel of degree 6
# gamma='auto' sets gamma = 1/n_features
# C=3.0 controls regularization (higher C = stricter fit)
# coef0=2.0 is used in polynomial kernel to adjust influence of higher-order terms
svr_reg = SVR(kernel='poly', degree=6, gamma='auto', C=3.0, coef0=2.0)

# Train the SVR model on training data (x = features, y = target)
svr_reg.fit(x, y)

# Predict the target value for input 6.5
svr_reg = svr_reg.predict([[6.5]])
print(svr_reg)   # Print SVR prediction


# ---------------- KNN Regression ----------------
from sklearn.neighbors import KNeighborsRegressor

# Create KNN regressor
# n_neighbors=2 means prediction is based on 2 nearest neighbors
# p=2 means distance metric is Euclidean (L2 norm)
knn_reg = KNeighborsRegressor(p=2, n_neighbors=2)

# Train the KNN model on training data
knn_reg.fit(x, y)

# Predict the target value for input 6.5
knn_reg = knn_reg.predict([[6.5]])
print(knn_reg)   # Print KNN prediction

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


# -------------------------------
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















