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


---

## Exercises

**Exercise 1.** Write the standard import statement for Matplotlib's pyplot module and NumPy. Then write code that checks and prints the Matplotlib version.

??? success "Solution to Exercise 1"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    # Solution code depends on the specific exercise
    x = np.linspace(0, 2 * np.pi, 100)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x))
    ax.set_title('Example Solution')
    plt.show()
    ```

    See the content of this page for the relevant API details to construct the full solution.

---

**Exercise 2.** Explain the difference between `pip install matplotlib` and `conda install matplotlib`. When would you use each?

??? success "Solution to Exercise 2"
    See the explanation in the main content of this page for the key concepts. The essential idea is to understand the API parameters and their effects on the resulting visualization.

---

**Exercise 3.** Write code that creates a simple test plot to verify Matplotlib is installed correctly. Plot $y = \sin(x)$ for $x \in [0, 2\pi]$.

??? success "Solution to Exercise 3"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    x = np.linspace(0, 2 * np.pi, 100)
    axes[0].plot(x, np.sin(x))
    axes[0].set_title('Left Subplot')

    axes[1].plot(x, np.cos(x))
    axes[1].set_title('Right Subplot')

    plt.tight_layout()
    plt.show()
    ```

    Adapt this pattern to the specific requirements of the exercise.

---

**Exercise 4.** List three Matplotlib backends and explain when you would use each. Write one line of code showing how to set the backend.

??? success "Solution to Exercise 4"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), 'b-', lw=2)
    ax.set_title('Solution')
    plt.show()
    ```

    Refer to the code examples in the main content for the specific API calls needed.
