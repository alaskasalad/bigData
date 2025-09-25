import csv 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

data = []
with open('tractor.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data.append(dict(row))

age = [x['age'] for x in data]
cost = [y['cost'] for y in data]

plt.plot(age,cost,'co')
# plt.show()

model = LinearRegression()
model.fit(age,cost)
