# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from sklearn.neighbors import LocalOutlierFactor
from sklearn.datasets import make_blobs
from numpy import quantile, where, random
import matplotlib.pyplot as plt

#random.seed(1)
x, _ = make_blobs(n_samples=200, centers=1, cluster_std=.3, center_box=(10, 10))
print(x)
plt.scatter(x[:, 0], x[:, 1])
plt.show()

lof = LocalOutlierFactor(n_neighbors=20, contamination=.03)
#print(thresh)

y_pred = lof.fit_predict(x)

lofs_index = where(y_pred == -1)
values = x[lofs_index]

plt.scatter(x[:, 0], x[:, 1])
plt.scatter(values[:, 0], values[:, 1], color='r')
plt.show()
