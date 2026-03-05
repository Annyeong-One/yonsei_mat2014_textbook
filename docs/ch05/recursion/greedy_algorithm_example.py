"""
Greedy Algorithm: The Knapsack Problem

A greedy algorithm makes the locally optimal choice at each step,
hoping to find a global optimum. It doesn't always find the best
solution, but it finds a satisfactory one quickly.

Topics covered:
- Greedy strategy: best value-to-weight ratio first
- OOP with @property for computed attributes
- sorted() with custom key functions

Based on concepts from Python-100-Days example04 and ch05/recursion materials.
"""


# =============================================================================
# Example 1: Item Class with Computed Property
# =============================================================================

class Item:
    """An item with name, value, and weight.

    The value_per_weight property computes the efficiency ratio,
    which the greedy algorithm uses to prioritize items.
    """

    def __init__(self, name: str, value: float, weight: float):
        self.name = name
        self.value = value
        self.weight = weight

    @property
    def value_per_weight(self) -> float:
        """Value-to-weight ratio (higher = more efficient)."""
        return self.value / self.weight

    def __repr__(self):
        return (f"Item('{self.name}', value={self.value}, "
                f"weight={self.weight}, ratio={self.value_per_weight:.2f})")


# =============================================================================
# Example 2: Greedy Knapsack (0/1 variant)
# =============================================================================

def greedy_knapsack(items: list[Item], capacity: float) -> tuple[list[Item], float]:
    """Select items using greedy strategy: best value/weight ratio first.

    This is the 0/1 knapsack variant - items cannot be split.
    The greedy approach doesn't guarantee the optimal solution for 0/1
    knapsack, but it's fast: O(n log n) for sorting + O(n) for selection.

    Args:
        items: Available items to choose from.
        capacity: Maximum weight the knapsack can hold.

    Returns:
        Tuple of (selected items, total value).

    >>> items = [Item('A', 60, 10), Item('B', 100, 20), Item('C', 120, 30)]
    >>> selected, value = greedy_knapsack(items, 50)
    >>> value
    220.0
    """
    # Sort by value-to-weight ratio (highest first)
    sorted_items = sorted(items, key=lambda x: x.value_per_weight, reverse=True)

    selected = []
    total_weight = 0.0
    total_value = 0.0

    for item in sorted_items:
        if total_weight + item.weight <= capacity:
            selected.append(item)
            total_weight += item.weight
            total_value += item.value

    return selected, total_value


# =============================================================================
# Example 3: Fractional Knapsack (items can be split)
# =============================================================================

def fractional_knapsack(items: list[Item], capacity: float) -> float:
    """Fractional knapsack: items can be partially taken.

    The greedy approach IS optimal for fractional knapsack.
    Take items by best ratio; if an item doesn't fully fit,
    take the fraction that fits.

    >>> items = [Item('A', 60, 10), Item('B', 100, 20), Item('C', 120, 30)]
    >>> fractional_knapsack(items, 50)
    240.0
    """
    sorted_items = sorted(items, key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0.0
    remaining = capacity

    for item in sorted_items:
        if remaining <= 0:
            break
        if item.weight <= remaining:
            total_value += item.value
            remaining -= item.weight
        else:
            # Take partial item
            fraction = remaining / item.weight
            total_value += item.value * fraction
            remaining = 0

    return total_value


# =============================================================================
# Example 4: Practical Demo
# =============================================================================

def demo():
    """Demonstrate greedy knapsack with sample items."""
    items = [
        Item('Gold Bar',    500, 25),
        Item('Diamond',     300,  5),
        Item('Painting',    200, 15),
        Item('Laptop',      150,  3),
        Item('Sculpture',   100, 20),
        Item('Book Set',     50, 10),
    ]
    capacity = 40

    print("=== Available Items ===")
    print(f"{'Name':<12} {'Value':>6} {'Weight':>6} {'Ratio':>8}")
    print("-" * 35)
    for item in items:
        print(f"{item.name:<12} {item.value:>6.0f} {item.weight:>6.0f} "
              f"{item.value_per_weight:>8.2f}")
    print(f"\nKnapsack capacity: {capacity}")

    # 0/1 Knapsack (greedy)
    selected, value = greedy_knapsack(items, capacity)
    print(f"\n--- 0/1 Knapsack (Greedy) ---")
    total_weight = sum(item.weight for item in selected)
    for item in selected:
        print(f"  Selected: {item.name} (value={item.value}, weight={item.weight})")
    print(f"  Total value:  {value:.0f}")
    print(f"  Total weight: {total_weight:.0f}/{capacity}")

    # Fractional Knapsack (greedy - optimal)
    frac_value = fractional_knapsack(items, capacity)
    print(f"\n--- Fractional Knapsack (Greedy, Optimal) ---")
    print(f"  Total value: {frac_value:.0f}")

    print("\nNote: Greedy is optimal for fractional knapsack but NOT")
    print("guaranteed optimal for 0/1 knapsack. Dynamic programming")
    print("is needed for optimal 0/1 solutions.")


if __name__ == '__main__':
    demo()
