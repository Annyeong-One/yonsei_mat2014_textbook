"""
TUTORIAL: How Hash Function Quality Impacts Dictionary Performance

Why this matters:
  A HASH FUNCTION distributes keys across buckets in a dict or set. A BAD hash
  function sends most keys to the same bucket, turning O(1) lookup into O(n).
  A GOOD hash function spreads keys evenly, keeping O(1) fast.

  This tutorial shows:
  1. How a bad hash (returning constant 42) destroys performance
  2. How a good hash spreads values and stays fast
  3. Why hash quality matters for real-world dicts/sets

Core lesson:
  Hash functions seem invisible, but quality determines whether your dict
  lookups are O(1) or O(n). Always ensure custom hashes distribute evenly.
"""

import string
import timeit


# ============ Example 1: A Bad Hash Function ============
# This hash always returns 42. All keys hash to the same value, so they
# all go in the same bucket. Lookup becomes a linear search through that bucket.

class BadHash(str):
    """String subclass with terrible hash function."""

    def __hash__(self):
        """Always return 42. All keys collide into same bucket!"""
        return 42


# ============ Example 2: A Good Hash Function ============
# This hash distributes two-letter strings evenly based on their characters.
# Keys spread across buckets, keeping lookups fast even with many items.

class GoodHash(str):
    """String subclass with good hash function."""

    def __hash__(self):
        """
        Hash based on first two letters.
        Spread all 26x26=676 combinations across different buckets.
        """
        # Use character ordinals to create distinct hash values
        # Simplified formula, but demonstrates good distribution
        return ord(self[1]) + 26 * ord(self[0]) - 2619


def demo_hash_distribution():
    """Visualize how hash functions distribute keys."""
    print("\n" + "=" * 70)
    print("Example 1: How Hash Functions Distribute Keys")
    print("=" * 70)

    bad_hashes = set()
    good_hashes = set()

    # Generate all two-letter combinations
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            key = i + j
            bad_hash_val = 42  # BadHash always returns 42
            good_hash_val = ord(j) + 26 * ord(i) - 2619

            bad_hashes.add(bad_hash_val)
            good_hashes.add(good_hash_val)

    print(f"Generated {26 * 26} two-letter combinations")
    print()
    print(f"BadHash unique values:  {len(bad_hashes)}")
    print(f"  All 676 keys hash to: 42 (TERRIBLE collision!)")
    print()
    print(f"GoodHash unique values: {len(good_hashes)}")
    print(f"  Keys spread across {len(good_hashes)} different hash values")
    print(f"  Much better distribution!")


def demo_lookup_performance():
    """Compare lookup speed with bad vs good hash."""
    print("\n" + "=" * 70)
    print("Example 2: Lookup Performance - Bad vs Good Hash")
    print("=" * 70)

    # Create a set of all two-letter combinations
    baddict = set()
    gooddict = set()

    print("Building sets with 676 two-letter combinations...")
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            key = i + j
            baddict.add(BadHash(key))
            gooddict.add(GoodHash(key))

    print(f"  baddict size:  {len(baddict)}")
    print(f"  gooddict size: {len(gooddict)}")
    print()

    # Time lookups in baddict (all keys hash to same bucket)
    print("Timing 100,000 lookups for 'zz' in each set...")
    print()

    badtime = timeit.repeat(
        stmt="key in baddict",
        setup="from __main__ import baddict, BadHash; key = BadHash('zz')",
        repeat=3,
        number=100_000,
    )

    goodtime = timeit.repeat(
        stmt="key in gooddict",
        setup="from __main__ import gooddict, GoodHash; key = GoodHash('zz')",
        repeat=3,
        number=100_000,
    )

    bad_min = min(badtime)
    good_min = min(goodtime)
    slowdown = bad_min / good_min

    print(f"BadHash  min time: {bad_min:.4f} seconds")
    print(f"GoodHash min time: {good_min:.4f} seconds")
    print()
    print(f"BadHash is {slowdown:.1f}x SLOWER than GoodHash!")
    print()
    print("""
    WHY this huge difference:

    BadHash (constant 42):
    - All 676 keys collide in the same bucket
    - Lookup must scan through 676 comparisons
    - O(n) time where n = bucket size

    GoodHash (distributed):
    - Keys spread across ~650+ different buckets
    - Average bucket has ~1 item
    - Lookup finds item immediately (O(1))
    """)


def demo_hash_quality_rules():
    """Show the properties of good hash functions."""
    print("\n" + "=" * 70)
    print("Example 3: What Makes a Good Hash Function")
    print("=" * 70)

    print("""
    PROPERTIES OF GOOD HASH FUNCTIONS:

    1. DETERMINISTIC:
       - Same input always gives same hash
       - hash(obj) must never change for the same object

    2. FAST:
       - Hashing should be quick (O(1) time)
       - If hash is slow, lookups become slow

    3. UNIFORMLY DISTRIBUTED:
       - Different inputs should hash to different buckets
       - Spread keys across many hash values
       - Minimize collisions (multiple keys per bucket)

    4. AVALANCHE PROPERTY:
       - Small change in input → big change in hash
       - If two keys are similar, hashes should differ
       - Prevents clustering of similar keys

    WHAT BAD HASHES DO:
    - Return constants (all keys → same bucket)
    - Return predictable patterns (collisions cluster)
    - Are slow to compute
    - Ignore important attributes of the data
    """)

    # Demonstrate clustering issue
    print("\n" + "-" * 70)
    print("Example of clustering:")
    print("-" * 70)

    print("\nBadHash clustering:")
    bad_examples = [BadHash('aa'), BadHash('ab'), BadHash('zz')]
    for ex in bad_examples:
        print(f"  hash({repr(ex)}) = {hash(ex)}")

    print("\nGoodHash distribution:")
    good_examples = [GoodHash('aa'), GoodHash('ab'), GoodHash('zz')]
    for ex in good_examples:
        print(f"  hash({repr(ex)}) = {hash(ex)}")

    print("\nNotice: GoodHash values are spread far apart (different buckets)")
    print("        BadHash values are identical (same bucket, linear search)")


def demo_real_world_impact():
    """Show impact on real operations."""
    print("\n" + "=" * 70)
    print("Example 4: Real-World Impact on Operations")
    print("=" * 70)

    print("""
    Scenario: You have a set of 1,000 API endpoints (usernames, IDs, etc.)

    With GOOD hash:
    - Lookup: ~1,000,000 operations, instant
    - Add: Insert at correct bucket, instant
    - Remove: Find and remove, instant
    - Memory: Buckets distributed, moderate

    With BAD hash (all keys → same bucket):
    - Lookup: Must scan ~1,000 items linearly, SLOW
    - Add: Must check all existing items, SLOW
    - Remove: Must scan entire bucket, SLOW
    - Memory: Everything in one bucket, cache-bad

    With 10,000 requests/second:
    - Good hash: Sub-millisecond response
    - Bad hash: Multiple second response (unusable!)
    """)


if __name__ == "__main__":
    print("=" * 70)
    print("TUTORIAL: Hash Function Quality and Performance")
    print("=" * 70)

    demo_hash_distribution()
    demo_lookup_performance()
    demo_hash_quality_rules()
    demo_real_world_impact()

    # -------- KEY INSIGHTS --------
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("""
1. HASH FUNCTION is INVISIBLE but CRITICAL:
   - It determines if dict/set is O(1) or O(n)
   - Bad hash turns fast lookups into slow scans
   - You usually don't think about it, but quality matters

2. COLLISIONS destroy performance:
   - Collision = multiple keys hash to same value
   - When collision happens, must do linear search
   - Good hash minimizes collisions

3. EVEN DISTRIBUTION is essential:
   - Hash values should spread across all buckets
   - Each bucket should have ~1 item on average
   - Large buckets mean slow lookups for those items

4. CUSTOM HASHES often perform poorly:
   - Easy to accidentally create clustering
   - Must think carefully about value distribution
   - Test your custom hash on realistic data

5. BUILT-IN HASHES are highly optimized:
   - Python's hash for str, int, tuple is excellent
   - Use built-in types when possible
   - Only custom hash when necessary

6. MEASURE BEFORE OPTIMIZING:
   - Profile your code to find bottlenecks
   - Bad hash is only a problem if it's slow
   - But when it is, slowdown is dramatic
    """)
