"""
Matplotlib Tutorial - Beginner Level
=====================================
Topic: Introduction to Matplotlib and First Plots
Author: Educational Python Course
Level: Beginner

Learning Objectives:
-------------------
1. Understand what matplotlib is and its purpose
2. Learn to import matplotlib.pyplot
3. Create your first simple plot
4. Understand the figure and show() function
5. Basic line plotting with plot()

Prerequisites:
-------------
- Basic Python knowledge
- NumPy basics (arrays)
"""

# ============================================================================
# SECTION 1: Introduction to Matplotlib
# ============================================================================

if __name__ == "__main__":

    """
    What is Matplotlib?
    ------------------
    Matplotlib is a comprehensive library for creating static, animated, and 
    interactive visualizations in Python. It is one of the most widely used 
    plotting libraries in the scientific Python ecosystem.

    Key Features:
    - Create publication-quality figures
    - Support for various plot types (line, bar, scatter, histogram, etc.)
    - Extensive customization options
    - Integration with NumPy and Pandas
    - Two different plotting interfaces: MATLAB-style and Object-Oriented style
    """

    # ============================================================================
    # SECTION 2: Importing Matplotlib
    # ============================================================================

    # Standard way to import matplotlib's plotting interface
    # 'plt' is the conventional alias used by the community
    import matplotlib.pyplot as plt
    import numpy as np  # We'll use numpy to generate data

    # ============================================================================
    # SECTION 3: Your First Plot - Simple Line
    # ============================================================================

    # Create some simple data
    # x-coordinates: 0, 1, 2, 3, 4
    x = [0, 1, 2, 3, 4]
    # y-coordinates: 0, 1, 4, 9, 16 (these are squares: 0^2, 1^2, 2^2, 3^2, 4^2)
    y = [0, 1, 4, 9, 16]

    # Create a plot
    # plot() is the most basic plotting function
    # It connects points with lines by default
    plt.plot(x, y)

    # Display the plot
    # show() is required to actually display the figure window
    # Without this, the plot exists in memory but won't be visible
    plt.show()

    # NOTE: After show() is called, the figure is displayed and then cleared
    # If you want to add more to the same figure, do it before calling show()

    # ============================================================================
    # SECTION 4: Adding Labels and Title
    # ============================================================================

    # Let's create a more informative plot
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]

    # Create the plot
    plt.plot(x, y)

    # Add x-axis label
    # The label appears below the x-axis
    plt.xlabel('Input Value')

    # Add y-axis label
    # The label appears to the left of the y-axis
    plt.ylabel('Squared Value')

    # Add a title
    # The title appears at the top of the plot
    plt.title('Simple Quadratic Function: y = x²')

    # Display the plot
    plt.show()

    # ============================================================================
    # SECTION 5: Using NumPy for More Data Points
    # ============================================================================

    # When plotting smooth curves, we need many points
    # NumPy's linspace() creates evenly spaced points

    # Create 100 points between 0 and 4
    # linspace(start, stop, num_points)
    x = np.linspace(0, 4, 100)

    # Calculate y values (each x squared)
    y = x ** 2

    # Create the plot
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y = x²')
    plt.title('Smooth Quadratic Function (100 points)')

    # Display the plot
    plt.show()

    # ============================================================================
    # SECTION 6: Customizing Line Appearance
    # ============================================================================

    # Generate data
    x = np.linspace(0, 4, 100)
    y = x ** 2

    # Create plot with custom line properties
    # 'r' = red color
    # '--' = dashed line style
    # linewidth controls the thickness of the line
    plt.plot(x, y, 'r--', linewidth=2)

    # You can also specify properties using keyword arguments
    # This is more explicit and readable
    # plt.plot(x, y, color='red', linestyle='--', linewidth=2)

    plt.xlabel('x')
    plt.ylabel('y = x²')
    plt.title('Customized Line: Red and Dashed')

    plt.show()

    # ============================================================================
    # SECTION 7: Multiple Lines on Same Plot
    # ============================================================================

    # Generate x data
    x = np.linspace(0, 4, 100)

    # Generate multiple y datasets
    y1 = x ** 2      # Quadratic
    y2 = x ** 3      # Cubic
    y3 = np.sqrt(x)  # Square root

    # Plot all three lines
    # Each plot() call adds a new line to the same figure
    plt.plot(x, y1, 'r-', linewidth=2, label='y = x²')   # Red solid line
    plt.plot(x, y2, 'b--', linewidth=2, label='y = x³')  # Blue dashed line
    plt.plot(x, y3, 'g:', linewidth=2, label='y = √x')   # Green dotted line

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Multiple Functions on Same Plot')

    # Add legend
    # legend() creates a box showing what each line represents
    # The labels come from the 'label' parameter in plot()
    # loc='best' automatically chooses the best position
    plt.legend(loc='best')

    plt.show()

    # ============================================================================
    # SECTION 8: Common Line Styles and Colors
    # ============================================================================

    """
    Common Color Codes:
    ------------------
    'r' = red
    'g' = green
    'b' = blue
    'c' = cyan
    'm' = magenta
    'y' = yellow
    'k' = black
    'w' = white

    You can also use full names: 'red', 'green', 'blue', etc.
    Or hex codes: '#FF0000' for red, '#00FF00' for green, etc.

    Common Line Styles:
    ------------------
    '-'  = solid line (default)
    '--' = dashed line
    ':'  = dotted line
    '-.' = dash-dot line

    Common Markers:
    --------------
    'o'  = circle
    's'  = square
    '^'  = triangle up
    'v'  = triangle down
    '*'  = star
    '+'  = plus
    'x'  = x mark
    'D'  = diamond

    You can combine them: 'ro-' = red circles connected by solid line
    """

    # Example demonstrating various styles
    x = np.linspace(0, 10, 20)

    plt.plot(x, x, 'ro-', label='Red circles, solid')
    plt.plot(x, x + 2, 'bs--', label='Blue squares, dashed')
    plt.plot(x, x + 4, 'g^:', label='Green triangles, dotted')
    plt.plot(x, x + 6, 'k*-.', label='Black stars, dash-dot')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Different Line Styles, Colors, and Markers')
    plt.legend()
    plt.grid(True)  # Add grid for better readability

    plt.show()

    # ============================================================================
    # SECTION 9: Saving Figures
    # ============================================================================

    # Create a plot
    x = np.linspace(0, 4, 100)
    y = x ** 2

    plt.plot(x, y, 'b-', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y = x²')
    plt.title('Quadratic Function')

    # Save the figure before showing it
    # savefig() saves the current figure to a file
    # Common formats: .png, .pdf, .svg, .jpg
    plt.savefig('my_first_plot.png', dpi=300, bbox_inches='tight')
    # dpi = dots per inch (resolution)
    # bbox_inches='tight' removes excess white space

    # You can still show the figure after saving
    plt.show()

    print("Figure saved as 'my_first_plot.png'")

    # ============================================================================
    # KEY TAKEAWAYS
    # ============================================================================

    """
    1. Import matplotlib.pyplot as plt
    2. Use plt.plot(x, y) to create line plots
    3. Add labels with xlabel(), ylabel(), and title()
    4. Use show() to display the plot
    5. Customize lines with color, style, and width parameters
    6. Add legends with plt.legend() when plotting multiple lines
    7. Save figures with savefig() before show()
    8. MATLAB-style (plt.plot, plt.xlabel, etc.) is simple for quick plots
    """
