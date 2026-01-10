# Dimensionality Reduction
PCA, t-SNE for reducing feature dimensions while preserving variance or structure.

## PCA
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(pca.explained_variance_ratio_)
```

## t-SNE
```python
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, perplexity=30)
X_embedded = tsne.fit_transform(X)
```

## When to Use
**PCA:** Linear, interpretable, fast  
**t-SNE:** Non-linear, visualization, slow