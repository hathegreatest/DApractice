# %%
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

#read and print the data set
df = pandas.read_csv("dataset4.csv")
# %%
print(df)
# %%
df['Wind'] = df['Wind'].astype(str)
df['Wind'].value_counts

df['Outlook'] = df['Outlook'].map({'rainy':0,'sunny':1,'overcast':2})
df['Temperature'] = df['Temperature'].map({'cool':0, 'mild':1, 'hot':2})    
df['Humidity'] = df['Humidity'].map({'normal':0, 'high':1})
df['Wind'] = df['Wind'].map({'False':1, 'True':0})
df['Play'] = df['Play'].map({'no':0, 'yes':1})
# %%
# X is the feature columns, Y is the target column
features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
X = df[features]
Y = df['Play']
print(X)
print(Y)

# Create a decision tree model
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, Y)
tree.plot_tree(dtree,feature_names=features)
plt.show()
# %%
print(dtree.predict([[2,1,1,0]]))


# %%
