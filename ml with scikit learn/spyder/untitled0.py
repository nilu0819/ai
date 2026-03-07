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

