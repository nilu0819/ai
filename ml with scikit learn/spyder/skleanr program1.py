# data pipe line
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\niles\Downloads\Data (2).csv")
df
x=df.iloc[:,:-1].values
y=df.iloc[:,3].values

from sklearn.impute import SimpleImputer
# simple imputer is liberary
# 

imputer=SimpleImputer(strategy='most_frequent')
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

from sklearn.preprocessing import LabelEncoder # use to making categorical to numerical
LabelEncoder_x=LabelEncoder()
x[:,0]=LabelEncoder_x.fit_transform(x[:,0])

LabelEncoder_y=LabelEncoder()
y=LabelEncoder_y.fit_transform(x[:,1])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
# random state 0 is use to data with acurate and not sufling
# without is data point is every time changing