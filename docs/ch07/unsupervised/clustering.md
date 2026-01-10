# Clustering Algorithms
K-means, hierarchical, DBSCAN for grouping similar data points without labels.

## K-Means
```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)
```

## DBSCAN
```python
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)
```

## Hierarchical
```python
from sklearn.cluster import AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=3)
labels = model.fit_predict(X)
```