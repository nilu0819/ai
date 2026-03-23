import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\logit classification (1).csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
#for this observation let me selcted as 100 observaion for test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20,random_state=0)

from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
model=BernoulliNB()
model.fit(X,y)

y_prd=model.predict(X)
print(y_prd)

ac=accuracy_score(y,y_prd)
print(ac)