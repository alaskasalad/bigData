import csv 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.ticker as mticker

data = []
with open('tractor.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data.append(dict(row))

age1 = [x['age'] for x in data]
cost2 = [y['cost'] for y in data]

plt.plot(age1,cost2,'co')
# plt.show() 

age = np.array([float(x['age']) for x in data]).reshape(-1, 1)  # column vector
cost = np.array([float(y['cost']) for y in data]) 

sorted_idx = np.argsort(age.flatten())
age_sorted = age[sorted_idx].flatten()
cost_sorted = cost[sorted_idx]

# --- Scatter plot of raw data ---
plt.scatter(age_sorted, cost_sorted, c='c', marker='o', label="Data")

# using sklearn linear regression 
model = LinearRegression()
model.fit(age,cost)

# predict line 
y_pred_sklearn = model.predict(age_sorted.reshape(-1, 1))
plt.plot(age_sorted, y_pred_sklearn, 'r-', label="Sklearn Regression")

# --- (B) Closed-form Least Squares ---
X_b = np.c_[np.ones((len(age), 1)), age]  # add bias term
theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ cost
B0, B1 = theta_best

y_pred_closed = B0 + B1 * age_sorted
plt.plot(age_sorted, y_pred_closed, 'g--', label="Closed-form Regression")

# --- Format axes ---
plt.xlabel("Age")
plt.ylabel("Cost")
plt.ylim(min(cost) - 100, max(cost) + 100)  # zoom y-axis around data
plt.gca().yaxis.set_major_formatter(mticker.ScalarFormatter())
plt.ticklabel_format(style='plain', axis='y')

# --- Legend & show ---
plt.legend()
plt.show()