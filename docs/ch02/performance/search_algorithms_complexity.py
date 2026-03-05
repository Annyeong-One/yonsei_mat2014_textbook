"""
Search Algorithms and Time Complexity Visualization

This tutorial demonstrates two fundamental search algorithms and visualizes
the growth rates of common time complexity classes.

Topics covered:
- Sequential (linear) search: O(n)
- Binary search: O(log n) on sorted data
- Big-O complexity growth rate comparison

Based on concepts from Python-100-Days example01 and ch02/performance materials.
"""

from math import log2, factorial


# =============================================================================
# Example 1: Sequential Search - O(n)
# =============================================================================

def sequential_search(items: list, target) -> int:
    """Search for target by checking each element one by one.

    Time Complexity: O(n) - must check every element in worst case.
    Best for: unsorted data, small lists.

    >>> sequential_search([35, 97, 12, 68, 55], 12)
    2
    >>> sequential_search([35, 97, 12, 68, 55], 99)
    -1
    """
    for index, item in enumerate(items):
        if item == target:
            return index  # Early return on match
    return -1


# =============================================================================
# Example 2: Binary Search - O(log n)
# =============================================================================

def binary_search(items: list, target) -> int:
    """Search for target by repeatedly halving the search space.

    Requires: items must be sorted in ascending order.
    Time Complexity: O(log n) - halves search space each step.

    >>> binary_search([12, 35, 40, 55, 68, 73, 81, 97], 55)
    3
    >>> binary_search([12, 35, 40, 55, 68, 73, 81, 97], 99)
    -1
    """
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > items[mid]:
            start = mid + 1
        elif target < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


# =============================================================================
# Example 3: Comparing Search Performance
# =============================================================================

def compare_searches():
    """Compare sequential vs binary search performance."""
    import time

    data = list(range(1_000_000))  # sorted list of 1M elements
    target = 999_999  # worst case for sequential

    # Sequential search
    start = time.perf_counter()
    result1 = sequential_search(data, target)
    seq_time = time.perf_counter() - start

    # Binary search
    start = time.perf_counter()
    result2 = binary_search(data, target)
    bin_time = time.perf_counter() - start

    print("=== Search Performance Comparison (1,000,000 elements) ===")
    print(f"Sequential search: found at index {result1}, time = {seq_time:.6f}s")
    print(f"Binary search:     found at index {result2}, time = {bin_time:.6f}s")
    print(f"Speedup: {seq_time / bin_time:.1f}x faster")
    print()


# =============================================================================
# Example 4: Big-O Complexity Classes
# =============================================================================

def print_complexity_table():
    """Display a table showing how different complexity classes grow.

    Common complexity classes (from fastest to slowest):
    O(1)        - Constant:    Hash table lookup
    O(log n)    - Logarithmic: Binary search
    O(n)        - Linear:      Sequential search
    O(n log n)  - Linearithmic: Merge sort, quick sort
    O(n^2)      - Quadratic:   Bubble sort, selection sort
    O(n^3)      - Cubic:       Matrix multiplication (naive)
    O(2^n)      - Exponential: Recursive fibonacci (naive)
    O(n!)       - Factorial:   Travelling salesman (brute force)
    """
    print("=== Big-O Complexity Growth Table ===")
    print(f"{'n':>4} | {'log n':>8} | {'n':>8} | {'n log n':>10} | "
          f"{'n^2':>10} | {'n^3':>12} | {'2^n':>12} | {'n!':>14}")
    print("-" * 90)

    for n in range(1, 11):
        log_n = log2(n) if n > 0 else 0
        n_log_n = n * log2(n) if n > 0 else 0
        n_sq = n ** 2
        n_cube = n ** 3
        two_n = 2 ** n
        n_fact = factorial(n)
        print(f"{n:>4} | {log_n:>8.2f} | {n:>8} | {n_log_n:>10.2f} | "
              f"{n_sq:>10} | {n_cube:>12} | {two_n:>12} | {n_fact:>14}")
    print()


# =============================================================================
# Example 5: Complexity Visualization (requires matplotlib + numpy)
# =============================================================================

def plot_complexity_growth():
    """Visualize how different complexity classes grow with n.

    This creates a plot comparing O(log n), O(n), O(n log n),
    O(n^2), O(n^3), O(2^n), and O(n!) growth rates.
    """
    try:
        from matplotlib import pyplot as plt
        import numpy as np
    except ImportError:
        print("matplotlib and numpy required for plotting")
        return

    num = 6
    x = list(range(1, num + 1))

    complexities = {
        'O(log n)':    [log2(n) for n in x],
        'O(n)':        x,
        'O(n log n)':  [n * log2(n) for n in x],
        'O(n²)':       [n ** 2 for n in x],
        'O(n³)':       [n ** 3 for n in x],
        'O(2ⁿ)':       [2 ** n for n in x],
        'O(n!)':       [factorial(n) for n in x],
    }

    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    fig, ax = plt.subplots(figsize=(10, 6))

    for (label, y_data), style in zip(complexities.items(), styles):
        ax.plot(x, y_data, style, label=label)

    ax.set_xlabel('Input Size (n)')
    ax.set_ylabel('Operations')
    ax.set_title('Time Complexity Growth Rates')
    ax.legend()
    ax.set_xticks(np.arange(1, num + 1, step=1))
    ax.set_yticks(np.arange(0, 751, step=50))
    plt.tight_layout()
    plt.show()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    compare_searches()
    print_complexity_table()
    # Uncomment to see the plot:
    # plot_complexity_growth()
