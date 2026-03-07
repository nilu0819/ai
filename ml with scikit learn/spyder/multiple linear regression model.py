# we need to find out optimized attribute to find the best profit

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\niles\Downloads\Investment.csv")

x=df.iloc[:,:-1] # -1 is removed in x 
y=df.iloc[:,4]

x=pd.get_dummies(x,dtype=int)# is convert the cetegory to numerical

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

# finding the constant
intercept=regressor.intercept_
print(intercept)

coef=regressor.coef_  # finding the independent constant values
print(coef)

# multiple linear regression
# adding the value in x
x=np.append(arr=np.full((50,1),42467).astype(int),values=x,axis=1)
print(x)

# feture selection and feture elimination
# baack word elimination
# when pvaue is >0.05 remove it all dummy variable

import statsmodels.api as sm
x_opt=x[:,[0,1,2,3,4,5]]

regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm
x_opt=x[:,[0,1,2,3,5]]

regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm
x_opt=x[:,[0,1,2,3]]

regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm
x_opt=x[:,[0,1,3]]

regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()


import statsmodels.api as sm
x_opt=x[:,[0,1]]

regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

bias=regressor.score(x_train,y_train)

# feture engineering-> eda technology
#feture scaling-> standrlization & normalization
#feture selection ->rfe,backword elimination

#-> +
