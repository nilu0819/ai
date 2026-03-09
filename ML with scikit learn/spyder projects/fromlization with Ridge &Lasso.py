# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Preprocessing and model utilities
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

# Regression models and evaluation metrics
from sklearn.linear_model import LinearRegression, Ridge, Lasso 
from sklearn.metrics import r2_score

# ---------------- Data Preparation ----------------

# Load dataset
data = pd.read_csv(r"C:\Users\niles\Downloads\car-mpg.csv")

# Drop irrelevant column
data = data.drop(['car_name'], axis=1)

# Replace numeric origin codes with categorical labels
data['origin'] = data['origin'].replace({1: 'america', 2: 'eroupe', 3: 'asia'})

# Convert categorical column 'origin' into dummy variables (one-hot encoding)
data = pd.get_dummies(data, columns=['origin'], dtype=int)

# Replace missing values represented by '?' with NaN
data = data.replace('?', np.nan)

# Convert all columns to numeric where possible
data = data.apply(pd.to_numeric, errors='ignore')

# Fill missing numeric values with median of each column
data = data.apply(lambda x: x.fillna(x.median()) if x.dtype != 'object' else x)

# ---------------- Feature & Target Split ----------------

# Independent variables (features)
x = data.drop(['mpg'], axis=1)

# Dependent variable (target)
y = data[['mpg']]

# ---------------- Scaling ----------------

# Standardize features (mean=0, variance=1)
x_s = preprocessing.scale(x)
x_s = pd.DataFrame(x_s, columns=x.columns)

# Standardize target variable
y_s = preprocessing.scale(y)
y_s = pd.DataFrame(y_s, columns=y.columns)

# ---------------- Train-Test Split ----------------

x_train, x_test, y_train, y_test = train_test_split(x_s, y_s, test_size=0.20, random_state=0)

# Print shapes of train/test sets
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# ---------------- Linear Regression ----------------

# Fit linear regression model
regression_model = LinearRegression()
regression_model.fit(x_train, y_train)

# Coefficients of regression model
reg_coef = regression_model.coef_
print("Linear Regression Coefficients:", reg_coef)

# ---------------- Ridge Regression ----------------

# Fit Ridge regression model (L2 regularization)
ridge_model = Ridge(alpha=0.4)
ridge_model.fit(x_train, y_train)
print("Ridge Regression Coefficients:", ridge_model.coef_)