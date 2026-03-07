import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score

df=pd.read_csv(r"C:\Users\niles\Downloads\car-mpg.csv") 
df.head()

# drop unnecessory columns
df=df.drop(['car_name'],axis=1)

#replace origin value
df['origin']=df['origin'].replace({1:'america',2:'europ',3:'asia'})

#convert origin to dummy variables
df=pd.get_dummies(df,columns=['origin'],dtype=int)

#replace ? with nan 
df=df.replace('?',np.nan)

#convert columns too numerical possible
df=df.apply(pd.to_numeric,errors='ignore')

#fill missing value with median
df=df.apply(lambda x:x.fillna(x.median())if x.dtype !='object' else x)

df.head()

#model buildings
x=df.drop(['mpg'],axis=1) #independent variable
y=df[['mpg']] # dependent varuable

x.head(1)
y.head()

# feture scaling for the reducing values
x_s=preprocessing.scale(x)
x_s=pd.DataFrame(x_s,columns=x.columns)

y_s=preprocessing.scale(y)
y_s=pd.DataFrame(y_s,columns=y.columns)

df.shape
# split into train test set
x_train,x_test,y_train,y_test=train_test_split(x_s,y_s,test_size=0.2,random_state=0)
x_train.shape

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#fit simple linear model and find the coef_

regression_model = LinearRegression()
regression_model.fit(x_train,y_train)

for idx,col_name in enumerate(x_train.columns):
    print('the coef_  for {} is {}'.format(col_name,regression_model.coef_[0][idx]))

intercept=regression_model.intercept_[0]
print('the intercept is {}'.format(intercept))

#alpha factoer hare id lambada
Ridge_model=Ridge(alpha=0.4)
Ridge_model.fit(x_train,y_train)

print('ridge model coef_ :{}'.format(Ridge_model))

Lasso_model=Lasso(alpha=0.1)
Lasso_model.fit(x_train,y_train)

print('Lasso_model coef_ :{}'.format(Lasso_model))

#score comaprision

#Model score - r^2 or coeff of determinant
#r^2 = 1-(RSS/TSS) = Regression error/TSS 


#Simple Linear Model
print(regression_model.score(x_train,y_train))
print(regression_model.score(x_test,y_test))

print('****************************')
#Ridgge
#Ridge
print(Ridge_model.score(x_train, y_train))
print(Ridge_model.score(x_test, y_test))

print('*************************')
#Lasso
print(Lasso_model.score(x_train, y_train))
print(Lasso_model.score(x_test, y_test))


#polynomial fetures
df=pd.concat([x_train,y_train],axis=1)
df.head()

#statistics impliments

import statsmodels.formula.api as smf
ols1=smf.ols(formula='mpg ~ cyl+disp+hp+wt+acc+yr+car_type+origin_america+origin_europ+origin_asia', data=df).fit() 

print(ols1.summary())

#Lets check Sum of Squared Errors (SSE) by predicting value of y for test cases and subtracting from the actual y for the test cases
mse  = np.mean((regression_model.predict(x_test)-y_test)**2)

# root of mean_sq_error is standard deviation i.e. avg variance between predicted and actual
import math
rmse = math.sqrt(mse)
print('Root Mean Squared Error: {}'.format(rmse))


# Is OLS a good model ? Lets check the residuals for some of these predictor.

fig = plt.figure(figsize=(10,8))
sns.residplot(x= x_test['hp'], y= y_test['mpg'], color='green', lowess=True )


fig = plt.figure(figsize=(10,8))
sns.residplot(x= x_test['acc'], y= y_test['mpg'], color='green', lowess=True )

# predict mileage (mpg) for a set of attributes not in the training or test set
y_pred = regression_model.predict(x_test)

# Since this is regression, plot the predicted y value vs actual y values for the test data
# A good model's prediction will be close to actual leading to high R and R2 values
#plt.rcParams['figure.dpi'] = 500
plt.scatter(y_test['mpg'], y_pred,color='black')


#Both Ridge & Lasso regularization performs very well on this data, though Ridge gives a
#better score. The above scatter plot depicts the correlation between the actual and 
#predicted mpg values.

