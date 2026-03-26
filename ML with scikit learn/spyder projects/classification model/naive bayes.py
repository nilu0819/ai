# Naive Bayes Classification Example

# Importing the essential libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# Replace the path with your dataset location
dataset = pd.read_csv(r"C:\Users\niles\Downloads\logit classification (1).csv")

# Selecting features (columns 2 and 3) and target (last column)
X = dataset.iloc[:, [2, 3]].values   # Independent variables
y = dataset.iloc[:, -1].values       # Dependent variable (class labels)

# Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)
# test_size=0.20 → 20% data for testing, 80% for training
# random_state=0 → ensures reproducibility

# Feature Scaling
# Normalizer scales each sample individually to unit norm (good for text-like data)
from sklearn.preprocessing import Normalizer
sc = Normalizer()
X_train = sc.fit_transform(X_train)  # Fit on training data and transform
X_test = sc.transform(X_test)        # Transform test data using same scaling

# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()         # Multinomial Naive Bayes (good for count data)
classifier.fit(X_train, y_train)     # Train the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)  # Predictions on test data

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)  # Compare actual vs predicted
print("Confusion Matrix:\n", cm)

# Calculating Accuracy
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

# Checking bias (training accuracy)
bias = classifier.score(X_train, y_train)  # Accuracy on training set
print("Training Accuracy (Bias):", bias)
