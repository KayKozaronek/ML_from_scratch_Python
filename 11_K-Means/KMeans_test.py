import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt 
from KMeans import KMeans

X, y = make_blobs(centers=4, n_samples =500, n_features = 2, shuffle=True, random_state= 123)
print(X.shape)

clusters = len(np.unique(y))
print(clusters)

k = KMeans(K=clusters, max_iters =150, plot_steps = False)
y_pred = k.predict(X)

k.plot()