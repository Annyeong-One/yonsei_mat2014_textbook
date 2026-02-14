"""
Matplotlib Tutorial - Beginner Level
=====================================
Topic: Two Plotting Styles - MATLAB Style vs Object-Oriented Style
Author: Educational Python Course
Level: Beginner

Learning Objectives:
-------------------
1. Understand the difference between MATLAB-style and OOP-style
2. Learn when to use each style
3. Understand the concept of Figure and Axes objects
4. Create simple plots using both styles
5. Recognize the advantages of each approach

Prerequisites:
-------------
- Completion of 01_introduction_and_first_plot.py
- Basic understanding of object-oriented programming concepts
"""

import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# SECTION 1: Introduction to Two Plotting Styles
# ============================================================================

"""
Matplotlib provides TWO different interfaces for creating plots:

1. MATLAB-Style (Pyplot Interface)
   - Uses plt.plot(), plt.xlabel(), plt.title(), etc.
   - Simpler and more intuitive for beginners
   - Good for quick, simple plots
   - Similar to MATLAB's plotting commands
   - Implicitly works on the "current" figure and axes

2. Object-Oriented Style (OO Interface)
   - Uses explicit Figure and Axes objects
   - More verbose but more powerful
   - Better for complex plots with multiple subplots
   - Recommended for more control and clarity
   - Explicitly specify which axes to work with

IMPORTANT: Both styles produce the same results, but OOP style gives you
more control and is better for complex visualizations.
"""

# ============================================================================
# SECTION 2: MATLAB-Style Plotting (Pyplot Interface)
# ============================================================================

print("=" * 70)
print("MATLAB-STYLE PLOTTING")
print("=" * 70)

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# MATLAB-style: Use plt.* functions directly
# These functions operate on the "current" figure and axes
plt.figure()  # Create a new figure (optional, but explicit)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('MATLAB-Style Plot')
plt.grid(True)
plt.show()

"""
What's happening behind the scenes:
- plt.plot() automatically creates a figure and axes if they don't exist
- plt.xlabel() adds a label to the current axes
- All plt.* functions work on the "current" active figure/axes
- This is convenient for simple plots but can be confusing with multiple plots
"""

# ============================================================================
# SECTION 3: Object-Oriented Style (OOP Interface)
# ============================================================================

print("=" * 70)
print("OBJECT-ORIENTED STYLE PLOTTING")
print("=" * 70)

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# OOP-style: Create explicit Figure and Axes objects
# fig is the entire window or page
# ax is a single plot area within the figure
fig, ax = plt.subplots()

# Now we call methods on the axes object (ax)
# Notice: ax.plot() instead of plt.plot()
ax.plot(x, y)
ax.set_xlabel('x')  # Note: set_xlabel, not xlabel
ax.set_ylabel('sin(x)')  # Note: set_ylabel, not ylabel
ax.set_title('Object-Oriented Style Plot')  # Note: set_title, not title
ax.grid(True)

plt.show()

"""
What's different:
- We explicitly create fig and ax objects using plt.subplots()
- We call methods on ax (the axes object), not plt
- Method names have 'set_' prefix: set_xlabel, set_ylabel, set_title
- This gives us explicit control over which axes we're modifying
"""

# ============================================================================
# SECTION 4: Method Name Differences - IMPORTANT!
# ============================================================================

"""
CRITICAL: Method names change between MATLAB-style and OOP-style!

MATLAB-Style (plt.*)          |  OOP-Style (ax.*)
------------------------------|----------------------------------
plt.xlabel()                  |  ax.set_xlabel()
plt.ylabel()                  |  ax.set_ylabel()
plt.title()                   |  ax.set_title()
plt.xlim()                    |  ax.set_xlim()
plt.ylim()                    |  ax.set_ylim()
plt.xticks()                  |  ax.set_xticks()
plt.yticks()                  |  ax.set_yticks()
plt.legend()                  |  ax.legend() (same name!)
plt.grid()                    |  ax.grid() (same name!)
plt.plot()                    |  ax.plot() (same name!)

Rule of Thumb:
- In OOP-style, most "setting" functions add a 'set_' prefix
- Some functions keep the same name (plot, legend, grid, etc.)
"""

# ============================================================================
# SECTION 5: Side-by-Side Comparison
# ============================================================================

print("=" * 70)
print("SIDE-BY-SIDE COMPARISON")
print("=" * 70)

x = np.linspace(0, 10, 100)
y = np.cos(x)

# --------------------
# MATLAB-Style
# --------------------
plt.figure(figsize=(6, 4))  # figsize in inches (width, height)
plt.plot(x, y, 'b-', linewidth=2)
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('MATLAB-Style: Cosine Function')
plt.grid(True, alpha=0.3)  # alpha controls transparency
plt.xlim(0, 10)  # Set x-axis limits
plt.ylim(-1.5, 1.5)  # Set y-axis limits
plt.show()

# --------------------
# OOP-Style (Equivalent)
# --------------------
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('x')
ax.set_ylabel('cos(x)')
ax.set_title('OOP-Style: Cosine Function')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
plt.show()

# Both produce identical results!

# ============================================================================
# SECTION 6: Understanding Figure and Axes Objects
# ============================================================================

"""
Key Concepts:
------------

Figure (fig):
- The entire window or page that contains your plot(s)
- Can contain one or more Axes
- Controls overall properties: size, DPI, background color
- Think of it as the canvas

Axes (ax):
- A single plot area within the Figure
- Contains the actual plot elements: lines, labels, ticks, etc.
- A Figure can have multiple Axes (subplots)
- Think of it as the drawing on the canvas

Hierarchy:
  Figure (the whole window)
    └── Axes (individual plot area)
          └── Plot elements (lines, markers, text, etc.)
"""

# Create a figure and axes explicitly
fig, ax = plt.subplots()

print(f"Type of fig: {type(fig)}")  # matplotlib.figure.Figure
print(f"Type of ax: {type(ax)}")    # matplotlib.axes._subplots.AxesSubplot

# You can access the figure from axes
print(f"ax.figure is fig: {ax.figure is fig}")  # True

# Plot something
x = np.linspace(0, 5, 50)
ax.plot(x, x**2, 'r-')
ax.set_title('Understanding Figure and Axes')

plt.show()

# ============================================================================
# SECTION 7: When to Use Each Style
# ============================================================================

"""
Use MATLAB-Style when:
---------------------
1. Creating quick, simple plots for exploration
2. You only need one plot
3. You're familiar with MATLAB
4. Code simplicity is more important than explicit control
5. Working interactively (Jupyter notebooks, IPython)

Use OOP-Style when:
------------------
1. Creating complex figures with multiple subplots
2. You need explicit control over which plot you're modifying
3. Writing functions that create plots
4. Building applications with embedded plots
5. You want clearer, more maintainable code
6. Working on larger projects (RECOMMENDED)

General Recommendation:
----------------------
- Learn both styles
- Use MATLAB-style for quick exploration
- Use OOP-style for production code and complex visualizations
- NEVER mix both styles in the same code (pick one and stick with it)
"""

# ============================================================================
# SECTION 8: Practical Example - Why OOP is Better for Multiple Plots
# ============================================================================

# Imagine you want to create two different plots
# With MATLAB-style, this can get confusing:

# MATLAB-style (works but less clear)
plt.figure(1)
x = np.linspace(0, 5, 50)
plt.plot(x, x**2)
plt.title('Figure 1: Quadratic')

plt.figure(2)
plt.plot(x, x**3)
plt.title('Figure 2: Cubic')

plt.figure(1)  # Go back to first figure
plt.xlabel('x')  # Add label to first figure

plt.show()

# OOP-style (clearer and more explicit)
x = np.linspace(0, 5, 50)

# Create first plot
fig1, ax1 = plt.subplots()
ax1.plot(x, x**2)
ax1.set_title('Figure 1: Quadratic')
ax1.set_xlabel('x')  # No confusion about which plot we're modifying

# Create second plot
fig2, ax2 = plt.subplots()
ax2.plot(x, x**3)
ax2.set_title('Figure 2: Cubic')
ax2.set_xlabel('x')

plt.show()

# With OOP style, it's always clear which axes object we're working with!

# ============================================================================
# SECTION 9: Converting Between Styles
# ============================================================================

"""
If you see MATLAB-style code, you can convert it to OOP-style:

MATLAB-Style:
------------
plt.plot(x, y)
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('My Title')
plt.show()

OOP-Style:
---------
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('My Title')
plt.show()

Just remember:
1. Create fig, ax first
2. Change plt.* to ax.*
3. Add 'set_' prefix for labels, title, limits, ticks
"""

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
1. Matplotlib has two styles: MATLAB-style (plt.*) and OOP-style (fig, ax)
2. Both produce identical results
3. OOP-style uses explicit Figure and Axes objects
4. Method names differ: plt.xlabel() vs ax.set_xlabel()
5. OOP-style is recommended for complex plots and maintainable code
6. MATLAB-style is good for quick, simple plots
7. Choose one style per script/project and be consistent
8. Understanding both styles helps you read others' code
"""

print("\n" + "=" * 70)
print("SUMMARY OF METHOD NAME DIFFERENCES")
print("=" * 70)
print("MATLAB-style          -->  OOP-style")
print("-" * 70)
print("plt.plot()            -->  ax.plot()")
print("plt.xlabel()          -->  ax.set_xlabel()")
print("plt.ylabel()          -->  ax.set_ylabel()")
print("plt.title()           -->  ax.set_title()")
print("plt.xlim()            -->  ax.set_xlim()")
print("plt.ylim()            -->  ax.set_ylim()")
print("plt.legend()          -->  ax.legend()")
print("plt.grid()            -->  ax.grid()")
print("=" * 70)
