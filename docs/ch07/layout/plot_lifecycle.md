# Plot Lifecycle

## Rendering Pipeline

### 1. Creation Phase

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Create Figure and Axes
ax.plot([1, 2, 3])  # Add Artists
```

### 2. Drawing Phase

```python
fig.canvas.draw()  # Render to backend
```

### 3. Display Phase

```python
plt.show()  # Display and enter event loop
```

## Display Methods

### 1. plt.show()

```python
plt.show()  # Blocks until window closed
# Enters main event loop
```

### 2. plt.draw()

```python
plt.draw()  # Non-blocking refresh
# Updates without halting
```

### 3. Interactive Mode

```python
plt.ion()  # Interactive on
plt.plot([1, 2, 3])  # Shows automatically
plt.ioff()  # Interactive off
```

## Backends

### 1. Interactive Backends

```python
import matplotlib
matplotlib.use('TkAgg')  # Tk-based
# matplotlib.use('Qt5Agg')  # Qt5-based
```

### 2. Non-interactive

```python
matplotlib.use('Agg')  # No display, file only
```

### 3. Jupyter

```python
%matplotlib inline  # Static images
%matplotlib notebook  # Interactive
```

## Event Loop

### 1. Blocking

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3])
plt.show()  # Blocks here
print("After show")  # Only after window closed
```

### 2. Non-blocking

```python
plt.ion()
fig, ax = plt.subplots()
ax.plot([1, 2, 3])
plt.pause(0.1)  # Brief pause to render
print("Continues immediately")
```

### 3. Animation Loop

```python
from matplotlib.animation import FuncAnimation

def update(frame):
    ax.clear()
    ax.plot([0, frame])

ani = FuncAnimation(fig, update, frames=range(10))
plt.show()
```
