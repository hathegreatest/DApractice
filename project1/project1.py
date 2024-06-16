import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('data.csv')
X = data['X'].values
y = data['y'].values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape the dataq
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

# Create the polynomial features
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Fit the model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predict the test data
y_pred = model.predict(X_test_poly)

# Calculate the R^2 score
r2 = r2_score(y_test, y_pred)
print(f'R^2 Score: {r2}')

# %%
# Define a function to square a number
def square(x):
    return x ** 2

# Apply the square function to each element in a list using map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Print the squared numbers
print(list(squared_numbers))
# %%
test_list = [{'name': 'Manjeet', 'age': 23},
             {'name': 'Akshat', 'age': 22},
             {'name': 'Nikhil', 'age': 21}]
 
# printing original list
print("The original list is : ",test_list)

# Create a functin to flatten the dictionary
def flatten_dict(d):
    return d['name'],d['age']
# Mapping key values to Dictionary
# Using map() and lambda function
res = dict(map(flatten_dict, test_list))
 
# printing result
print("The flattened dictionary is : " + str(res))
# %%
