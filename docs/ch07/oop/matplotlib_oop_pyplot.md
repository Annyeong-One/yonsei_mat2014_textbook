# OOP vs Pyplot

## Two Paradigms

### 1. OOP Style (Explicit)

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
```

### 2. Pyplot Style (Implicit)

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

### 3. State Machine

Pyplot maintains current figure and axes:

```python
plt.plot([1, 2])  # Acts on current axes
plt.title('Title')  # Acts on current axes
```

## When to Use Each

### 1. OOP Advantages

- Explicit control
- Multiple figures
- Reusable functions
- GUI integration

```python
def plot_data(ax, data):
    ax.plot(data)
    ax.set_title('Data')
    return ax

fig, (ax1, ax2) = plt.subplots(1, 2)
plot_data(ax1, [1, 2, 3])
plot_data(ax2, [4, 5, 6])
```

### 2. Pyplot Advantages

- Quick scripts
- Interactive use
- Familiar (MATLAB-like)

```python
# Quick exploration
plt.plot([1, 2, 3])
plt.show()
```

### 3. Mixing Styles

```python
fig, ax = plt.subplots()  # OOP
ax.plot([1, 2, 3])  # OOP
plt.title('Title')  # Pyplot (acts on current axes)
plt.show()  # Pyplot
```

## Best Practices

### 1. Prefer OOP

```python
# ✅ GOOD - Explicit
def make_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    return fig, ax

# ❌ BAD - Implicit state
def make_plot():
    plt.plot([1, 2, 3])  # Which figure?
```

### 2. Return Objects

```python
def create_figure():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    return fig  # Caller controls display
```

### 3. Avoid plt.show() in Functions

```python
# ✅ GOOD
def plot_data(ax, data):
    ax.plot(data)
    # No plt.show() - let caller decide

# ❌ BAD
def plot_data(data):
    plt.plot(data)
    plt.show()  # Blocks and closes figure
```
