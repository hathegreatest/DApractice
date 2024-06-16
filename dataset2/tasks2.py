# %%
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('hdbresale_cluster.csv')
data.head()
# %%
x = data.floor_area_sqm
y = data.amenities
plt.xlabel('floor_area_sqm')
plt.ylabel('amenities')
plt.scatter(x,y)
plt.show()
# %%
data.dtypes

# %%
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
data = list(zip(x,y))
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)

# %%
