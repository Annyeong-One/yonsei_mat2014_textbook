"""
TUTORIAL: Hashing Fundamentals - __hash__ and __eq__ Working Together

Why this matters:
  When you put objects in a dict or set, Python uses HASHING to find them quickly.
  The hash value determines where to store the object. But here's the catch:
  __hash__ and __eq__ MUST work together consistently. If they disagree,
  lookups fail even when the object exists!

  This tutorial shows:
  1. What happens with default hash (identity-based)
  2. What you get with custom __hash__ and __eq__
  3. Why BOTH methods matter and must be consistent

Core lesson:
  If you override __eq__ to define equality by value, you MUST override __hash__
  to hash by the same values. Otherwise, equal objects won't be treated as equal
  in sets and dicts.
"""


# ============ Example 1: Default Hash (Identity-based) ============
# Without custom __hash__ and __eq__, two Point(1,1) objects are different
# because they're different objects in memory. Python uses the object's
# memory address (identity) for the default hash.

class Point:
    """Point with no custom hash or equality. Uses object identity."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# ============ Example 2: Custom Hash and Equality ============
# By defining __hash__ and __eq__ based on coordinates, two Point objects
# with the same x and y are treated as equal and hash to the same value.

class PointHash:
    """Point with custom hash and equality based on coordinates."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        """Hash based on coordinates, not object identity."""
        return hash((self.x, self.y))

    def __eq__(self, other):
        """Two points are equal if they have same coordinates."""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"PointHash({self.x}, {self.y})"


def demo_default_hash():
    """Show how default hash fails for equality by value."""
    print("\n" + "=" * 70)
    print("Example 1: Default Hash (Identity-based)")
    print("=" * 70)

    p1 = Point(1, 1)
    p2 = Point(1, 1)

    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"\np1 == p2: {p1 == p2}  (False, different objects)")
    print(f"p1 is p2: {p1 is p2}  (False, different memory addresses)")

    # Create a set with both points
    points = set([p1, p2])
    print(f"\nset([p1, p2]) = {points}")
    print(f"Set has {len(points)} items (both points are stored separately)")

    # Try to find a point with same coordinates
    p3 = Point(1, 1)
    found = p3 in points
    print(f"\nPoint(1, 1) in set([p1, p2]) = {found}")
    print("WHY: p3 is a different object, different hash, lookup fails!")

    print("""
    PROBLEM with default hash:
    - Hash is based on object identity (memory address)
    - Two objects with same data get different hashes
    - Sets/dicts can't find equal objects
    """)


def demo_custom_hash():
    """Show how custom hash/eq enables value-based equality."""
    print("\n" + "=" * 70)
    print("Example 2: Custom Hash and Equality (Value-based)")
    print("=" * 70)

    p1 = PointHash(1, 1)
    p2 = PointHash(1, 1)

    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"\np1 == p2: {p1 == p2}  (True, same coordinates!)")
    print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}  (True, same hash!)")

    # Create a set with both points
    points = set([p1, p2])
    print(f"\nset([p1, p2]) = {points}")
    print(f"Set has {len(points)} item (duplicate detected and removed!)")

    # Try to find a point with same coordinates
    p3 = PointHash(1, 1)
    found = p3 in points
    print(f"\nPointHash(1, 1) in set([p1, p2]) = {found}")
    print("SUCCESS: p3 has same hash and is equal to p1/p2, found in set!")

    print("""
    SOLUTION with custom hash/eq:
    - Hash is based on coordinates (the actual data)
    - Two objects with same data get same hash
    - Sets/dicts find equal objects correctly
    """)


def demo_hash_eq_consistency():
    """Show why __hash__ and __eq__ must be consistent."""
    print("\n" + "=" * 70)
    print("Example 3: Why __hash__ and __eq__ Must Be Consistent")
    print("=" * 70)

    p1 = PointHash(1, 1)
    p2 = PointHash(1, 1)
    p3 = PointHash(2, 2)

    print("Rule: If a == b, then hash(a) == hash(b)")
    print()

    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p3 = {p3}")
    print()

    print(f"p1 == p2: {p1 == p2}")
    print(f"hash(p1) = {hash(p1)}")
    print(f"hash(p2) = {hash(p2)}")
    print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)} ✓ CONSISTENT")
    print()

    print(f"p1 == p3: {p1 == p3}")
    print(f"hash(p1) = {hash(p1)}")
    print(f"hash(p3) = {hash(p3)}")
    print(f"hash(p1) == hash(p3): {hash(p1) == hash(p3)} ✓ CONSISTENT")
    print()

    print("""
    WHY consistency matters:
    - Dict/set uses hash to find bucket
    - Then uses == to find exact item in bucket
    - If p1 == p2 but hash(p1) != hash(p2), they go to different buckets
    - Lookup fails even though object exists!
    """)


def demo_use_in_dict():
    """Show that custom hash enables dict use."""
    print("\n" + "=" * 70)
    print("Example 4: Using Custom Hash in Dictionaries")
    print("=" * 70)

    p1 = PointHash(1, 1)
    p2 = PointHash(1, 1)  # Equal to p1
    p3 = PointHash(2, 2)

    # Create a dict with point coordinates as keys
    distances = {}
    distances[p1] = 1.41  # Distance from origin

    print(f"distances[PointHash(1, 1)] = {distances[p1]}")
    print(f"distances[p2] = {distances[p2]}")  # p2 is equal to p1, so same key
    print(f"distances[p3] = {distances.get(p3, 'NOT FOUND')}")

    print(f"\nDict has {len(distances)} entry (p1 and p2 are the same key)")


if __name__ == "__main__":
    print("=" * 70)
    print("TUTORIAL: Hashing - __hash__ and __eq__")
    print("=" * 70)

    demo_default_hash()
    demo_custom_hash()
    demo_hash_eq_consistency()
    demo_use_in_dict()

    # -------- KEY INSIGHTS --------
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("""
1. DEFAULT HASH is identity-based:
   - Two objects with same data get different hashes
   - Sets and dicts treat them as different items
   - Use default hash only when object identity matters

2. CUSTOM HASH must be value-based:
   - Hash based on the attributes that define equality
   - Equal objects must have equal hashes
   - Different objects should (usually) have different hashes

3. __HASH__ and __EQ__ are a pair:
   - Always override both together
   - They must be consistent (see Rule above)
   - Violating consistency causes hard-to-find bugs

4. HASH MUST BE IMMUTABLE:
   - Hash value must never change after object creation
   - Only hash immutable attributes (strings, ints, tuples)
   - Don't hash mutable attributes (lists, dicts, sets)

5. PRACTICAL RULE:
   - If you override __eq__, override __hash__ too
   - Think about which attributes define equality
   - Hash those exact attributes using tuple or XOR
   - Test that equal objects have equal hashes
    """)
