"""
MATPLOTLIB QUICK REFERENCE CHEAT SHEET
======================================

This is a condensed reference for quick lookup while coding.
For detailed explanations, see the full course files.
"""

# ============================================================================
# IMPORTS
# ============================================================================

import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# TWO PLOTTING STYLES
# ============================================================================

# MATLAB-Style (Simple, for quick plots)
plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

# OOP-Style (Recommended for complex plots)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Title')
plt.show()

# ============================================================================
# METHOD NAME DIFFERENCES
# ============================================================================

"""
MATLAB-style              OOP-style
-------------            ----------------
plt.xlabel()      →      ax.set_xlabel()
plt.ylabel()      →      ax.set_ylabel()
plt.title()       →      ax.set_title()
plt.xlim()        →      ax.set_xlim()
plt.ylim()        →      ax.set_ylim()
plt.xticks()      →      ax.set_xticks()
plt.yticks()      →      ax.set_yticks()
plt.legend()      →      ax.legend()        # SAME
plt.grid()        →      ax.grid()          # SAME
plt.plot()        →      ax.plot()          # SAME
"""

# ============================================================================
# CREATING SUBPLOTS
# ============================================================================

# Single plot
fig, ax = plt.subplots()

# Multiple plots (2 rows, 3 columns)
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
# axes.shape = (2, 3)
# Access: axes[row, col]

# With shared axes
fig, axes = plt.subplots(2, 1, sharex=True)

# Flatten for easy iteration
axes_flat = axes.flatten()

# ============================================================================
# PLOT() - LINE PLOTS
# ============================================================================

# Basic
ax.plot(x, y)

# With format string: '[marker][line][color]'
ax.plot(x, y, 'ro-')   # Red circles with solid line
ax.plot(x, y, 'b--')   # Blue dashed line
ax.plot(x, y, 'g:s')   # Green dotted with squares

# With keyword arguments
ax.plot(x, y, 
        color='red',              # or 'r' or '#FF0000'
        linestyle='--',           # or '--'
        linewidth=2,              # or lw
        marker='o',
        markersize=8,             # or ms
        markerfacecolor='blue',   # or mfc
        markeredgecolor='black',  # or mec
        alpha=0.7,
        label='My Line')

# Multiple lines
ax.plot(x, y1, 'r-', label='Line 1')
ax.plot(x, y2, 'b--', label='Line 2')
ax.legend()

# ============================================================================
# HIST() - HISTOGRAMS
# ============================================================================

# Basic histogram
n, bins, patches = ax.hist(data, bins=30)

# With explicit bin edges (can be unequal!)
bins = [0, 1, 2, 5, 10]
n, bins, patches = ax.hist(data, bins=bins)

# Probability density (area = 1.0)
n, bins, patches = ax.hist(data, bins=30, density=True)

# Customization
ax.hist(data,
        bins=30,                  # int or array
        density=False,            # False=counts, True=density
        cumulative=False,         # False or True
        histtype='bar',           # 'bar', 'step', 'stepfilled'
        color='blue',
        edgecolor='black',
        alpha=0.7,
        label='My Data')

# Return values
n       # Array of counts or densities (length = num_bins)
bins    # Array of bin edges (length = num_bins + 1)
patches # List of bar objects

# Key formula for density
# density[i] = count[i] / (N × bin_width[i])

# ============================================================================
# COLORS
# ============================================================================

# Short codes
'r' 'g' 'b' 'c' 'm' 'y' 'k' 'w'

# Full names
'red' 'green' 'blue' 'cyan' 'magenta' 'yellow' 'black' 'white'

# Hex codes
'#FF0000'  # Red
'#00FF00'  # Green
'#0000FF'  # Blue

# RGB tuple (0-1)
(1.0, 0.0, 0.0)  # Red

# RGBA tuple (0-1, with alpha)
(1.0, 0.0, 0.0, 0.5)  # Semi-transparent red

# ============================================================================
# LINE STYLES
# ============================================================================

'-'   # Solid
'--'  # Dashed
':'   # Dotted
'-.'  # Dash-dot
''    # No line

# ============================================================================
# MARKERS
# ============================================================================

'.'  # Point
'o'  # Circle
's'  # Square
'^'  # Triangle up
'v'  # Triangle down
'*'  # Star
'+'  # Plus
'x'  # X
'D'  # Diamond

# ============================================================================
# CUSTOMIZATION
# ============================================================================

# Labels and title
ax.set_xlabel('X Label', fontsize=12)
ax.set_ylabel('Y Label', fontsize=12)
ax.set_title('Title', fontsize=14, fontweight='bold')

# Limits
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Ticks
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['0', '2', '4', '6', '8', '10'])

# Grid
ax.grid(True)
ax.grid(True, alpha=0.3, linestyle='--')

# Legend
ax.legend()
ax.legend(loc='upper right', fontsize=12, framealpha=0.9)

# Spines (hide top and right)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ============================================================================
# TEXT AND ANNOTATIONS
# ============================================================================

# Simple text
ax.text(5, 0.5, 'My text', fontsize=12)

# Text with box
ax.text(5, 0.5, 'Text', bbox=dict(boxstyle='round', facecolor='wheat'))

# Annotation with arrow
ax.annotate('Point of interest',
            xy=(5, 0.5),      # Point to annotate
            xytext=(6, 0.8),  # Text position
            arrowprops=dict(arrowstyle='->'))

# ============================================================================
# FIGURE AND AXES
# ============================================================================

# Figure size
fig, ax = plt.subplots(figsize=(10, 6))  # Width, height in inches

# DPI (resolution)
fig, ax = plt.subplots(dpi=150)

# Tight layout (auto-adjust spacing)
plt.tight_layout()

# Save figure
plt.savefig('figure.png', dpi=300, bbox_inches='tight')

# ============================================================================
# GRIDSPEC (COMPLEX LAYOUTS)
# ============================================================================

import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 3, figure=fig)

# Span multiple cells
ax1 = fig.add_subplot(gs[0, :])    # Row 0, all columns
ax2 = fig.add_subplot(gs[1:, 0])   # Rows 1-2, column 0
ax3 = fig.add_subplot(gs[1, 1:])   # Row 1, columns 1-2

# ============================================================================
# COMMON PATTERNS
# ============================================================================

# Single plot with customization
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2, label='Data')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('My Plot', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Histogram with density and PDF overlay
fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(data, bins=30, density=True, alpha=0.7, label='Data')
ax.plot(x_pdf, pdf, 'r-', linewidth=3, label='Theory')
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.legend()
plt.show()

# Multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for i, ax in enumerate(axes.flatten()):
    ax.plot(x, y[i])
    ax.set_title(f'Plot {i+1}')
plt.tight_layout()
plt.show()

# ============================================================================
# DEBUGGING CHECKLIST
# ============================================================================

"""
Common Mistakes:
1. Using plt.xlabel() instead of ax.set_xlabel() in OOP style
2. Forgetting that axes[row, col] (not axes[col, row])
3. Not unpacking hist() return values when needed
4. Confusing density=True (area=1) with density=False (counts)
5. Accessing axes[2, 1] when shape is (2, 2) (out of bounds)
6. Not calling plt.show() at the end
7. Forgetting that bins array has length = num_bins + 1
"""

# ============================================================================
# QUICK DIAGNOSIS
# ============================================================================

"""
Error: 'AxesSubplot' object has no attribute 'xlabel'
Fix: Use ax.set_xlabel() not ax.xlabel()

Error: IndexError: index 2 is out of bounds for axis 0 with size 2
Fix: Check axes.shape, remember axes[row, col]

Issue: Histogram looks weird
Check: bins parameter, try different values

Issue: Want to overlay PDF but scales don't match
Fix: Use density=True in hist()

Issue: Can't access individual subplots
Fix: Use axes.flatten() to convert to 1D array
"""

print("Cheat sheet loaded! Use as quick reference while coding.")
