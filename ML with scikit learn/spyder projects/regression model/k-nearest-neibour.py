import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\emp_sal.csv")

# Independent variable (Position level) and dependent variable (Salary)
x = dataset.iloc[:, 1:2].values   # Position level column
y = dataset.iloc[:, 2].values     # Salary column

from sklearn.neighbors import KNeighborsRegressor
regressor_knn = KNeighborsRegressor(n_neighbors=4)
regressor_knn.fit(x,y)

from sklearn.tree import DecisionTreeRegressor
regressor_dt = DecisionTreeRegressor(splitter="random",criterion='absolute_error')
regressor_dt.fit(x,y)


from sklearn.ensemble import RandomForestRegressor
reg_rf = RandomForestRegressor(random_state=0, n_estimators = 50)
reg_rf.fit(x,y)

 # ---------------- Visualization: Linear Regression ----------------
plt.scatter(x, y, color='red')                        # Actual data points
plt.plot(x, regressor_knn.predict(x), color='blue')         # Linear regression line
plt.title('Linear Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')                                  # <-- fixed typo (ylable → ylabel)
plt.show()