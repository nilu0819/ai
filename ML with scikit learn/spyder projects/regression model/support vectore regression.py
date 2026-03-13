# SVR

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\emp_sal.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'poly',degree = 4)
regressor.fit(X, y)

#regressor created properly with default parameter after execute the above line of code
#now we will check what was the actual salary after scaling 

# Predicting a new result

#y_pred_knn = regressor_knn.predict([[6.5]])

y_pred_svr = regressor.predict([[6.5]])

#y_pred_dtr = regressor_dt.predict([[6.5]])

#y_pred_rf = reg_rf.predict([[6.5]])

#y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))
#we will see what is predicted salary for the 6.5yrs of exp new employee
#always check the next argument function by select the object inspector
#you have to transform the 6.5 numerical value transform and fit to the regressor 
#we have to do the inverse transform to get the orginial scale & by using the inverse_transform then we will get the scaled prediction salary
#after execute we get very great prediction we found the predicted sal is 170k which is too good
#we can say that our svr model quite good model compare to polynomial regression, finally we can say that svr is great model





# SVR

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\emp_sal.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

'''
from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor(n_neighbors=4, algorithm = 'kd_tree')
regressor.fit(X, y)
'''

# Fitting SVR to the dataset
from sklearn.svm import SVR
#imported the svr class from SKLEARN.SVM library
regressor = SVR(kernel = 'poly', degree=5)

#create regressor object & for now understand kernal is use for linear,polynomial or non-linear svr which we will see indepth concept SVM 
#Non-linear data we will use kernal & rbf is the value which we will assign rbf for kernal
regressor.fit(X, y)
#as usual fit the svr regressor 

# Predicting a new result
y_pred = regressor.predict([[6.5]])

#we are checking employee previous salary we found as 130k but actually his sal was 160k which is incorrect
#that is not good at all, we


# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


#why wrong prediction happened hear & why we got the blue straight line we got hear
#lets look at this & on this cases we have to do the feature scaling 
#lets see the code with feature scaling technique





