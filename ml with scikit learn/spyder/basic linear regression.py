#importing librarys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

 # prepare the data
data=pd.DataFrame({
     'size':[1000,1500,2000,2500,3000],
     'price':[200000,250000,300000,350000,400000]
     })

x=data[['size']] #[[]] for the 2 d array
y=data['price']
 
# spliting data 
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=1
    )

#train the model

model=LinearRegression()
model.fit(x_train, y_train)

# maka a predications
y_pre=model.predict(x_test) 

#evaluate the model
print('mean squared error',mean_squared_error(y_test,y_pre))
print('r2 score'),r2_score(y_test,y_pre)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

# making the visualizatins
plt.scatter(x, y, color='blue',label='data points')
plt.plot(x,model.predict(x),color='red',label='regression line')
plt.xlabel('size')
plt.ylabel('price')
plt.legend()
plt.show()