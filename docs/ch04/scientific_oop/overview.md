# OOP in Scientific Python

This section examines how major scientific Python libraries apply object-oriented design principles. Understanding their architecture helps you use them more effectively and write better code that integrates with their patterns.

---

## Why Study Library Design?

Scientific Python libraries are masterclasses in OOP:

| Library | Key OOP Concepts Demonstrated |
|---------|-------------------------------|
| **NumPy** | Custom container types, operator overloading, views vs copies, ufuncs |
| **Pandas** | Composition, method chaining, index objects, accessor pattern |
| **Matplotlib** | Object hierarchy, factory pattern, artist abstraction |

Understanding *how* these libraries work — not just *what* they do — makes you a better Python programmer.

---

## NumPy: The ndarray Object Model

NumPy's `ndarray` demonstrates:

- **Dunder methods**: `__getitem__`, `__setitem__`, `__add__`, `__matmul__`
- **Views vs copies**: Memory-efficient slicing through shared buffers
- **Universal functions (ufuncs)**: Vectorized operations via `__array_ufunc__`
- **Broadcasting**: Shape compatibility rules for element-wise operations
- **dtype system**: Type metadata as first-class objects

```python
import numpy as np

arr = np.array([1, 2, 3])

# Dunder methods in action
arr[0]           # __getitem__
arr + 10         # __add__ (broadcasts scalar)
arr @ arr        # __matmul__
len(arr)         # __len__
for x in arr:    # __iter__
    pass
```

---

## Pandas: Composition and Method Chaining

Pandas demonstrates:

- **Composition**: DataFrame contains Series, Series contains Index
- **Method chaining**: Fluent interface returning `self`
- **Accessor pattern**: `.str`, `.dt`, `.cat` namespace objects
- **Index as first-class object**: Not just row numbers, but rich objects

```python
import pandas as pd

# Method chaining — each method returns DataFrame
result = (df
    .query('age > 25')
    .groupby('department')
    .agg({'salary': 'mean'})
    .sort_values('salary', ascending=False)
    .head(10)
)

# Accessor pattern
df['name'].str.upper()      # StringMethods object
df['date'].dt.year          # DatetimeProperties object
```

---

## Matplotlib: The Artist Hierarchy

Matplotlib demonstrates:

- **Object hierarchy**: Figure → Axes → Artists
- **Factory pattern**: `plt.subplots()` creates configured objects
- **Separation of concerns**: Data (Artists) vs rendering (Backend)
- **Two APIs**: Procedural (pyplot) vs OOP (explicit objects)

```python
import matplotlib.pyplot as plt

# Procedural API (state machine)
plt.plot([1, 2, 3])
plt.title('Plot')
plt.show()

# OOP API (explicit objects)
fig, ax = plt.subplots()    # Factory creates Figure and Axes
line, = ax.plot([1, 2, 3])  # Returns Line2D artist
ax.set_title('Plot')        # Configure Axes object
fig.savefig('plot.png')     # Figure handles output
```

---

## Design Patterns in Action

### Pattern 1: Container Protocol (NumPy)

```python
class ndarray:
    def __getitem__(self, key):
        # Supports: arr[0], arr[1:3], arr[[1,2,3]], arr[arr > 0]
        ...
    
    def __setitem__(self, key, value):
        # In-place modification with broadcasting
        ...
    
    def __iter__(self):
        # Iterate over first dimension
        ...
```

### Pattern 2: Method Chaining (Pandas)

```python
class DataFrame:
    def query(self, expr):
        result = self._filter(expr)
        return result  # Return DataFrame for chaining
    
    def groupby(self, by):
        return DataFrameGroupBy(self, by)  # Return GroupBy object
    
    def sort_values(self, by):
        result = self._sort(by)
        return result  # Return DataFrame for chaining
```

### Pattern 3: Hierarchy (Matplotlib)

```python
class Figure:
    def __init__(self):
        self.axes = []  # Contains Axes objects
    
    def add_subplot(self, *args):
        ax = Axes(self, *args)
        self.axes.append(ax)
        return ax

class Axes:
    def __init__(self, figure, ...):
        self.figure = figure  # Reference to parent
        self.artists = []     # Contains Line2D, Text, etc.
    
    def plot(self, *args):
        line = Line2D(*args)
        self.artists.append(line)
        return [line]
```

---

## What You'll Learn

| Topic | OOP Concepts |
|-------|--------------|
| NumPy ndarray | Custom containers, operator overloading, memory views |
| NumPy dtype | Type objects, metadata, type promotion |
| NumPy ufuncs | Vectorization, `__array_ufunc__` protocol |
| NumPy broadcasting | Shape compatibility, implicit iteration |
| NumPy views | Shared memory, copy semantics |
| Pandas Series | Composition, Index objects |
| Pandas DataFrame | Heterogeneous containers, column access |
| Pandas Index | Immutable sequences, alignment |
| Pandas chaining | Fluent interfaces, method design |
| Matplotlib hierarchy | Figure/Axes/Artist, containment |
| Matplotlib APIs | State machine vs explicit OOP |
| Matplotlib artists | Drawable objects, rendering abstraction |

---

## Prerequisites

Before studying this section, ensure you understand:

- Classes and instances (Section 4.1)
- Dunder methods (Sections 4.10-4.11)
- Properties and descriptors (Sections 4.6, 4.9)
- Composition vs inheritance (Section 4.5)

---

## Key Takeaways Preview

1. **NumPy ndarray** is a sophisticated container implementing many dunder protocols
2. **Pandas** uses composition extensively — DataFrame contains Series contains Index
3. **Matplotlib** separates data (Artists) from presentation (Backend)
4. **Method chaining** requires methods to return appropriate objects
5. **Views vs copies** is a memory optimization pattern using shared buffers
6. Understanding library internals helps you debug and extend them effectively
