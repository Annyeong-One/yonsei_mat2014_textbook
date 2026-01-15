# Basic Line Plot

The `plot()` method is the fundamental tool for creating line plots in Matplotlib.

---

## Simplest Line Plot

Provide only y-values (x-values are auto-generated as indices):

```python
import matplotlib.pyplot as plt

y = [1, 5, 2]

plt.plot(y)
plt.show()
```

---

## Providing X and Y Values

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [1, 5, 2]

plt.plot(x, y)
plt.show()
```

---

## OOP Style

Using explicit Figure and Axes objects:

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Multiple Lines

Plot multiple lines on the same axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y_sin)
ax.plot(x, y_cos)
plt.show()
```

---

## Plot Returns Line2D Objects

The `plot()` method returns a list of `Line2D` objects:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 10)
y = np.sin(x)

lines = plt.plot(x, y, '--*r', ms=20)
plt.show()

print(type(lines))     # <class 'list'>
print(type(lines[0]))  # <class 'matplotlib.lines.Line2D'>
```

---

## With Labels and Title

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y = x + x**2

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y, color='g')
ax.set_title('$y = x + x^2$', fontsize=20)
ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$y$', fontsize=20)
plt.show()
```

---

## Combining Multiple Options

Use the `set()` method for multiple properties at once:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y = x + x**2

fig, ax = plt.subplots()
ax.plot(x, y, color='g')
ax.set(
    title='$y = x + x^2$',
    xlabel='$x$',
    ylabel='$y$',
    xlim=[0, 1],
    ylim=(0, 2),
    xticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    yticks=[0.0, 0.5, 1.0, 1.5, 2.0]
)
plt.show()
```

---

## Practical Example: Financial Data

```python
import matplotlib.pyplot as plt
import yfinance as yf

def main():
    kospi_ticker = "^KS11"
    kospi_data = yf.download(kospi_ticker, start="2023-01-01", end="2024-12-31")
    close_prices = kospi_data["Close"]

    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(close_prices, label="KOSPI Close")
    ax.set_title("KOSPI Closing Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    ax.legend()
    ax.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
```

---

## Key Takeaways

- `plt.plot(y)` uses indices as x-values
- `plt.plot(x, y)` specifies both coordinates
- Multiple `plot()` calls add lines to the same axes
- `plot()` returns a list of `Line2D` objects
- Use `ax.set()` for multiple properties at once
