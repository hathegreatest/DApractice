# %%
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

#read and print the data set
df = pandas.read_csv("dataset3.csv")
print(df)

# Change string vlues into numerical values
d = {'UK':0, 'USA':1, 'N':2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES':1, 'NO':0}
df['Go'] = df['Go'].map(d)
print(df)

# X is the feature columns, Y is the target column
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
Y = df['Go']
print(X)
print(Y)

# Create a decision tree model
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, Y)
tree.plot_tree(dtree,feature_names=features)
plt.show()
print(dtree.predict([[40, 10, 7, 1]]))
print(dtree.predict([[40, 10, 6, 1]]))


# %%
