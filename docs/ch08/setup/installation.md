# Installation and Import

Matplotlib is the foundational plotting library for Python scientific computing.

---

## Installation

Install via pip:

```bash
pip install matplotlib
```

Or via conda:

```bash
conda install matplotlib
```

---

## Import Convention

The standard import convention uses `plt` as the alias:

```python
import matplotlib.pyplot as plt
```

For numerical data, NumPy is typically imported alongside:

```python
import matplotlib.pyplot as plt
import numpy as np
```

---

## Version Check

```python
import matplotlib
print(matplotlib.__version__)
```

---

## Backend Configuration

Matplotlib uses backends for rendering. Common backends include:

```python
import matplotlib
matplotlib.use('TkAgg')  # Before importing pyplot
```

In Jupyter notebooks:

```python
%matplotlib inline    # Static images
%matplotlib notebook  # Interactive
```

---

## Verifying Installation

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

If a plot window appears (or renders inline in Jupyter), the installation is successful.

---

## Key Takeaways

- Install with `pip install matplotlib` or `conda install matplotlib`
- Import as `import matplotlib.pyplot as plt`
- Configure backend before importing pyplot if needed
