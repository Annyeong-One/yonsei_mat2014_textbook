# Saving and Exporting Figures

Once a figure is created, it often needs to be saved for reports, papers, or presentations.

---

## 1. Saving figures

Use `savefig` on the Figure object:

```python
fig.savefig("figure.png")
```

Or via pyplot:

```python
plt.savefig("figure.png")
```

---

## 2. File formats

Common formats:
- PNG: raster, good for screens
- PDF: vector, ideal for papers
- SVG: vector, web-friendly

```python
fig.savefig("plot.pdf")
```

---

## 3. Resolution and size

Control resolution with `dpi`:

```python
fig.savefig("plot.png", dpi=300)
```

Figure size is set at creation time:

```python
fig, ax = plt.subplots(figsize=(6, 4))
```

---

## 4. Tight layout

Avoid clipped labels:

```python
fig.tight_layout()
```

Or:

```python
plt.tight_layout()
```

---

## 5. Reproducibility

- Save figures programmatically.
- Avoid manual resizing.
- Use consistent styles for reports.

---

## Key takeaways

- Use `savefig` to export figures.
- Choose formats based on use case.
- Control size and DPI explicitly.
