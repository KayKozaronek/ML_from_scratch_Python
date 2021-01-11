import numpy as np 
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
from collections import Counter
from knn import KNN

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state =1234)


# Get a feel for the Dataset

# print(X_train.shape)
# print(X_train[0])

# print(y_train.shape)
# print(y_train)

# cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
# plt.figure()
# plt.scatter(X[:,0], X[:,1], c=y, cmap=cmap, edgecolor= "k", s=20)
# plt.show()

# Demonstrating Counter.most_common method
# a = [1,1,1,2,2,2,3,4,5,6]
# most_comn = Counter(a).most_common(2)
# print(most_comn)

clf = KNN(k=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

acc = np.sum(predictions == y_test) / len(y_test)
print(acc)

