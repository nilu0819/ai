# IMPORT LIBRARY
import numpy as np 	#Array		

import matplotlib.pyplot as plt		

import pandas as pd	

# IMPORT THE DATASET

dataset = pd.read_csv(r"C:\Users\niles\Downloads\Data (2).csv")

# INDEPENDENT VARIABLE
x = dataset.iloc[:, :-1].values	
# DEPENDENT VARIABLE
y = dataset.iloc[:,3].values  

# SKLEARN FILL MISSING NUMERICAL VALUE
from sklearn.impute import SimpleImputer

imputer = SimpleImputer() 

imputer = imputer.fit(x[:,1:3]) 

x[:, 1:3] = imputer.transform(x[:,1:3]) 

# IMPUTE CATEGORICAL VALUE FOR INDEPDENT 
from sklearn.preprocessing import LabelEncoder

labelencoder_X = LabelEncoder()

labelencoder_X.fit_transform(x[:,0]) 

x[:,0] = labelencoder_X.fit_transform(x[:,0]) 

## IMPUTE CATEGORICAL VALUE FOR DEPENDENT 

labelencoder_y = LabelEncoder()

y = labelencoder_y.fit_transform(y)

# SPLIT THE DATA 

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x, y,train_size=0.7,random_state=0) 


from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)
# ---------------------------------------------------------------




from sklearn.preprocessing import Normalizer
sc_x=Normalizer()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)