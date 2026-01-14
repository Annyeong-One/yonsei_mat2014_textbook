# Python Data Science Ecosystem

Matplotlib sits at the center of the Python data science ecosystem, integrating with numerical computing, data manipulation, and machine learning libraries.

---

## The Ecosystem

The Python data science stack consists of interconnected libraries:

```
                    ┌─────────────────┐
                    │   Applications  │
                    │  (Your Code)    │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│   Matplotlib  │   │    Pandas     │   │  Scikit-learn │
│ (Visualization)│   │(Data Analysis)│   │     (ML)      │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │     NumPy     │
                    │(Array Computing)│
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Python     │
                    └───────────────┘
```

---

## Core Libraries

### NumPy

The foundation for numerical computing:

- N-dimensional arrays
- Mathematical functions
- Linear algebra
- Random number generation

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
```

### Pandas

Data manipulation and analysis:

- DataFrame and Series
- Data cleaning
- Time series support
- CSV/Excel I/O

```python
import pandas as pd

df = pd.read_csv('data.csv')
df['column'].plot()
```

### Matplotlib

Visualization:

- 2D plotting
- Publication quality
- Highly customizable
- Multiple backends

```python
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()
```

---

## Integration Examples

### NumPy + Matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

### Pandas + Matplotlib

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.plot(kind='bar')
plt.show()
```

### Scikit-learn + Matplotlib

```python
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
plt.show()
```

---

## Library Relationships

| Library | Depends On | Used By |
|---------|------------|---------|
| NumPy | Python | Everything |
| Pandas | NumPy | Seaborn, Scikit-learn |
| Matplotlib | NumPy | Seaborn, Pandas |
| Seaborn | Matplotlib, Pandas | Applications |
| Scikit-learn | NumPy, SciPy | Applications |

---

## Key Takeaways

- NumPy is the foundation for numerical computing
- Pandas builds on NumPy for data manipulation
- Matplotlib integrates with both for visualization
- Seaborn extends Matplotlib for statistical graphics
- Understanding the ecosystem helps choose the right tool
