"""
TUTORIAL: Reducing Unnecessary Operations for Performance

Why this matters:
  When writing loops that need to find something or check a condition, how you
  structure the code dramatically impacts performance. The key insight is that
  EARLY TERMINATION (returning immediately when we find what we need) is much
  faster than continuing to process data after finding our target.

  This tutorial shows three critical patterns:
  1. Early return (best): Stop immediately when condition is met
  2. Unnecessary continuation (worst): Keep looping even after finding answer
  3. Using builtins (good): Leverage optimized functions like any()

Core lesson:
  Don't continue work after you have your answer. The CPU time spent on
  unnecessary operations adds up fast, especially in loops.
"""

import timeit


# ============ Example 1: The FAST way - Early Return ============
# This is the optimal pattern. As soon as we find a match, we return True
# immediately. If needle is near the beginning, we save scanning the rest.

def search_fast(haystack, needle):
    """Return True if needle is in haystack, STOP as soon as found."""
    for item in haystack:
        if item == needle:
            return True  # <-- Exit immediately when found
    return False


# ============ Example 2: The SLOW way - No Early Return ============
# This function continues looping EVEN AFTER finding the match. It sets
# return_value to True but keeps iterating through the entire list.
# This wastes CPU cycles on comparisons we don't need.

def search_slow(haystack, needle):
    """Same functionality, but doesn't return early. Much slower!"""
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
        # <-- Keeps looping here instead of exiting
    return return_value


# ============ Example 3: Using any() with generator ============
# The any() builtin is optimized in C and also uses short-circuit evaluation.
# This generator expression doesn't create a full list in memory - it generates
# comparisons on-demand, and any() stops as soon as one True is found.

def search_builtin_gen(haystack, needle):
    """Use any() with a generator - efficient and Pythonic."""
    return any((item == needle for item in haystack))


# ============ Example 4: Using any() with list comprehension ============
# WARNING: This creates the entire list of comparisons BEFORE any() starts.
# So this must evaluate the entire list even if the match is near the beginning.
# Don't use this pattern for early termination tasks!

def search_builtin_list(haystack, needle):
    """Using any() with list comprehension - creates full list first."""
    return any([item == needle for item in haystack])


if __name__ == "__main__":
    print("=" * 70)
    print("TUTORIAL: Reducing Unnecessary Operations")
    print("=" * 70)

    # Setup test data
    haystack = list(range(1000))  # 0, 1, 2, ..., 999
    iterations = 10000

    # -------- TEST 1: Needle near the beginning --------
    print("\n" + "=" * 70)
    print("Test 1: Needle CLOSE TO START (position 5)")
    print("=" * 70)

    needle = 5

    t_fast = timeit.timeit(
        stmt="search_fast(haystack, needle)",
        setup="from __main__ import haystack, needle, search_fast",
        number=iterations
    )
    print(f"search_fast:        {t_fast/iterations:.5e} seconds per call")

    t_slow = timeit.timeit(
        stmt="search_slow(haystack, needle)",
        setup="from __main__ import haystack, needle, search_slow",
        number=iterations
    )
    print(f"search_slow:        {t_slow/iterations:.5e} seconds per call")

    t_gen = timeit.timeit(
        stmt="search_builtin_gen(haystack, needle)",
        setup="from __main__ import haystack, needle, search_builtin_gen",
        number=iterations
    )
    print(f"any() + generator:  {t_gen/iterations:.5e} seconds per call")

    t_list = timeit.timeit(
        stmt="search_builtin_list(haystack, needle)",
        setup="from __main__ import haystack, needle, search_builtin_list",
        number=iterations
    )
    print(f"any() + list comp:  {t_list/iterations:.5e} seconds per call")

    slowdown = t_slow / t_fast
    print(f"\nSLOW version is {slowdown:.1f}x slower than FAST!")
    print("WHY: search_slow must scan 995 more items after finding the match.")

    # -------- TEST 2: Needle near the end --------
    print("\n" + "=" * 70)
    print("Test 2: Needle CLOSE TO END (position 990)")
    print("=" * 70)

    needle = len(haystack) - 10

    t_fast = timeit.timeit(
        stmt="search_fast(haystack, needle)",
        setup="from __main__ import haystack, needle, search_fast",
        number=iterations
    )
    print(f"search_fast:        {t_fast/iterations:.5e} seconds per call")

    t_slow = timeit.timeit(
        stmt="search_slow(haystack, needle)",
        setup="from __main__ import haystack, needle, search_slow",
        number=iterations
    )
    print(f"search_slow:        {t_slow/iterations:.5e} seconds per call")

    t_gen = timeit.timeit(
        stmt="search_builtin_gen(haystack, needle)",
        setup="from __main__ import haystack, needle, search_builtin_gen",
        number=iterations
    )
    print(f"any() + generator:  {t_gen/iterations:.5e} seconds per call")

    slowdown = t_slow / t_fast
    print(f"\nSLOW version is {slowdown:.1f}x slower than FAST!")
    print("WHY: Both must scan almost the entire list, so difference is smaller.")
    print("But FAST is still faster because it stops immediately upon finding.")

    # -------- KEY INSIGHTS --------
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("""
1. EARLY RETURN beats everything:
   - Return as soon as you find your answer
   - Don't set a variable and keep looping

2. any() with GENERATOR is nearly as good:
   - Generators use lazy evaluation (compute on-demand)
   - any() short-circuits (stops when first True found)
   - More Pythonic than manual loops

3. any() with LIST COMPREHENSION is slower:
   - List comprehension creates the ENTIRE list first
   - No short-circuit benefit since list exists fully
   - Never use this pattern for early-termination logic

4. The impact depends on DATA POSITION:
   - Near the start: HUGE difference (10x+ slowdown)
   - Near the end: Smaller difference but still present
   - Worst case: Missing item requires checking everything

5. CPU TIME MATTERS:
   - In tight loops, unnecessary iterations add up
   - 10,000 iterations × extra work = measurable delay
   - In real code with millions of iterations: seconds wasted
    """)
