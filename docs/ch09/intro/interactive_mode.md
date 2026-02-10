# Interactive Mode

Interactive mode allows dynamic updating of plots without blocking script execution.

---

## Enabling Interactive Mode

```python
import matplotlib.pyplot as plt

plt.ion()   # Turn ON interactive mode
plt.ioff()  # Turn OFF interactive mode
```

Check current state:

```python
plt.isinteractive()  # Returns True or False
```

---

## Basic Interactive Example

```python
import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    # Enable interactive mode
    plt.ion()

    # Create initial plot
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    line, = ax.plot(x, y)

    # Set labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Interactive Plotting')

    # Update the plot dynamically
    for i in range(50):
        y = np.sin(x + i * 0.1)
        line.set_ydata(y)
        
        # Redraw the figure
        plt.draw()
        
        # Pause for animation effect
        plt.pause(0.1)

    # Turn off interactive mode
    plt.ioff()

    # Keep window open
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Key Functions

### plt.ion()

Turns on interactive mode:

- Plots update immediately
- Non-blocking execution
- Figures display without `show()`

```python
plt.ion()
plt.plot([1, 2, 3])  # Displays immediately
```

### plt.ioff()

Turns off interactive mode:

- Returns to default behavior
- Requires `plt.show()` to display
- Blocking execution

```python
plt.ioff()
plt.plot([1, 2, 3])
plt.show()  # Required to display
```

### plt.draw()

Redraws the current figure:

- Updates modified elements
- Non-blocking
- Use after changing data

```python
line.set_ydata(new_data)
plt.draw()  # Update display
```

### plt.pause(interval)

Pauses execution and updates display:

- Combines `draw()` with sleep
- Processes GUI events
- Essential for animations

```python
plt.pause(0.1)  # Pause 0.1 seconds and update
```

---

## Animation Pattern

The standard pattern for interactive animations:

```python
import matplotlib.pyplot as plt
import numpy as np

def animate():
    plt.ion()
    
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    line, = ax.plot(x, np.sin(x))
    ax.set_ylim(-1.5, 1.5)
    
    for phase in np.linspace(0, 4*np.pi, 100):
        line.set_ydata(np.sin(x + phase))
        plt.draw()
        plt.pause(0.05)
    
    plt.ioff()
    plt.show()

animate()
```

---

## Updating Plot Elements

### Update Line Data

```python
line, = ax.plot(x, y)  # Note the comma for unpacking

# Update y-data only
line.set_ydata(new_y)

# Update both x and y
line.set_data(new_x, new_y)
```

### Update Axis Limits

```python
ax.set_xlim(new_xmin, new_xmax)
ax.set_ylim(new_ymin, new_ymax)
```

### Update Title

```python
ax.set_title(f'Frame {i}')
```

---

## Real-Time Data Example

```python
import matplotlib.pyplot as plt
import numpy as np

def real_time_plot():
    plt.ion()
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(-2, 2)
    
    x_data = []
    y_data = []
    line, = ax.plot([], [])
    
    for i in range(100):
        # Simulate incoming data
        x_data.append(i)
        y_data.append(np.sin(i * 0.1) + np.random.normal(0, 0.1))
        
        line.set_data(x_data, y_data)
        ax.set_title(f'Data Point: {i}')
        
        plt.draw()
        plt.pause(0.05)
    
    plt.ioff()
    plt.show()

real_time_plot()
```

---

## Interactive Mode vs FuncAnimation

For more complex animations, consider `FuncAnimation`:

```python
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1.5, 1.5)

def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))
    return line,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
```

| Feature | Interactive Mode | FuncAnimation |
|---------|------------------|---------------|
| Simplicity | Simple | More setup |
| Performance | Lower | Higher (blit) |
| Saving | Manual | Built-in |
| Control | Full | Callback-based |

---

## Key Takeaways

- `plt.ion()` enables non-blocking interactive mode
- `plt.draw()` updates the display
- `plt.pause()` combines draw with a delay
- Update data with `line.set_ydata()` or `line.set_data()`
- Use for real-time data and simple animations
- Consider `FuncAnimation` for complex animations
