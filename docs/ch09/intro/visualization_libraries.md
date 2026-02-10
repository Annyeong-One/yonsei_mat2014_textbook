# Visualization Libraries

Python offers a rich ecosystem of visualization libraries for different use cases.

---

## General Purpose

### Matplotlib

[Matplotlib](https://matplotlib.org/) is the foundational plotting library for Python.

- Most widely used
- Highly customizable
- Foundation for many other libraries
- Publication-quality output

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('Values')
plt.show()
```

---

## Statistical Data Analysis

### Seaborn

[Seaborn](http://stanford.edu/~mwaskom/software/seaborn) is built on Matplotlib for statistical visualization.

- Beautiful default styles
- High-level interface for statistical graphics
- Integration with pandas DataFrames
- Built-in themes

```python
import seaborn as sns

tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
```

---

## Web-Based Visualization

### Bokeh

[Bokeh](http://bokeh.pydata.org) creates interactive visualizations for web browsers.

- Interactive plots
- Streaming data support
- Web-ready output
- Dashboards

### Plotly

[Plotly](http://plot.ly) provides interactive, publication-quality graphs.

- Interactive charts
- 3D plotting
- Dashboards with Dash
- Wide language support

---

## 3D Visualization

### VisPy

[VisPy](http://vispy.org) is a high-performance interactive 2D/3D visualization library.

- GPU-accelerated
- Large dataset handling
- Scientific visualization
- OpenGL-based

---

## Choosing a Library

| Use Case | Recommended Library |
|----------|---------------------|
| Static publication plots | Matplotlib |
| Statistical analysis | Seaborn |
| Interactive web dashboards | Plotly, Bokeh |
| Large 3D datasets | VisPy |
| Quick exploratory analysis | Seaborn, Matplotlib |

---

## Key Takeaways

- Matplotlib is the foundation for Python visualization
- Seaborn simplifies statistical plotting
- Bokeh and Plotly excel at interactive web graphics
- VisPy handles high-performance 3D visualization
- Most libraries build on or integrate with Matplotlib
