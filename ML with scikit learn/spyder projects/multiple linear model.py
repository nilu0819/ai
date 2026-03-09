#importing all the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

%matplotlib inline

#importing dataset using panda
dataset = pd.read_csv('../input/kc_house_data.csv')
#to see what my dataset is comprised of
dataset.head()

#checking if any value is missing
print(dataset.isnull().any())

#checking for categorical data
print(dataset.dtypes)

#dropping the id and date column
dataset = dataset.drop(['id','date'], axis = 1)

#understanding the distribution with seaborn
with sns.plotting_context("notebook",font_scale=2.5):
    g = sns.pairplot(dataset[['sqft_lot','sqft_above','price','sqft_living','bedrooms']], 
                 hue='bedrooms', palette='tab20',size=6)
g.set(xticklabels=[]);

#separating independent and dependent variable
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values
#splitting dataset into training and testing dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

import numpy as np
import statsmodels.api as sm

def backward_elimination(X, y, significance_level=0.05):
    """
    Perform backward elimination to remove insignificant variables.
    X: feature matrix (numpy array)
    y: target vector
    significance_level: threshold for p-values
    """
    num_vars = X.shape[1]
    while num_vars > 0:
        regressor = sm.OLS(y, X).fit()
        max_p_value = max(regressor.pvalues)
        if max_p_value > significance_level:
            # remove the variable with the highest p-value
            max_p_index = np.argmax(regressor.pvalues)
            X = np.delete(X, max_p_index, axis=1)
            num_vars -= 1
        else:
            break
    return X, regressor