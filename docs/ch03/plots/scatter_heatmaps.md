# Scatter Plots and Heatmaps

Scatter plots and heatmaps visualize relationships between variables and are essential for multivariate analysis.

---

## 1. Scatter plots

Scatter plots show pairs of observations:

```python
x = np.random.normal(size=500)
y = 0.5 * x + np.random.normal(size=500)

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
```

They reveal:
- correlation,
- clusters,
- outliers.

---

## 2. Enhancing scatter plots

```python
plt.scatter(x, y, alpha=0.5)
```

Transparency helps with overplotting.

---

## 3. Heatmaps

Heatmaps visualize values on a grid using color intensity.

```python
Z = np.random.rand(20, 20)
plt.imshow(Z)
plt.colorbar()
```

---

## 4. Correlation matrices

```python
corr = np.corrcoef(np.random.randn(5, 100))
plt.imshow(corr, vmin=-1, vmax=1)
plt.colorbar()
```

Heatmaps are widely used for correlation analysis.

---

## Key takeaways

- Scatter plots show pairwise relationships.
- Heatmaps encode values via color.
- Useful for correlation and structure discovery.
