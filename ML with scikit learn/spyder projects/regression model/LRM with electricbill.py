# ==============================
# 1️⃣ Import Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# ==============================
# 2️⃣ Load Dataset
# ==============================
dataset = pd.read_excel(r"C:\Users\niles\OneDrive\Documents\Book2.xlsx")


# ==============================
# 3️⃣ Create Numeric Month Column
# ==============================
dataset['Month_Number'] = range(1, len(dataset) + 1)


# ==============================
# 4️⃣ Define Features (X) and Target (y)
# ==============================
X = dataset[['Month_Number']]
y = dataset['amount']


# ==============================
# 5️⃣ Split Data into Train & Test
# ==============================
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==============================
# 6️⃣ Train Linear Regression Model
# ==============================
regressor = LinearRegression()
regressor.fit(x_train, y_train)


# ==============================
# 7️⃣ Predict on Test Data
# ==============================
y_pred = regressor.predict(x_test)


# ==============================
# 8️⃣ Create Comparison Table
# ==============================
comparison = pd.DataFrame({
    'Actual': y_test.values,
    'Prediction': y_pred
})

print("\nActual vs Predicted Comparison:\n")
print(comparison)


# ==============================
# 9️⃣ Plot Actual Points + Predicted Points + Line
# ==============================
plt.figure(figsize=(8,5))

# Actual points
plt.scatter(x_test, y_test, color='red', label='Actual')

# Predicted points
plt.scatter(x_test, y_pred, color='green', label='Predicted Points')

# Regression line (using full dataset for clean line)
plt.plot(X, regressor.predict(X), color='blue', label='Regression Line')

plt.title('Monthly Bill Prediction')
plt.xlabel('Month Number')
plt.ylabel('Total Bill')
plt.legend()

plt.show()


# ==============================
# 🔟 Print Model Parameters
# ==============================
print("\nSlope (m):", regressor.coef_[0])
print("Intercept (c):", regressor.intercept_)


# ==============================
# 1️⃣1️⃣ Predict Month 13
# ==============================
next_month_prediction = regressor.predict([[13]])

print("\nPredicted Bill for Month 13:", next_month_prediction[0])