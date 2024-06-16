# %%
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Sales.csv')
data.head()
# %%
x = data.num_of_orders
y = data.sales_total
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y, color='blue')
plt.plot(x, mymodel, color='red')
plt.show()
# %%
# cluster the data
from sklearn.cluster import KMeans
data = list(zip(x, y))
inertias = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)
plt.plot(range(1, 11), inertias)
plt.show()

# %%
kmeans = KMeans(n_clusters=3)

kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()
# %%
