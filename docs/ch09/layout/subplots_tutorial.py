"""
Matplotlib Tutorial - Beginner Level
=====================================
Topic: Subplots and Understanding Axes as NumPy Array
Author: Educational Python Course
Level: Beginner

Learning Objectives:
-------------------
1. Create multiple subplots using plt.subplots()
2. Understand that axes is a NumPy array
3. Learn the counter-intuitive shape of the axes array
4. Access individual axes for plotting
5. Master the indexing of axes arrays

Prerequisites:
-------------
- Completion of 01_introduction_and_first_plot.py
- Completion of 02_two_plotting_styles.py
- Basic NumPy array indexing knowledge

CRITICAL CONCEPT:
----------------
When using fig, axes = plt.subplots(nrows, ncols), the 'axes' object is
a NumPy array. Its shape and indexing can be counter-intuitive at first,
but once you understand it, it becomes very handy!
"""

import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# SECTION 1: Creating a Single Subplot (Review)
# ============================================================================

if __name__ == "__main__":

    """
    When you create a single plot with plt.subplots(), you get:
    - fig: a Figure object (the container)
    - ax: a single Axes object (the plot area)
    """

    fig, ax = plt.subplots()

    print(f"Type of ax (single plot): {type(ax)}")
    print(f"Is ax a numpy array? {isinstance(ax, np.ndarray)}")
    # Output: False - with single subplot, ax is NOT an array

    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x))
    ax.set_title('Single Subplot')
    plt.show()

    # ============================================================================
    # SECTION 2: Creating Multiple Subplots (1 Row, Multiple Columns)
    # ============================================================================

    """
    When you create multiple subplots, plt.subplots() returns:
    - fig: a Figure object
    - axes: a NumPy array of Axes objects (NOT a single Axes!)
    """

    # Create 1 row, 3 columns of subplots
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    print("\n" + "=" * 70)
    print("1 ROW, 3 COLUMNS")
    print("=" * 70)
    print(f"Type of axes: {type(axes)}")
    print(f"Is axes a numpy array? {isinstance(axes, np.ndarray)}")
    print(f"Shape of axes: {axes.shape}")  # (3,) - a 1D array with 3 elements
    print(f"Number of axes: {len(axes)}")

    # axes is a 1D NumPy array: [ax0, ax1, ax2]
    # Access each subplot using index: axes[0], axes[1], axes[2]

    x = np.linspace(0, 10, 100)

    # Plot on first subplot (index 0)
    axes[0].plot(x, np.sin(x))
    axes[0].set_title('sin(x)')

    # Plot on second subplot (index 1)
    axes[1].plot(x, np.cos(x))
    axes[1].set_title('cos(x)')

    # Plot on third subplot (index 2)
    axes[2].plot(x, np.tan(x))
    axes[2].set_ylim(-5, 5)  # Limit y-axis for tan
    axes[2].set_title('tan(x)')

    plt.tight_layout()  # Automatically adjust spacing to prevent overlap
    plt.show()

    # ============================================================================
    # SECTION 3: Creating Multiple Subplots (Multiple Rows, 1 Column)
    # ============================================================================

    # Create 3 rows, 1 column of subplots
    fig, axes = plt.subplots(3, 1, figsize=(6, 8))

    print("\n" + "=" * 70)
    print("3 ROWS, 1 COLUMN")
    print("=" * 70)
    print(f"Shape of axes: {axes.shape}")  # (3,) - still a 1D array!
    print(f"Number of axes: {len(axes)}")

    # axes is still a 1D array: [ax0, ax1, ax2]
    # Even though the visual layout is vertical!

    x = np.linspace(0, 10, 100)

    # Plot on first subplot (top)
    axes[0].plot(x, x)
    axes[0].set_title('Linear: y = x')

    # Plot on second subplot (middle)
    axes[1].plot(x, x**2)
    axes[1].set_title('Quadratic: y = x²')

    # Plot on third subplot (bottom)
    axes[2].plot(x, x**3)
    axes[2].set_title('Cubic: y = x³')

    plt.tight_layout()
    plt.show()

    # ============================================================================
    # SECTION 4: The Counter-Intuitive Part - 2D Grid of Subplots
    # ============================================================================

    """
    CRITICAL: Understanding the shape of axes in a 2D grid

    When you create a 2D grid: plt.subplots(nrows, ncols)
    The axes array has shape (nrows, ncols)

    COUNTER-INTUITIVE PART:
    - First index = row number (vertical position)
    - Second index = column number (horizontal position)
    - This is like matrix indexing: axes[row, col]

    Visual Layout:           Array Indexing:
    -------------           ----------------
    [plot1] [plot2]   ==>   axes[0,0]  axes[0,1]
    [plot3] [plot4]   ==>   axes[1,0]  axes[1,1]

    The first index (row) changes the VERTICAL position
    The second index (col) changes the HORIZONTAL position

    This matches NumPy array conventions but can feel backwards at first!
    """

    # Create 2 rows, 3 columns
    fig, axes = plt.subplots(2, 3, figsize=(12, 6))

    print("\n" + "=" * 70)
    print("2 ROWS, 3 COLUMNS - THE IMPORTANT CASE")
    print("=" * 70)
    print(f"Type of axes: {type(axes)}")
    print(f"Shape of axes: {axes.shape}")  # (2, 3) - a 2D array
    print(f"axes is a 2D array with shape (rows, cols)")
    print()
    print("Visual Layout:")
    print("  Col 0    Col 1    Col 2")
    print("Row 0: [0,0]   [0,1]   [0,2]")
    print("Row 1: [1,0]   [1,1]   [1,2]")

    # Let's number each subplot to see the indexing clearly
    for i in range(2):  # rows
        for j in range(3):  # cols
            axes[i, j].text(0.5, 0.5, f'axes[{i},{j}]',
                            ha='center', va='center',
                            fontsize=20, transform=axes[i, j].transAxes)
            axes[i, j].set_title(f'Row {i}, Col {j}')

    plt.tight_layout()
    plt.show()

    # ============================================================================
    # SECTION 5: Practical Example - Plotting Data in 2D Grid
    # ============================================================================

    # Create a 2x2 grid of different functions
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    print("\n" + "=" * 70)
    print("2x2 GRID EXAMPLE")
    print("=" * 70)
    print(f"axes.shape = {axes.shape}")

    x = np.linspace(0, 10, 100)

    # Top-left: axes[0, 0] (row 0, col 0)
    axes[0, 0].plot(x, np.sin(x), 'r-')
    axes[0, 0].set_title('Top-Left: sin(x)')
    axes[0, 0].set_ylabel('Row 0')

    # Top-right: axes[0, 1] (row 0, col 1)
    axes[0, 1].plot(x, np.cos(x), 'b-')
    axes[0, 1].set_title('Top-Right: cos(x)')

    # Bottom-left: axes[1, 0] (row 1, col 0)
    axes[1, 0].plot(x, np.exp(-x/5) * np.sin(x), 'g-')
    axes[1, 0].set_title('Bottom-Left: Damped sine')
    axes[1, 0].set_ylabel('Row 1')
    axes[1, 0].set_xlabel('Col 0')

    # Bottom-right: axes[1, 1] (row 1, col 1)
    axes[1, 1].plot(x, np.log(x + 1), 'm-')
    axes[1, 1].set_title('Bottom-Right: log(x+1)')
    axes[1, 1].set_xlabel('Col 1')

    plt.tight_layout()
    plt.show()

    # ============================================================================
    # SECTION 6: Why This Shape Convention Makes Sense
    # ============================================================================

    """
    Why axes[row, col] instead of axes[col, row]?

    Reason: It matches NumPy and mathematical matrix conventions!

    In NumPy arrays and matrices:
    - First index = row (vertical position)
    - Second index = column (horizontal position)
    - This is standard in linear algebra

    Example with a NumPy array:
    """

    # Create a 3x4 array
    arr = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])

    print("\n" + "=" * 70)
    print("NUMPY ARRAY INDEXING ANALOGY")
    print("=" * 70)
    print("Array:")
    print(arr)
    print()
    print(f"arr[0, 0] = {arr[0, 0]} (top-left)")
    print(f"arr[0, 3] = {arr[0, 3]} (top-right)")
    print(f"arr[2, 0] = {arr[2, 0]} (bottom-left)")
    print(f"arr[2, 3] = {arr[2, 3]} (bottom-right)")
    print()
    print("Same logic applies to axes[row, col]!")

    # ============================================================================
    # SECTION 7: Flattening Axes Array for Easy Iteration
    # ============================================================================

    """
    Sometimes you want to iterate over all subplots without worrying about
    row/column indexing. You can flatten the axes array!
    """

    # Create a 2x3 grid
    fig, axes = plt.subplots(2, 3, figsize=(12, 6))

    print("\n" + "=" * 70)
    print("FLATTENING AXES ARRAY")
    print("=" * 70)
    print(f"Original shape: {axes.shape}")  # (2, 3)

    # Flatten to 1D array
    axes_flat = axes.flatten()
    print(f"Flattened shape: {axes_flat.shape}")  # (6,)

    # Now you can iterate easily
    x = np.linspace(0, 10, 100)
    functions = [
        ('sin(x)', np.sin(x)),
        ('cos(x)', np.cos(x)),
        ('sin(2x)', np.sin(2*x)),
        ('cos(2x)', np.cos(2*x)),
        ('sin(x/2)', np.sin(x/2)),
        ('cos(x/2)', np.cos(x/2))
    ]

    for ax, (name, y) in zip(axes_flat, functions):
        ax.plot(x, y)
        ax.set_title(name)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Alternative: Use ravel() instead of flatten()
    # ravel() is similar but returns a view when possible (more efficient)
    axes_flat = axes.ravel()

    # ============================================================================
    # SECTION 8: Common Patterns and Best Practices
    # ============================================================================

    """
    Common Patterns:
    ---------------
    """

    # Pattern 1: Single subplot (no array)
    fig, ax = plt.subplots()
    # ax is a single Axes object, NOT an array

    # Pattern 2: One row or one column (1D array)
    fig, axes = plt.subplots(1, 3)  # shape (3,)
    fig, axes = plt.subplots(3, 1)  # shape (3,)
    # axes is a 1D array, use axes[i]

    # Pattern 3: Grid (2D array)
    fig, axes = plt.subplots(2, 3)  # shape (2, 3)
    # axes is a 2D array, use axes[i, j]

    # Pattern 4: Force axes to always be 2D (even for single row/column)
    fig, axes = plt.subplots(1, 3, squeeze=False)  # shape (1, 3)
    fig, axes = plt.subplots(3, 1, squeeze=False)  # shape (3, 1)
    # squeeze=False prevents reduction to 1D

    print("\n" + "=" * 70)
    print("EFFECT OF squeeze PARAMETER")
    print("=" * 70)

    fig, axes1 = plt.subplots(1, 3)  # Default: squeeze=True
    fig, axes2 = plt.subplots(1, 3, squeeze=False)

    print(f"With squeeze=True (default):  axes.shape = {axes1.shape}")  # (3,)
    print(f"With squeeze=False:           axes.shape = {axes2.shape}")  # (1, 3)

    plt.close('all')  # Close the figures we just created

    # ============================================================================
    # SECTION 9: Handling Different Cases with Robust Code
    # ============================================================================

    """
    Problem: You might not know in advance if axes will be:
    - A single Axes object (1 subplot)
    - A 1D array (one row or column)
    - A 2D array (grid)

    Solution: Always use np.atleast_2d() or ravel() to standardize
    """

    def plot_on_grid(nrows, ncols):
        """
        Demonstrates robust handling of axes regardless of shape
        """
        fig, axes = plt.subplots(nrows, ncols, figsize=(4*ncols, 3*nrows))

        # Convert to 1D array for easy iteration
        # This works regardless of whether axes is single object, 1D, or 2D
        if nrows == 1 and ncols == 1:
            axes_list = [axes]  # Single axes, wrap in list
        else:
            axes_list = axes.flatten()  # Array of axes, flatten

        # Now we can safely iterate
        for i, ax in enumerate(axes_list):
            x = np.linspace(0, 10, 100)
            ax.plot(x, np.sin((i+1)*x))
            ax.set_title(f'Subplot {i+1}')

        plt.tight_layout()
        return fig, axes

    # Test with different configurations
    print("\n" + "=" * 70)
    print("TESTING ROBUST CODE")
    print("=" * 70)

    fig1, ax1 = plot_on_grid(1, 1)  # Single plot
    print(f"1x1: type(axes) = {type(ax1)}")

    fig2, ax2 = plot_on_grid(2, 2)  # 2x2 grid
    print(f"2x2: axes.shape = {ax2.shape}")

    plt.show()

    # ============================================================================
    # KEY TAKEAWAYS
    # ============================================================================

    """
    1. When using plt.subplots(nrows, ncols), axes is a NumPy array
    2. Shape of axes array: (nrows, ncols)
    3. Indexing: axes[row, col] where row is vertical, col is horizontal
    4. This matches NumPy/matrix conventions (row first, column second)
    5. For single row/column, axes is 1D: use axes[i]
    6. For grids, axes is 2D: use axes[i, j]
    7. Use flatten() or ravel() to convert to 1D for easy iteration
    8. Use squeeze=False to keep axes as 2D even for single row/column
    9. Once you understand the convention, it's very handy!

    Common Gotchas:
    --------------
    ✗ axes[col, row]  # WRONG! Don't think horizontally first
    ✓ axes[row, col]  # CORRECT! Think vertically first (like matrices)

    Quick Reference:
    ---------------
    plt.subplots(1, 1)     → ax (single Axes object)
    plt.subplots(1, n)     → axes (1D array, shape (n,))
    plt.subplots(n, 1)     → axes (1D array, shape (n,))
    plt.subplots(m, n)     → axes (2D array, shape (m, n))
    """

    print("\n" + "=" * 70)
    print("VISUAL SUMMARY: axes[row, col]")
    print("=" * 70)
    print("    Col 0      Col 1      Col 2")
    print("Row 0: [0,0]     [0,1]     [0,2]")
    print("Row 1: [1,0]     [1,1]     [1,2]")
    print()
    print("First index increases DOWN (rows)")
    print("Second index increases RIGHT (columns)")
    print("=" * 70)
