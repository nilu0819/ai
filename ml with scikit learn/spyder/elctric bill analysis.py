# in this we are importing liberarys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# in this we are reading the file with path location
df=pd.read_excel(r"C:\Users\niles\OneDrive\Documents\Book2.xlsx")

# in this dependent and independent saperating with x and y
x=df.iloc[:,:-1].values
y=df.iloc[:,1].values

#in this spliting in this x and y in to train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

# in this importing the linearregresion model to predict 
from sklearn.linear_model import LinearRegression
regresor=LinearRegression()
regresor.fit(x_train,y_train)

y_pre=regresor.predict(x_test)

comp=pd.DataFrame({'actual':y_test,'predicte':y_pre})
print(comp)

plt.scatter(x_test,y_test,color='blue')
plt.plot(x_train,regresor.predict(x_train),color='green')
plt.title('month wise electric bill')
plt.xlabel('consuption')
plt.ylabel('amount')
plt.show()

jan=regresor.coef_  
print('jan =',jan)

inte=regresor.intercept_
print('intercept=',inte)

jan1=jan *700 + inte
print('jan1=',jan1)

r2=regresor.score(x_train,y_train)
print('r2=',r2)

var=regresor.score(x_test, y_test)
print(var)


import pickle
#save the trained model to disk
filename='Linear_regression_elctri _bill_analysis.pkl'
with open(filename,'wb') as file:
          pickle.dump(regresor,file)
          
          