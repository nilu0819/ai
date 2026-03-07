import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic =pd.read_csv(r"C:\Users\niles\OneDrive\Documents\Desktop\titanic dataset.csv")
titanic
# imp columns:
    # survived = target(0 = no = yes)
    # pclass = passenger class
    # sex = male\female
    # age = num
    # fare= num
    # embarked=port(c,q,s)


# Sepearte x and yes
# x = inde
# y = depe
x = titanic[['Pclass','Sex','Age','Fare','Embarked']].values
y = titanic['Survived'].values

# missing value--

# Age
# Embarked

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
x[:,2:3] = imputer.fit_transform(x[:,2:3])   # Age column


imputer_cat = SimpleImputer(strategy='most_frequent')
x[:,4:5] = imputer_cat.fit_transform(x[:,4:5])


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(),[1,4])
        ],
    remainder='passthrough'
    )

x = ct.fit_transform(x)

# split dataset

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=0)


# Feature Scalling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# train model


from sklearn.linear_model import LinearRegression

model = LogisticRegression()
model.fit(x_train,y_train)

print(model.score(x_test,y_test))