# %%
import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

# %%
# Load the data
data = pd.read_csv('Sales.csv')
data.head() 
# %%
X = data[['num_of_orders','gender']].values.reshape(-1,2) # independent variable
y = data['sales_total'].values # dependent variable 
reg = LinearRegression()
reg.fit(X,y)
# %%
# Plot the data
plt.scatter(X,y)
plt.plot(X, reg.predict(X), color='red')
plt.xlabel('Number of Orders')
plt.ylabel('Sales Total')
plt.title('Number of Orders vs Sales Total')
plt.show()
# %%
# Predict the sales total for 100 orders
reg.predict([[300,0]])
# %%
