# Axes Customization

## Axes Configuration

### 1. Limits

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

# Or
ax.set(xlim=(0, 10), ylim=(-5, 5))
```

### 2. Labels

```python
ax.set_xlabel('Time (s)', fontsize=12)
ax.set_ylabel('Amplitude', fontsize=12)
ax.set_title('Signal Analysis', fontsize=14, fontweight='bold')
```

### 3. Ticks

```python
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['zero', 'two', 'four', 'six', 'eight', 'ten'])
ax.tick_params(axis='both', labelsize=10, rotation=45)
```

## Grid and Spines

### 1. Grid

```python
ax.grid(True, linestyle='--', alpha=0.7)
ax.grid(which='major', color='gray', linestyle='-')
ax.grid(which='minor', color='lightgray', linestyle=':')
ax.minorticks_on()
```

### 2. Spines

```python
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_linewidth(2)
```

### 3. Axis Scaling

```python
ax.set_xscale('log')
ax.set_yscale('linear')
# Options: 'linear', 'log', 'symlog', 'logit'
```

## Legends and Annotations

### 1. Legend

```python
ax.plot([1, 2, 3], label='Line 1')
ax.plot([3, 2, 1], label='Line 2')
ax.legend(loc='upper right', frameon=False, fontsize=10)
```

### 2. Text

```python
ax.text(1, 1, 'Point A', fontsize=12)
ax.annotate('Peak', xy=(2, 3), xytext=(3, 4),
            arrowprops=dict(arrowstyle='->'))
```

### 3. Title Positioning

```python
ax.set_title('Title', loc='left', pad=20)
```
