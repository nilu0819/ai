# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\Salary_Data.csv")

# Separate features (YearsExperience) and target (Salary)
x = dataset.iloc[:, :-1]   # Independent variable(s)
y = dataset.iloc[:, -1]    # Dependent variable (Salary)

# Split dataset into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Apply Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)   # Train the model

# Predict salaries for test data
y_pred = regressor.predict(x_test)

# Compare actual vs predicted values
comparision = pd.DataFrame({'Actual': y_test, 'Prediction': y_pred})
print(comparision)

# Plot regression line with test data
plt.scatter(x_test, y_test, color='Red')   # Scatter plot of actual test data
plt.plot(x_train, regressor.predict(x_train), color='blue')   # Regression line
plt.title('Salary of employee based on experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# Predict future salary for 20 years of experience
m_coef = regressor.coef_       # Slope (coefficient)
print(m_coef)

c_intercept = regressor.intercept_   # Intercept
print(c_intercept)

y_20 = m_coef * 20 + c_intercept     # Salary prediction for 20 years experience
print(y_20)

# Model performance: bias (train score) and variance (test score)
bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)

# ---------------- Statistical Analysis ----------------

# Mean values
dataset.mean()
dataset['Salary'].mean()
dataset['YearsExperience'].mean()

# Median values
dataset.median()
dataset['Salary'].median()
dataset['YearsExperience'].median()

# Variance and Standard Deviation
dataset.var()
dataset.std()
dataset['Salary'].std()
dataset['YearsExperience'].std()

# Coefficient of variation
from scipy.stats import variation
variation(dataset.values)

# Correlation
dataset.corr()
dataset['Salary'].corr(dataset['YearsExperience'])

# Skewness
dataset.skew()
dataset['Salary'].skew()
dataset['YearsExperience'].skew()

# Standard Error of Mean
dataset.sem()

# Z-score normalization
import scipy.stats as stats
dataset.apply(stats.zscore)

# ---------------- Regression Statistics ----------------

y_mean = np.mean(y)
SSR = np.sum((y_pred - y_mean) ** 2)   # Sum of Squares for Regression
print(SSR)

y = y[0:6]   # Taking first 6 values for SSE calculation
SSE = np.sum((y - y_pred) ** 2)        # Sum of Squares for Error
print(SSE)

mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values - mean_total) ** 2)   # Total Sum of Squares
print(SST)

r_square = 1 - SSR / SST   # R² calculation
print(r_square)

# ---------------- Save Model ----------------

import pickle
filename = 'Linear_regression_model_pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as Linear_regression_model.pkl")