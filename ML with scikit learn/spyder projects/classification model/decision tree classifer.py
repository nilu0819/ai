# ---------------- Polynomial Regression Model ----------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\logit classification (1).csv")

# Independent variable (Position level) and dependent variable (Salary)
x = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values    # Salary column


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0
                                               )

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(max_depth=2,criterion='entropy')
dt.fit(x_train, y_train)

y_pred=dt.predict(x_test)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print(ac)

# tree algorithm does not requre any feature sclaing 