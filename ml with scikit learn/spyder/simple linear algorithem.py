import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\niles\Downloads\Salary_Data.csv")
df

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

# import traintest split

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=0)

# making the linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)# train data ==is call biyas 

# predicat the ctest values
y_pred=regressor.predict(x_test)# test data== is variance

# comparision table
comparision =pd.DataFrame({'actual':y_test, 'predicated':y_pred})
print(comparision)

# ploting the linear regression graph
plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('salary of employee based on expiriance')
plt.xlabel('expiriance')
plt.ylabel('salary')
plt.show()

# how predicat future
y_20=regressor.coef_
print(y_20)

# intercept is find the concetant
c_intercept=regressor.intercept_
print(c_intercept)

# fing the future 
y_20=y_20 * 20 +c_intercept
print(y_20)
# when the bias == variance than is best fit line
# bias is ==0.9423777652193379 out of 1
#Error from oversimplifying the model
bias=regressor.score(x_train,y_train)
print(bias)

#Error from being too sensitive to training data
# variance ==0.9740993407213511 out of 1
variance=regressor.score(x_test,y_test)
print(variance)

# states impliments in simple linear model (mean)
df.mean()
df['Salary'].mean()

# median
df.median()
df['Salary'].median()

# mode
df.mode()
df['Salary'].mode()

#variance
df.var() #this will give variance of entire data frame

df['Salary'].var()
#std
df.std()
df['Salary'].std()

#coefficiant of variance (cv)
from scipy.stats import variation
variation(df.values) # this will give cv entire data freame

variation(df['Salary'])

#correlation
df.corr()
df['Salary'].corr(df['YearsExperience'])

# skweeness 
df.skew()
df['Salary'].skew()

# standerd error
df.sem()

#z score this will give the entire data drame z score
import scipy.stats as stats
df.apply(stats.zscore)

stats.zscore(df['Salary'])

# ssr(SSR Sum of Squared Residuals (or Errors))predicted - actual**2)()
# fromula (actual - predicted)
y_mean=np.mean(y)
ssr=np.sum((y_pred-y_mean)**2)
print(ssr)

#sse(sum of squared error)
#formula ((actual - predicted)**2)
y=y[0:6]
sse=np.sum((y-y_pred)**2)
print(sse)

#sst(total sum of square)
#fromula(ssr+sse)
mean_total=np.mean(df.values)
sst=np.sum((df.values - mean_total)**2)
print(sst)

#r2
r_squre=1-ssr/sst
print(r_squre)

bias=regressor.score(x_train,y_train)
print(bias)


import pickle
#save the trained model to disk
filename='Linear_regression_model.pkl'
with open(filename,'wb') as file:
          pickle.dump(regressor,file)
print('model has been pickel and save') 






