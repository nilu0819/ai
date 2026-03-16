# Import necessary libraries
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
X, y = load_breast_cancer(return_X_y=True)

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize and train Logistic Regression model
lo = LogisticRegression(max_iter=10000)   # added max_iter to avoid convergence warnings
lo.fit(X_train, y_train)

# Evaluate accuracy on test set
acc = accuracy_score(y_test, lo.predict(X_test)) * 100
print(f'Logistic Regression model accuracy: {acc:.2f}%')


# ------------------- Digits Dataset Example -------------------

from sklearn import datasets, linear_model, metrics
from sklearn.metrics import confusion_matrix, classification_report

# Load digits dataset
digits = datasets.load_digits()
x, y = digits.data, digits.target

# Split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Train Logistic Regression model
lin = linear_model.LogisticRegression(max_iter=10000)
lin.fit(x_train, y_train)

# Predict on test set
y_pred = lin.predict(x_test)
print("Predicted labels:", y_pred)

# Compare actual vs predicted (for test set only)
comp = {'actual': y_test, 'predicted': y_pred}
print(comp)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Accuracy Score
ac = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {ac:.2f}")

# Classification Report
cr = classification_report(y_test, y_pred)
print("Classification Report:\n", cr)