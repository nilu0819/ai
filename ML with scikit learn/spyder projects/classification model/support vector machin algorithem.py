# -------------------------------
# Support Vector Machine (SVM) Classification
# -------------------------------

# Importing essential libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\niles\Downloads\logit classification (1).csv")

# Selecting features (columns 2 and 3) and target (last column)
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into Training set and Test set (80% train, 20% test)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Feature Scaling (important for SVM and distance-based algorithms)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the SVM model on the Training set
from sklearn.svm import SVC
classifier = SVC()   # Default kernel = 'rbf'
classifier.fit(X_train, y_train)

# -------------------------------
# (Optional) KNN Classifier Example
# Uncomment to try KNN instead of SVM
# from sklearn.neighbors import KNeighborsClassifier
# classifier_knn = KNeighborsClassifier()
# classifier_knn.fit(X_train, y_train)
# -------------------------------

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Evaluating the model
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Accuracy Score
ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

# Bias (Training accuracy)
bias = classifier.score(X_train, y_train)
print("Training Accuracy (Bias):", bias)

# Variance (Test accuracy)
variance = classifier.score(X_test, y_test)
print("Test Accuracy (Variance):", variance)

# Detailed Classification Report (Precision, Recall, F1-score)
cr = classification_report(y_test, y_pred)
print("Classification Report:\n", cr)