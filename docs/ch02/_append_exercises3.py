#!/usr/bin/env python3
"""Batch 3: Append exercises to numerics, operators, performance, scope, strings, typing, variables."""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

EXERCISES = {}

# ============================================================================
# NUMERICS
# ============================================================================

EXERCISES["numerics/int_number_systems.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `convert_all_bases(n)` that takes a decimal integer and returns a dictionary with keys `"bin"`, `"oct"`, and `"hex"`, each holding the string representation (with prefix) of `n` in that base.

---

**Exercise 2.**
Given the string `"0b11010110"`, convert it to its decimal, octal, and hexadecimal string representations without using `int()` with a base argument more than once. Print all three results.

---

**Exercise 3.**
Write a function `base_to_decimal(s)` that accepts a string with a prefix (`"0b"`, `"0o"`, or `"0x"`) and returns the decimal integer. If the prefix is unrecognized, raise a `ValueError`.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def convert_all_bases(n):
        return {
            "bin": bin(n),
            "oct": oct(n),
            "hex": hex(n),
        }

    result = convert_all_bases(255)
    print(result)
    # {'bin': '0b11111111', 'oct': '0o377', 'hex': '0xff'}
    ```

    `bin()`, `oct()`, and `hex()` return string representations with the appropriate prefix.

??? success "Solution to Exercise 2"

    ```python
    s = "0b11010110"
    decimal_val = int(s, 2)          # Use int() once with base 2
    print(f"Decimal: {decimal_val}")  # 214
    print(f"Octal: {oct(decimal_val)}")  # 0o326
    print(f"Hex: {hex(decimal_val)}")    # 0xd6
    ```

    `int(s, 2)` parses a binary string. From the integer, `oct()` and `hex()` produce the other representations.

??? success "Solution to Exercise 3"

    ```python
    def base_to_decimal(s):
        prefix = s[:2].lower()
        if prefix == "0b":
            return int(s, 2)
        elif prefix == "0o":
            return int(s, 8)
        elif prefix == "0x":
            return int(s, 16)
        else:
            raise ValueError(f"Unrecognized prefix in '{s}'")

    print(base_to_decimal("0b1010"))   # 10
    print(base_to_decimal("0o17"))     # 15
    print(base_to_decimal("0xFF"))     # 255
    ```

    The function inspects the first two characters to determine the base, then delegates to `int()` with the appropriate base argument.
"""

EXERCISES["numerics/type_promotion.md"] = """

---

## Exercises

**Exercise 1.**
Predict the type and value of each expression without running the code, then verify:

```python
a = True + 2
b = 1 + 2.0
c = 3.0 + 4j
```

---

**Exercise 2.**
Write a function `promotion_chain(value)` that accepts a numeric value and returns a string describing the promotion hierarchy from `bool` to `complex`. For example, `promotion_chain(True)` should return `"bool -> int -> float -> complex"` along with the value at each stage.

---

**Exercise 3.**
Explain why `True + True + True` equals `3` and what type the result is. Then show how `sum([True, False, True, True, False])` leverages this behavior.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    a = True + 2
    print(a, type(a))  # 3 <class 'int'>

    b = 1 + 2.0
    print(b, type(b))  # 3.0 <class 'float'>

    c = 3.0 + 4j
    print(c, type(c))  # (3+4j) <class 'complex'>
    ```

    `True` is promoted to `int(1)`, then `1 + 2 = 3`. An `int` plus a `float` promotes to `float`. A `float` plus a `complex` promotes to `complex`.

??? success "Solution to Exercise 2"

    ```python
    def promotion_chain(value):
        results = []
        results.append(f"bool:    {bool(value)} (type: {type(bool(value)).__name__})")
        results.append(f"int:     {int(value)} (type: {type(int(value)).__name__})")
        results.append(f"float:   {float(value)} (type: {type(float(value)).__name__})")
        results.append(f"complex: {complex(value)} (type: {type(complex(value)).__name__})")
        return "\\n".join(results)

    print(promotion_chain(True))
    ```

    Each constructor explicitly converts the value to the next type in the hierarchy.

??? success "Solution to Exercise 3"

    ```python
    result = True + True + True
    print(result)        # 3
    print(type(result))  # <class 'int'>

    values = [True, False, True, True, False]
    print(sum(values))   # 3
    ```

    `True` is `1` and `False` is `0` in arithmetic context. `sum()` adds them as integers, effectively counting the number of `True` values.
"""

EXERCISES["numerics/float_special_values.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `classify_float(x)` that returns `"positive infinity"`, `"negative infinity"`, `"NaN"`, or `"finite"` for any given float value. Use the `math` module.

---

**Exercise 2.**
Demonstrate that `float('nan') != float('nan')` is `True`. Then write a function `safe_equal(a, b)` that correctly handles NaN comparisons (two NaN values should be considered equal).

---

**Exercise 3.**
Create a list containing `[1.0, float('inf'), float('nan'), -2.5, float('-inf')]`. Write code that filters out all non-finite values and computes the mean of the remaining finite values.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    import math

    def classify_float(x):
        if math.isnan(x):
            return "NaN"
        elif math.isinf(x):
            return "positive infinity" if x > 0 else "negative infinity"
        else:
            return "finite"

    print(classify_float(float('inf')))   # positive infinity
    print(classify_float(float('nan')))   # NaN
    print(classify_float(3.14))           # finite
    print(classify_float(float('-inf')))  # negative infinity
    ```

    Check NaN first because `math.isinf(nan)` returns `False`, but NaN also fails all comparison operators.

??? success "Solution to Exercise 2"

    ```python
    import math

    # NaN is not equal to itself
    print(float('nan') != float('nan'))  # True

    def safe_equal(a, b):
        if math.isnan(a) and math.isnan(b):
            return True
        return a == b

    print(safe_equal(float('nan'), float('nan')))  # True
    print(safe_equal(1.0, 1.0))                    # True
    print(safe_equal(1.0, 2.0))                    # False
    ```

    The standard `==` operator returns `False` for NaN comparisons. The workaround uses `math.isnan()` to detect NaN values explicitly.

??? success "Solution to Exercise 3"

    ```python
    import math

    values = [1.0, float('inf'), float('nan'), -2.5, float('-inf')]

    finite_values = [x for x in values if math.isfinite(x)]
    mean = sum(finite_values) / len(finite_values)

    print(finite_values)  # [1.0, -2.5]
    print(mean)           # -0.75
    ```

    `math.isfinite()` returns `True` only for values that are neither infinity nor NaN.
"""

EXERCISES["numerics/float_python_vs_c.md"] = """

---

## Exercises

**Exercise 1.**
Use `sys.getsizeof()` to compare the memory used by a single Python `float`, a Python `int`, and a Python `str` of `"3.14"`. Explain why a Python float uses more memory than the 8 bytes needed for the IEEE 754 value.

---

**Exercise 2.**
Write a timing comparison that sums one million `0.1` values using (a) a Python `for` loop and (b) `sum()` with a generator expression. Report the times and explain the difference.

---

**Exercise 3.**
Demonstrate that `0.1 + 0.2 != 0.3` in Python and show two different ways to correctly compare floating-point values for approximate equality.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    import sys

    f = 3.14
    i = 3
    s = "3.14"

    print(f"float: {sys.getsizeof(f)} bytes")  # 24
    print(f"int:   {sys.getsizeof(i)} bytes")   # 28
    print(f"str:   {sys.getsizeof(s)} bytes")   # 53

    # Python float uses 24 bytes:
    #   8 bytes for reference count
    #   8 bytes for type pointer
    #   8 bytes for the actual IEEE 754 double value
    ```

    Every Python object carries metadata (reference count and type pointer), adding 16 bytes of overhead on top of the 8-byte double value.

??? success "Solution to Exercise 2"

    ```python
    import time

    n = 1_000_000

    # Method 1: for loop
    start = time.perf_counter()
    total = 0.0
    for _ in range(n):
        total += 0.1
    loop_time = time.perf_counter() - start

    # Method 2: sum with generator
    start = time.perf_counter()
    total = sum(0.1 for _ in range(n))
    sum_time = time.perf_counter() - start

    print(f"for loop: {loop_time:.4f}s")
    print(f"sum():    {sum_time:.4f}s")
    ```

    `sum()` is implemented in C and avoids Python bytecode overhead for each addition, making it faster than an explicit loop.

??? success "Solution to Exercise 3"

    ```python
    import math

    # The problem
    print(0.1 + 0.2 == 0.3)  # False

    # Solution 1: math.isclose
    print(math.isclose(0.1 + 0.2, 0.3))  # True

    # Solution 2: absolute tolerance
    epsilon = 1e-9
    print(abs((0.1 + 0.2) - 0.3) < epsilon)  # True
    ```

    Floating-point representation errors mean `0.1 + 0.2` produces `0.30000000000000004`. Use `math.isclose()` or an explicit tolerance for comparisons.
"""

EXERCISES["numerics/float_ieee754.md"] = """

---

## Exercises

**Exercise 1.**
Use Python's `struct` module to extract the sign, exponent, and mantissa bits of the float `−6.5`. Verify your result by reconstructing the value from the extracted components.

---

**Exercise 2.**
Demonstrate that `float(2**53 + 1) == float(2**53)` is `True`. Explain why this happens in terms of IEEE 754 mantissa bits.

---

**Exercise 3.**
Write a function `is_exact_float(x)` that checks whether a decimal string like `"0.375"` can be represented exactly as a Python float. Test it with `"0.5"`, `"0.1"`, and `"0.375"`.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    import struct

    def float_parts(x):
        packed = struct.pack('>d', x)
        bits = ''.join(f'{b:08b}' for b in packed)
        sign = int(bits[0])
        exponent = int(bits[1:12], 2)
        mantissa = bits[12:]
        return sign, exponent, mantissa

    s, e, m = float_parts(-6.5)
    print(f"Sign: {s}")       # 1 (negative)
    print(f"Exponent: {e}")   # 1025
    print(f"Mantissa: {m[:10]}...")

    # Reconstruct: (-1)^1 * (1 + mantissa_fraction) * 2^(1025-1023)
    # = -1 * 1.625 * 4 = -6.5
    bias = 1023
    mantissa_val = int(m, 2) / (2**52)
    reconstructed = ((-1)**s) * (1 + mantissa_val) * (2**(e - bias))
    print(f"Reconstructed: {reconstructed}")  # -6.5
    ```

    The sign bit is 1 (negative), the biased exponent gives an actual exponent of 2, and the mantissa encodes the fraction 0.625, so the value is `-(1.625) * 4 = -6.5`.

??? success "Solution to Exercise 2"

    ```python
    a = 2**53
    b = 2**53 + 1

    print(float(a) == float(b))  # True
    print(f"2^53     = {a}")
    print(f"2^53 + 1 = {b}")
    print(f"float(2^53)     = {float(a):.1f}")
    print(f"float(2^53 + 1) = {float(b):.1f}")
    ```

    IEEE 754 double precision has 52 mantissa bits (plus one implicit bit), so it can represent integers exactly up to `2^53`. Beyond that, consecutive floats are spaced 2 apart, and `2^53 + 1` rounds down to `2^53`.

??? success "Solution to Exercise 3"

    ```python
    from decimal import Decimal

    def is_exact_float(s):
        float_val = float(s)
        return Decimal(float_val) == Decimal(s)

    print(is_exact_float("0.5"))    # True
    print(is_exact_float("0.1"))    # False
    print(is_exact_float("0.375"))  # True
    ```

    Values that are sums of powers of 2 (like 0.5 = 2^-1 and 0.375 = 2^-2 + 2^-3) are exact. Values like 0.1 have infinite binary expansions and cannot be stored exactly.
"""

EXERCISES["numerics/int_python_vs_c.md"] = """

---

## Exercises

**Exercise 1.**
Compute `2 ** 1000` in Python and print the number of digits. Explain why this works in Python but would overflow in C.

---

**Exercise 2.**
Use `sys.getsizeof()` to compare the memory usage of the integers `0`, `1`, `2**30`, and `2**1000`. Explain the pattern.

---

**Exercise 3.**
Write a function `factorial_digits(n)` that computes `n!` and returns the number of decimal digits in the result. Test with `n = 100`. Explain why Python can handle this while C `int` or `long` cannot.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    result = 2 ** 1000
    num_digits = len(str(result))
    print(f"2^1000 has {num_digits} digits")  # 302 digits
    ```

    Python integers have arbitrary precision -- they grow as needed. In C, a 64-bit `long` can hold at most about 19 digits before overflowing.

??? success "Solution to Exercise 2"

    ```python
    import sys

    for val in [0, 1, 2**30, 2**1000]:
        size = sys.getsizeof(val)
        print(f"getsizeof({str(val)[:20]:>20s}...) = {size} bytes")
    ```

    Small integers use a fixed base size. As the value grows, Python allocates additional machine words to store the extra digits, so `2**1000` uses significantly more memory than `1`.

??? success "Solution to Exercise 3"

    ```python
    import math

    def factorial_digits(n):
        result = math.factorial(n)
        return len(str(result))

    print(f"100! has {factorial_digits(100)} digits")  # 158 digits
    ```

    `100!` is a 158-digit number. Python handles this naturally because `int` has arbitrary precision. A C `unsigned long long` (64 bits) overflows at about `20!`.
"""

EXERCISES["numerics/float_numerical_errors.md"] = """

---

## Exercises

**Exercise 1.**
Demonstrate catastrophic cancellation by computing `(1 + 1e-16) - 1` and comparing it to the expected result `1e-16`. How many significant digits are lost?

---

**Exercise 2.**
Implement Kahan summation and compare it against the built-in `sum()` when adding `[0.1] * 10000`. Report the error of each relative to the expected value `1000.0`.

---

**Exercise 3.**
Show that floating-point addition is not associative by finding three values `a`, `b`, `c` where `(a + b) + c != a + (b + c)`. Print both results and their difference.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    result = (1 + 1e-16) - 1
    expected = 1e-16
    print(f"Computed: {result}")
    print(f"Expected: {expected}")
    print(f"Relative error: {abs(result - expected) / expected:.2%}")
    ```

    The result is `0.0` instead of `1e-16`. Adding `1e-16` to `1.0` does not change the float because the value falls below machine epsilon. All significant digits are lost.

??? success "Solution to Exercise 2"

    ```python
    def kahan_sum(values):
        total = 0.0
        compensation = 0.0
        for x in values:
            y = x - compensation
            t = total + y
            compensation = (t - total) - y
            total = t
        return total

    values = [0.1] * 10000
    expected = 1000.0

    builtin_result = sum(values)
    kahan_result = kahan_sum(values)

    print(f"sum():  {builtin_result:.15f}, error: {abs(builtin_result - expected):.2e}")
    print(f"kahan:  {kahan_result:.15f}, error: {abs(kahan_result - expected):.2e}")
    ```

    Kahan summation tracks a compensation term that captures the low-order bits lost during each addition, producing a result much closer to the true value.

??? success "Solution to Exercise 3"

    ```python
    a = 1e16
    b = -1e16
    c = 1.0

    left = (a + b) + c
    right = a + (b + c)

    print(f"(a + b) + c = {left}")   # 1.0
    print(f"a + (b + c) = {right}")  # 0.0
    print(f"Difference: {abs(left - right)}")  # 1.0
    ```

    `b + c` equals `-1e16` because `c = 1.0` is too small relative to `-1e16` to affect the sum. So `a + (b + c) = 0.0`. But `(a + b) = 0.0`, then `0.0 + c = 1.0`.
"""

EXERCISES["numerics/int_bitwise_operations.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `is_power_of_two(n)` that uses bitwise operations to check whether a positive integer is a power of two. Hint: a power of two has exactly one bit set.

---

**Exercise 2.**
Without using multiplication, write a function `multiply_by_eight(n)` that multiplies an integer by 8 using only bitwise shift operators.

---

**Exercise 3.**
Write a function `swap_bits(n, i, j)` that swaps the bits at positions `i` and `j` in the integer `n`. Test with `n = 0b1010`, `i = 1`, `j = 3`.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def is_power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0

    print(is_power_of_two(1))    # True  (2^0)
    print(is_power_of_two(16))   # True  (2^4)
    print(is_power_of_two(18))   # False
    print(is_power_of_two(1024)) # True  (2^10)
    ```

    A power of two in binary is `100...0`. Subtracting 1 flips all bits below the set bit to `011...1`. The AND of these two values is zero only for powers of two.

??? success "Solution to Exercise 2"

    ```python
    def multiply_by_eight(n):
        return n << 3

    print(multiply_by_eight(5))   # 40
    print(multiply_by_eight(10))  # 80
    print(multiply_by_eight(-3))  # -24
    ```

    Left-shifting by `k` positions multiplies by `2^k`. Shifting by 3 multiplies by `2^3 = 8`.

??? success "Solution to Exercise 3"

    ```python
    def swap_bits(n, i, j):
        # Extract bits at positions i and j
        bit_i = (n >> i) & 1
        bit_j = (n >> j) & 1
        # If bits differ, flip both using XOR
        if bit_i != bit_j:
            n ^= (1 << i) | (1 << j)
        return n

    result = swap_bits(0b1010, 1, 3)
    print(f"{result:#06b}")  # 0b0010 -> 0b0010
    print(result)            # 2
    ```

    If the two bits are different, XOR with a mask that has 1s at both positions flips them, effectively swapping. If they are the same, no change is needed.
"""

# ============================================================================
# OPERATORS
# ============================================================================

EXERCISES["operators/walrus_operator.md"] = """

---

## Exercises

**Exercise 1.**
Rewrite the following code to use the walrus operator so that `len(data)` is computed only once:

```python
data = [1, 2, 3, 4, 5]
if len(data) > 3:
    print(f"Long list with {len(data)} elements")
```

---

**Exercise 2.**
Use the walrus operator in a list comprehension to collect the squares of numbers from 1 to 10, but only include squares greater than 50.

---

**Exercise 3.**
Write a `while` loop that uses the walrus operator to read items from an iterator until `None` is encountered. Use `iter([10, 20, 30, None, 40])` as the data source.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    data = [1, 2, 3, 4, 5]
    if (n := len(data)) > 3:
        print(f"Long list with {n} elements")
    ```

    The walrus operator assigns `len(data)` to `n` and evaluates it in the condition simultaneously, avoiding a redundant call.

??? success "Solution to Exercise 2"

    ```python
    result = [sq for x in range(1, 11) if (sq := x**2) > 50]
    print(result)  # [64, 81, 100]
    ```

    The walrus operator computes `x**2` once per iteration, assigns it to `sq`, uses it in the filter condition, and includes it in the output list.

??? success "Solution to Exercise 3"

    ```python
    data = iter([10, 20, 30, None, 40])

    while (value := next(data, None)) is not None:
        print(f"Processing: {value}")
    # Processing: 10
    # Processing: 20
    # Processing: 30
    ```

    The loop stops when `next()` returns `None`. The value `40` is never reached because `None` appears first and terminates the loop.
"""

EXERCISES["operators/sequence_comparison.md"] = """

---

## Exercises

**Exercise 1.**
Without running the code, predict the result of each comparison and explain why:

```python
print([1, 2, 3] < [1, 2, 4])
print("banana" < "cherry")
print((1, 2) < (1, 2, 0))
```

---

**Exercise 2.**
Write a function `sort_names_case_insensitive(names)` that sorts a list of names lexicographically, ignoring case. For example, `["charlie", "Alice", "Bob"]` should become `["Alice", "Bob", "charlie"]`.

---

**Exercise 3.**
Given a list of `(last_name, first_name)` tuples, sort them by last name first, then by first name. Demonstrate with at least 4 entries where some share the same last name.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    print([1, 2, 3] < [1, 2, 4])   # True  (3 < 4 at index 2)
    print("banana" < "cherry")      # True  ('b' < 'c')
    print((1, 2) < (1, 2, 0))      # True  (prefix match, shorter is less)
    ```

    Lexicographic comparison proceeds element by element. If all compared elements are equal, the shorter sequence is considered less than the longer one.

??? success "Solution to Exercise 2"

    ```python
    def sort_names_case_insensitive(names):
        return sorted(names, key=str.lower)

    result = sort_names_case_insensitive(["charlie", "Alice", "Bob"])
    print(result)  # ['Alice', 'Bob', 'charlie']
    ```

    Using `str.lower` as the key function ensures that comparison ignores case while preserving the original casing in the output.

??? success "Solution to Exercise 3"

    ```python
    people = [
        ("Smith", "Alice"),
        ("Jones", "Bob"),
        ("Smith", "Charlie"),
        ("Jones", "Alice"),
    ]

    sorted_people = sorted(people)
    for last, first in sorted_people:
        print(f"{last}, {first}")
    # Jones, Alice
    # Jones, Bob
    # Smith, Alice
    # Smith, Charlie
    ```

    Tuples are compared lexicographically, so sorting by the tuple itself sorts by last name first, then by first name when last names are equal.
"""

EXERCISES["operators/comparison.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `clamp(value, low, high)` that uses chained comparisons to check if `value` is within the range `[low, high]`. Return `low` if below, `high` if above, or `value` if within range.

---

**Exercise 2.**
Demonstrate the floating-point comparison gotcha with `0.1 + 0.2 == 0.3`. Then fix the comparison using `math.isclose()` with both default and custom tolerances.

---

**Exercise 3.**
Explain the difference between `==` and `is` by creating two lists with the same contents. Show that `==` returns `True` but `is` returns `False`, and explain when to use each.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def clamp(value, low, high):
        if low <= value <= high:
            return value
        elif value < low:
            return low
        else:
            return high

    print(clamp(5, 0, 10))   # 5
    print(clamp(-3, 0, 10))  # 0
    print(clamp(15, 0, 10))  # 10
    ```

    The chained comparison `low <= value <= high` is equivalent to `low <= value and value <= high` but more readable.

??? success "Solution to Exercise 2"

    ```python
    import math

    # The gotcha
    print(0.1 + 0.2 == 0.3)   # False
    print(f"{0.1 + 0.2:.20f}")  # 0.30000000000000004441

    # Fix with math.isclose (default tolerance)
    print(math.isclose(0.1 + 0.2, 0.3))  # True

    # Custom tolerance
    print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9, abs_tol=1e-12))  # True
    ```

    `math.isclose()` uses a relative tolerance (default `1e-9`) to account for floating-point representation errors.

??? success "Solution to Exercise 3"

    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]

    print(a == b)   # True  (same values)
    print(a is b)   # False (different objects)

    c = a
    print(a is c)   # True  (same object)
    ```

    Use `==` to compare values. Use `is` only for singleton comparisons (`None`, `True`, `False`). Two separately created lists are equal in value but are distinct objects in memory.
"""

EXERCISES["operators/identity.md"] = """

---

## Exercises

**Exercise 1.**
Create two empty lists using separate expressions. Verify that they are equal (`==`) but not identical (`is`). Then assign one to the other and verify they become identical.

---

**Exercise 2.**
Demonstrate Python's integer caching by showing that `a is b` is `True` for `a = b = 256` but may be `False` for `a = b = 257`. Explain why you should never rely on this behavior.

---

**Exercise 3.**
Write a function `process(data=None)` that creates a new empty list when no argument is passed. Explain why the check uses `is None` rather than `== None`.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    a = []
    b = []
    print(a == b)   # True  (same contents)
    print(a is b)   # False (different objects)

    c = a
    print(a is c)   # True  (same object)
    ```

    Each `[]` literal creates a new list object. After `c = a`, both names refer to the same object.

??? success "Solution to Exercise 2"

    ```python
    a = 256
    b = 256
    print(a is b)   # True (cached)

    a = 257
    b = 257
    print(a is b)   # May be False (not cached)
    ```

    CPython caches integers from -5 to 256. Beyond that range, each creation may produce a new object. Never use `is` to compare integer values -- always use `==`.

??? success "Solution to Exercise 3"

    ```python
    def process(data=None):
        if data is None:
            data = []
        data.append("processed")
        return data

    print(process())           # ['processed']
    print(process([1, 2, 3]))  # [1, 2, 3, 'processed']
    ```

    `is None` checks identity against the `None` singleton. Using `== None` would work but is not idiomatic, and a custom class could override `__eq__` to return `True` when compared to `None`, leading to unexpected behavior.
"""

EXERCISES["operators/membership.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `find_missing(required, provided)` that takes two sets and returns a sorted list of items in `required` but not in `provided`. Use the `not in` operator.

---

**Exercise 2.**
Demonstrate the performance difference between membership testing in a list versus a set. Create a list and set each containing numbers 0 to 99999, and time how long it takes to check if `99999` is in each.

---

**Exercise 3.**
Given a dictionary `person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}`, show three different membership tests: checking if a key exists, checking if a value exists, and checking if a key-value pair exists.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def find_missing(required, provided):
        return sorted(item for item in required if item not in provided)

    required = {'name', 'email', 'phone', 'address'}
    provided = {'name', 'email'}
    print(find_missing(required, provided))  # ['address', 'phone']
    ```

    The function iterates over `required` and filters items absent from `provided`. Using sets for `provided` ensures O(1) lookup per check.

??? success "Solution to Exercise 2"

    ```python
    import timeit

    setup_list = "lst = list(range(100000))"
    setup_set = "s = set(range(100000))"

    list_time = timeit.timeit("99999 in lst", setup=setup_list, number=1000)
    set_time = timeit.timeit("99999 in s", setup=setup_set, number=1000)

    print(f"List: {list_time:.4f}s")
    print(f"Set:  {set_time:.6f}s")
    print(f"Set is {list_time / set_time:.0f}x faster")
    ```

    List membership is O(n) because Python checks each element sequentially. Set membership is O(1) on average because sets use hash tables.

??? success "Solution to Exercise 3"

    ```python
    person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

    # Check key
    print('name' in person)                        # True

    # Check value
    print('Alice' in person.values())              # True

    # Check key-value pair
    print(('name', 'Alice') in person.items())     # True
    ```

    By default, `in` checks dictionary keys. Use `.values()` to check values and `.items()` to check key-value pairs.
"""

EXERCISES["operators/precedence.md"] = """

---

## Exercises

**Exercise 1.**
Without running the code, evaluate the following expression step by step and give the final result:

```python
result = 2 + 3 * 4 ** 2 / 8 - 1
```

---

**Exercise 2.**
Explain why `5 & 3 == 1` evaluates to `False` and how adding parentheses fixes it to `True`. What precedence rule causes this?

---

**Exercise 3.**
Rewrite the following expression using parentheses to make the evaluation order explicit and unambiguous:

```python
x = not a or b and c > d + e * f
```

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    # Step by step:
    # 1. 4 ** 2 = 16         (exponentiation first)
    # 2. 3 * 16 = 48         (multiplication)
    # 3. 48 / 8 = 6.0        (division)
    # 4. 2 + 6.0 = 8.0       (addition)
    # 5. 8.0 - 1 = 7.0       (subtraction)

    result = 2 + 3 * 4 ** 2 / 8 - 1
    print(result)  # 7.0
    ```

    Exponentiation has the highest precedence among arithmetic operators, followed by multiplication/division (left to right), then addition/subtraction.

??? success "Solution to Exercise 2"

    ```python
    # Without parentheses
    print(5 & 3 == 1)     # False
    # Evaluated as: 5 & (3 == 1) = 5 & False = 0

    # With parentheses
    print((5 & 3) == 1)   # True
    # Evaluated as: (5 & 3) = 1, then 1 == 1 = True
    ```

    Comparison operators (`==`) have higher precedence than bitwise operators (`&`). So `3 == 1` is evaluated first, yielding `False`, and then `5 & False` gives `0`.

??? success "Solution to Exercise 3"

    ```python
    # Original: not a or b and c > d + e * f
    # Fully parenthesized:
    x = (not a) or (b and (c > (d + (e * f))))
    ```

    The precedence order is: `*` > `+` > `>` > `not` > `and` > `or`. Multiplication is evaluated first, then addition, then the comparison, then logical operators from highest to lowest precedence.
"""

EXERCISES["operators/arithmetic.md"] = """

---

## Exercises

**Exercise 1.**
Explain the difference between `/` and `//` for both positive and negative numbers. Show examples where `-7 / 2` and `-7 // 2` give different results and explain why.

---

**Exercise 2.**
Using only `divmod()`, write a function `time_breakdown(total_seconds)` that converts a number of seconds into hours, minutes, and remaining seconds.

---

**Exercise 3.**
Demonstrate that `**` is right-associative by showing that `2 ** 3 ** 2` equals `2 ** 9` (not `8 ** 2`). Then use parentheses to get the left-associative result.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    # True division always returns float
    print(-7 / 2)    # -3.5

    # Floor division rounds toward negative infinity
    print(-7 // 2)   # -4 (not -3!)

    # For positive numbers
    print(7 / 2)     # 3.5
    print(7 // 2)    # 3
    ```

    `/` performs true division and returns a float. `//` performs floor division, rounding toward negative infinity. For `-7 // 2`, the mathematical result is `-3.5`, and the floor of `-3.5` is `-4`.

??? success "Solution to Exercise 2"

    ```python
    def time_breakdown(total_seconds):
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds

    h, m, s = time_breakdown(3725)
    print(f"{h}h {m}m {s}s")  # 1h 2m 5s
    ```

    `divmod(a, b)` returns `(a // b, a % b)` in one call, which is both cleaner and slightly faster than computing quotient and remainder separately.

??? success "Solution to Exercise 3"

    ```python
    # Right-associative (default)
    print(2 ** 3 ** 2)    # 512 (2 ** 9)

    # Left-associative (with parentheses)
    print((2 ** 3) ** 2)  # 64 (8 ** 2)

    # Verify
    print(2 ** 9)         # 512
    print(8 ** 2)         # 64
    ```

    Without parentheses, `2 ** 3 ** 2` is evaluated as `2 ** (3 ** 2) = 2 ** 9 = 512`. This right-to-left associativity matches mathematical convention for exponentiation.
"""

EXERCISES["operators/operators_deep_dive_overview.md"] = """

---

## Exercises

**Exercise 1.**
For the `+` operator, show three different behaviors depending on the operand types: with two integers, with two strings, and with two lists. What determines which behavior is used?

---

**Exercise 2.**
Write a function `type_aware_multiply(a, b)` that checks the types of its arguments and returns a meaningful result: numeric multiplication for numbers, string repetition for `str * int`, and raises `TypeError` for unsupported combinations.

---

**Exercise 3.**
List all seven Python operator categories and give one example of each. For the membership category, show how `in` works differently with a `list` versus a `dict`.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    # Integers: arithmetic addition
    print(3 + 2)              # 5

    # Strings: concatenation
    print("Hello" + " World") # Hello World

    # Lists: concatenation
    print([1, 2] + [3, 4])    # [1, 2, 3, 4]
    ```

    The `+` operator dispatches to the `__add__` method of the left operand. Each type implements `__add__` differently, so behavior depends on the operand's type.

??? success "Solution to Exercise 2"

    ```python
    def type_aware_multiply(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        elif isinstance(a, str) and isinstance(b, int):
            return a * b
        elif isinstance(a, int) and isinstance(b, str):
            return b * a
        else:
            raise TypeError(f"Cannot multiply {type(a).__name__} and {type(b).__name__}")

    print(type_aware_multiply(3, 4))       # 12
    print(type_aware_multiply("ab", 3))    # ababab
    print(type_aware_multiply(3, "ab"))    # ababab
    ```

    The function uses `isinstance()` to check operand types and delegates to the appropriate behavior.

??? success "Solution to Exercise 3"

    ```python
    # 1. Arithmetic
    print(10 + 3)             # 13

    # 2. Comparison
    print(5 > 3)              # True

    # 3. Logical
    print(True and False)     # False

    # 4. Assignment
    x = 10
    x += 5                    # 15

    # 5. Bitwise
    print(5 & 3)              # 1

    # 6. Identity
    print(None is None)       # True

    # 7. Membership
    print(3 in [1, 2, 3])    # True (checks elements)
    d = {'a': 1, 'b': 2}
    print('a' in d)           # True (checks keys, not values)
    ```

    For lists, `in` checks if the value is an element. For dicts, `in` checks if the value is a key.
"""

# ============================================================================
# PERFORMANCE
# ============================================================================

EXERCISES["performance/big_o.md"] = """

---

## Exercises

**Exercise 1.**
Write both a linear search and a binary search for a sorted list. Time each when searching for the last element in a list of 1,000,000 items. Report the time difference.

---

**Exercise 2.**
Write a function that finds all duplicate values in a list. Implement it in two ways: one with O(n^2) time complexity (nested loops) and one with O(n) time complexity (using a set). Compare their performance on a list of 10,000 elements.

---

**Exercise 3.**
Explain why an O(n^2) algorithm with a small constant factor might outperform an O(n log n) algorithm for small input sizes. Demonstrate with a concrete example using `timeit`.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    import time

    def linear_search(arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1

    def binary_search(arr, target):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    data = list(range(1_000_000))
    target = 999_999

    start = time.perf_counter()
    linear_search(data, target)
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    binary_search(data, target)
    binary_time = time.perf_counter() - start

    print(f"Linear: {linear_time:.4f}s")
    print(f"Binary: {binary_time:.6f}s")
    ```

    Linear search checks every element (O(n)), while binary search halves the search space each step (O(log n)).

??? success "Solution to Exercise 2"

    ```python
    import time

    def find_dupes_quadratic(lst):
        dupes = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j] and lst[i] not in dupes:
                    dupes.append(lst[i])
        return dupes

    def find_dupes_linear(lst):
        seen = set()
        dupes = set()
        for item in lst:
            if item in seen:
                dupes.add(item)
            seen.add(item)
        return list(dupes)

    data = list(range(5000)) + list(range(5000))

    start = time.perf_counter()
    find_dupes_quadratic(data)
    quad_time = time.perf_counter() - start

    start = time.perf_counter()
    find_dupes_linear(data)
    lin_time = time.perf_counter() - start

    print(f"O(n^2): {quad_time:.4f}s")
    print(f"O(n):   {lin_time:.6f}s")
    ```

    The set-based approach uses O(1) membership testing, reducing the overall complexity from O(n^2) to O(n).

??? success "Solution to Exercise 3"

    ```python
    import timeit

    # Simple O(n^2) insertion sort vs O(n log n) sorted()
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    n = 10
    setup = f"import random; data = random.sample(range({n}), {n})"

    t_insert = timeit.timeit("insertion_sort(data[:])",
                              setup=setup + "; from __main__ import insertion_sort",
                              number=10000)
    t_sorted = timeit.timeit("sorted(data)",
                              setup=setup,
                              number=10000)

    print(f"Insertion sort (n={n}): {t_insert:.4f}s")
    print(f"sorted() (n={n}):      {t_sorted:.4f}s")
    ```

    For very small inputs, the overhead of O(n log n) algorithms (function calls, more complex logic) can exceed the theoretical advantage. The constant factors dominate when `n` is tiny.
"""

EXERCISES["performance/operation_costs.md"] = """

---

## Exercises

**Exercise 1.**
Compare building a string from 10,000 integers using `+=` concatenation versus `"".join()`. Time both approaches and explain why one is faster.

---

**Exercise 2.**
Show the performance difference between appending to a list with `append()` in a loop versus using a list comprehension. Use `timeit` with 100,000 elements.

---

**Exercise 3.**
Demonstrate the attribute lookup optimization by caching `list.append` in a local variable before a loop. Compare the timed results for 1,000,000 iterations with and without caching.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    import timeit

    code_concat = '''
    result = ""
    for i in range(10000):
        result += str(i)
    '''

    code_join = '''
    result = "".join(str(i) for i in range(10000))
    '''

    t_concat = timeit.timeit(code_concat, number=100)
    t_join = timeit.timeit(code_join, number=100)

    print(f"+= concat: {t_concat:.4f}s")
    print(f"join():    {t_join:.4f}s")
    ```

    String concatenation with `+=` creates a new string object each iteration because strings are immutable. `"".join()` allocates the final string once after computing the total length.

??? success "Solution to Exercise 2"

    ```python
    import timeit

    code_loop = '''
    result = []
    for i in range(100000):
        result.append(i * 2)
    '''

    code_comp = '[i * 2 for i in range(100000)]'

    t_loop = timeit.timeit(code_loop, number=100)
    t_comp = timeit.timeit(code_comp, number=100)

    print(f"Loop + append: {t_loop:.4f}s")
    print(f"Comprehension: {t_comp:.4f}s")
    ```

    List comprehensions are faster because the append operation is handled internally in C bytecode, avoiding the overhead of the `append` method lookup and call on every iteration.

??? success "Solution to Exercise 3"

    ```python
    import timeit

    code_with_dot = '''
    result = []
    for i in range(1000000):
        result.append(i)
    '''

    code_cached = '''
    result = []
    append = result.append
    for i in range(1000000):
        append(i)
    '''

    t_dot = timeit.timeit(code_with_dot, number=10)
    t_cached = timeit.timeit(code_cached, number=10)

    print(f"With dot:    {t_dot:.4f}s")
    print(f"Cached:      {t_cached:.4f}s")
    print(f"Speedup:     {t_dot / t_cached:.2f}x")
    ```

    Caching `result.append` avoids an attribute dictionary lookup on every iteration. For millions of iterations, eliminating one dictionary lookup per cycle produces a measurable speedup.
"""

EXERCISES["performance/timeit.md"] = """

---

## Exercises

**Exercise 1.**
Use `timeit.timeit()` to compare the speed of creating a list using `list(range(1000))` versus `[*range(1000)]`. Run each 10,000 times and report which is faster.

---

**Exercise 2.**
Use `timeit.repeat()` to measure `sum(range(1000))` with 5 repeats of 10,000 executions each. Print the best, worst, and average times.

---

**Exercise 3.**
Write a benchmark that compares three ways to check if a number is even: `n % 2 == 0`, `n & 1 == 0`, and `not n % 2`. Use `timeit` to determine which is fastest.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    import timeit

    t_list = timeit.timeit("list(range(1000))", number=10000)
    t_unpack = timeit.timeit("[*range(1000)]", number=10000)

    print(f"list():    {t_list:.4f}s")
    print(f"[*...]:    {t_unpack:.4f}s")
    ```

    Both create a list from a range, but unpacking (`[*range()]`) can be slightly faster because it avoids the overhead of calling the `list()` constructor function.

??? success "Solution to Exercise 2"

    ```python
    import timeit

    times = timeit.repeat("sum(range(1000))", number=10000, repeat=5)

    print(f"Best:    {min(times):.4f}s")
    print(f"Worst:   {max(times):.4f}s")
    print(f"Average: {sum(times)/len(times):.4f}s")
    ```

    `timeit.repeat()` runs the full measurement multiple times. The best time is the most reliable because higher times include OS scheduling overhead.

??? success "Solution to Exercise 3"

    ```python
    import timeit

    setup = "n = 42"

    t_mod = timeit.timeit("n % 2 == 0", setup=setup, number=1000000)
    t_bit = timeit.timeit("n & 1 == 0", setup=setup, number=1000000)
    t_not = timeit.timeit("not n % 2", setup=setup, number=1000000)

    print(f"n % 2 == 0: {t_mod:.4f}s")
    print(f"n & 1 == 0: {t_bit:.4f}s")
    print(f"not n % 2:  {t_not:.4f}s")
    ```

    All three approaches are very fast for single checks. The bitwise approach (`n & 1`) may be marginally faster since it avoids a comparison, but the difference is negligible in practice.
"""

EXERCISES["performance/tradeoffs.md"] = """

---

## Exercises

**Exercise 1.**
Implement a Fibonacci function in two ways: (a) naive recursion (O(2^n) time, O(n) space) and (b) memoized version using a dictionary (O(n) time, O(n) space). Compare their execution times for `n = 30`.

---

**Exercise 2.**
Demonstrate the time-space tradeoff by implementing a function that checks for duplicate elements in a list. Write one version that uses O(1) extra space (nested loops, O(n^2) time) and one that uses O(n) extra space (set, O(n) time). Compare for a list of 5,000 elements.

---

**Exercise 3.**
Explain why `functools.lru_cache` is an example of the time-space tradeoff. Write a decorated function that computes factorials and show that repeated calls with the same argument are instant after the first call.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    import time

    def fib_naive(n):
        if n <= 1:
            return n
        return fib_naive(n - 1) + fib_naive(n - 2)

    def fib_memo(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]

    start = time.perf_counter()
    fib_naive(30)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    fib_memo(30)
    memo_time = time.perf_counter() - start

    print(f"Naive:    {naive_time:.4f}s")
    print(f"Memoized: {memo_time:.6f}s")
    ```

    Memoization trades O(n) memory for eliminating redundant computation, reducing time from exponential to linear.

??? success "Solution to Exercise 2"

    ```python
    import time

    def has_dupes_quadratic(lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    return True
        return False

    def has_dupes_linear(lst):
        seen = set()
        for item in lst:
            if item in seen:
                return True
            seen.add(item)
        return False

    data = list(range(5000))  # no duplicates (worst case)

    start = time.perf_counter()
    has_dupes_quadratic(data)
    quad_time = time.perf_counter() - start

    start = time.perf_counter()
    has_dupes_linear(data)
    lin_time = time.perf_counter() - start

    print(f"O(n^2): {quad_time:.4f}s")
    print(f"O(n):   {lin_time:.6f}s")
    ```

    The set-based approach uses extra memory proportional to the input size but provides O(1) lookups, making the overall check O(n).

??? success "Solution to Exercise 3"

    ```python
    import functools
    import time

    @functools.lru_cache(maxsize=None)
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    # First call: computes and caches
    start = time.perf_counter()
    factorial(500)
    first_time = time.perf_counter() - start

    # Second call: returns cached result
    start = time.perf_counter()
    factorial(500)
    second_time = time.perf_counter() - start

    print(f"First call:  {first_time:.6f}s")
    print(f"Second call: {second_time:.6f}s")
    print(f"Cache info:  {factorial.cache_info()}")
    ```

    `lru_cache` stores previously computed results in memory (space cost) so that identical calls return instantly (time saving). This is the classic time-space tradeoff.
"""

# ============================================================================
# SCOPE
# ============================================================================

EXERCISES["scope/global_nonlocal.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `increment_counter()` that modifies a global variable `counter` each time it is called. Call it three times and print the final value.

---

**Exercise 2.**
Write a function `make_accumulator(start)` that returns an inner function. Each call to the inner function should add a given amount to the running total (using `nonlocal`) and return the new total.

---

**Exercise 3.**
Explain what happens if you try to use `nonlocal` to reference a global variable. Write code that demonstrates the resulting error.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    counter = 0

    def increment_counter():
        global counter
        counter += 1

    increment_counter()
    increment_counter()
    increment_counter()
    print(counter)  # 3
    ```

    Without `global`, the assignment `counter += 1` would create a local variable, causing an `UnboundLocalError`.

??? success "Solution to Exercise 2"

    ```python
    def make_accumulator(start):
        total = start

        def add(amount):
            nonlocal total
            total += amount
            return total

        return add

    acc = make_accumulator(100)
    print(acc(10))   # 110
    print(acc(20))   # 130
    print(acc(5))    # 135
    ```

    `nonlocal total` allows the inner function to modify `total` in the enclosing scope. Each call updates the same variable.

??? success "Solution to Exercise 3"

    ```python
    x = 10

    def func():
        try:
            # nonlocal x  # Uncommenting causes: SyntaxError
            pass
        except:
            pass

    # nonlocal can only refer to variables in an enclosing function scope,
    # not the global (module-level) scope.
    # To modify a global variable, use 'global' instead.
    ```

    `nonlocal` targets the nearest enclosing function scope. It cannot be used at the module level. For module-level variables, use `global` instead.
"""

EXERCISES["scope/legb_resolution.md"] = """

---

## Exercises

**Exercise 1.**
Write a nested function example that demonstrates all four LEGB scopes. Define a variable with the same name at each level and print which value is seen from the innermost function.

---

**Exercise 2.**
Use `locals()` and `globals()` inside a function to inspect the available namespaces. Define some local variables and print both dictionaries to see the difference.

---

**Exercise 3.**
Create a closure where the inner function captures a variable from the enclosing scope. After calling the outer function, use `__closure__` to inspect the captured value.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    x = "global"

    def outer():
        x = "enclosing"

        def inner():
            x = "local"
            print(f"inner sees: {x}")  # local

        inner()
        print(f"outer sees: {x}")  # enclosing

    outer()
    print(f"module sees: {x}")  # global
    print(f"built-in example: {len([1,2,3])}")  # 3 (built-in)
    ```

    Python searches Local first, then Enclosing, then Global, then Built-in. The first match wins.

??? success "Solution to Exercise 2"

    ```python
    module_var = "I am global"

    def example():
        local_var = "I am local"
        another = 42
        print("Locals:", locals())
        print("Globals contain 'module_var':", 'module_var' in globals())

    example()
    ```

    `locals()` returns a snapshot of the local namespace. `globals()` returns the module-level namespace dictionary, which can be modified directly.

??? success "Solution to Exercise 3"

    ```python
    def outer(value):
        def inner():
            return value
        return inner

    closure = outer(42)
    print(closure())  # 42
    print(closure.__closure__[0].cell_contents)  # 42
    ```

    The inner function captures `value` from the enclosing scope. The `__closure__` attribute contains cell objects holding the captured values.
"""

EXERCISES["scope/scope_lifetime.md"] = """

---

## Exercises

**Exercise 1.**
Write a function that creates a local variable. After the function returns, attempt to access that variable and show that it no longer exists.

---

**Exercise 2.**
Demonstrate that a closure keeps enclosing variables alive even after the outer function returns. Create an outer function that returns an inner function, and show the inner function can still use the outer variable.

---

**Exercise 3.**
Create a global variable, modify it inside a function using the `global` keyword, and show that the change persists after the function call. Then explain the lifetime difference between global and local variables.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def create_local():
        secret = 42
        print(f"Inside function: {secret}")
        return secret

    result = create_local()
    # print(secret)  # NameError: name 'secret' is not defined
    print(f"Returned value: {result}")
    ```

    Local variables are created when the function is called and destroyed when it returns. The name `secret` does not exist outside the function.

??? success "Solution to Exercise 2"

    ```python
    def outer():
        message = "I survive!"

        def inner():
            return message

        return inner

    closure = outer()
    # outer() has returned, but message is kept alive
    print(closure())  # I survive!
    ```

    The inner function holds a reference to `message` through a closure. Python keeps the enclosing variable alive as long as the closure exists.

??? success "Solution to Exercise 3"

    ```python
    count = 0

    def increment():
        global count
        count += 1

    increment()
    increment()
    print(count)  # 2
    ```

    Global variables live for the entire duration of the program. Local variables are created when a function is called and destroyed when it returns. Closures extend the lifetime of enclosing variables beyond the outer function's return.
"""

# ============================================================================
# STRINGS
# ============================================================================

EXERCISES["strings/str_immutability.md"] = """

---

## Exercises

**Exercise 1.**
Show that calling `.upper()` on a string returns a new object by comparing the `id()` of the original and the result. Verify that the original string is unchanged.

---

**Exercise 2.**
Write code that attempts to change the second character of a string using index assignment. Catch the resulting error and then show the correct way to create a modified string using slicing.

---

**Exercise 3.**
Demonstrate string interning by creating two variables with the same short string literal and checking if they are the same object using `is`. Then show a case where interning does not apply.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    original = "hello"
    upper = original.upper()

    print(f"original: {original}, id: {id(original)}")
    print(f"upper:    {upper}, id: {id(upper)}")
    print(f"Same object: {original is upper}")  # False
    ```

    `.upper()` creates a new string object. The original remains unchanged because strings are immutable.

??? success "Solution to Exercise 2"

    ```python
    s = "hello"
    try:
        s[1] = "E"
    except TypeError as e:
        print(f"Error: {e}")

    # Correct approach using slicing
    s_new = s[0] + "E" + s[2:]
    print(s_new)  # hEllo
    print(s)      # hello (unchanged)
    ```

    Strings do not support item assignment. To create a modified version, build a new string from slices of the original.

??? success "Solution to Exercise 3"

    ```python
    a = "hello"
    b = "hello"
    print(a is b)  # True (interned)

    # Interning may not apply for dynamically created strings
    c = "".join(["h", "e", "l", "l", "o"])
    print(a == c)  # True (same value)
    print(a is c)  # May be False (different object)
    ```

    Python interns small string literals as an optimization. However, dynamically constructed strings may not be interned, so `is` may return `False` even when values are equal.
"""

EXERCISES["strings/unicode_normalization.md"] = """

---

## Exercises

**Exercise 1.**
Create two strings that look identical when printed (`"cafe\\u0301"` and `"caf\\u00e9"`) and show that `==` returns `False`. Then use `unicodedata.normalize("NFC", ...)` to make them compare equal.

---

**Exercise 2.**
Write a function `normalize_and_compare(s1, s2)` that returns `True` if two strings are equivalent after NFC normalization. Test it with both precomposed and decomposed forms of accented characters.

---

**Exercise 3.**
Demonstrate the difference between NFC and NFD normalization by showing the `len()` of the same accented string after applying each form.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    from unicodedata import normalize

    s1 = "caf\\u00e9"    # precomposed
    s2 = "cafe\\u0301"   # decomposed

    print(s1 == s2)       # False
    print(normalize("NFC", s1) == normalize("NFC", s2))  # True
    ```

    The two strings have different internal code point sequences despite looking identical. NFC normalization converts both to the same precomposed form.

??? success "Solution to Exercise 2"

    ```python
    from unicodedata import normalize

    def normalize_and_compare(s1, s2):
        return normalize("NFC", s1) == normalize("NFC", s2)

    print(normalize_and_compare("caf\\u00e9", "cafe\\u0301"))  # True
    print(normalize_and_compare("nai\\u0308ve", "na\\u00efve"))  # True
    print(normalize_and_compare("hello", "world"))              # False
    ```

    Normalizing both strings to NFC before comparison ensures equivalent representations match.

??? success "Solution to Exercise 3"

    ```python
    from unicodedata import normalize

    s = "caf\\u00e9"
    nfc = normalize("NFC", s)
    nfd = normalize("NFD", s)

    print(f"NFC: '{nfc}', length: {len(nfc)}")  # 4
    print(f"NFD: '{nfd}', length: {len(nfd)}")  # 5
    ```

    NFC produces precomposed characters (fewer code points), while NFD decomposes characters into base character plus combining marks (more code points). Both render identically.
"""

EXERCISES["strings/unicode_case_folding.md"] = """

---

## Exercises

**Exercise 1.**
Show the difference between `.lower()` and `.casefold()` using the German character `"\\u00df"` (sharp s). Explain why `casefold()` is more suitable for case-insensitive comparison.

---

**Exercise 2.**
Write a `fold_equal(s1, s2)` function that combines NFC normalization and case folding. Test it with `"Cafe\\u0301"` and `"CAFE"`.

---

**Exercise 3.**
Implement a case-insensitive search function `search_users(query, users)` where `users` is a list of name strings. The search should match regardless of case and Unicode representation differences.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    sharp_s = "\\u00df"
    print(f"lower():    '{sharp_s.lower()}'")      # ß (unchanged)
    print(f"casefold(): '{sharp_s.casefold()}'")    # ss

    print("SS".casefold() == sharp_s.casefold())  # True
    print("SS".lower() == sharp_s.lower())        # False
    ```

    `lower()` does not change `ß` because it has no uppercase form. `casefold()` maps it to `ss`, enabling correct case-insensitive matching with `"SS"`.

??? success "Solution to Exercise 2"

    ```python
    from unicodedata import normalize

    def fold_equal(s1, s2):
        return normalize("NFC", s1).casefold() == normalize("NFC", s2).casefold()

    print(fold_equal("Cafe\\u0301", "CAFE"))   # True
    print(fold_equal("\\u00df", "SS"))           # True
    print(fold_equal("hello", "HELLO"))         # True
    ```

    NFC normalization handles representation differences, and `casefold()` handles case differences, making this the most robust comparison approach.

??? success "Solution to Exercise 3"

    ```python
    from unicodedata import normalize

    def fold_equal(s1, s2):
        return normalize("NFC", s1).casefold() == normalize("NFC", s2).casefold()

    def search_users(query, users):
        return [u for u in users if fold_equal(u, query)]

    users = ["Jose\\u0301", "Fran\\u00e7oise", "M\\u00fcller", "alice"]
    print(search_users("jose", users))       # ['José']
    print(search_users("ALICE", users))      # ['alice']
    print(search_users("muller", users))     # ['Müller']
    ```

    By normalizing and folding both the query and each user name, the search handles all case and representation variations.
"""

EXERCISES["strings/unicode_comparison.md"] = """

---

## Exercises

**Exercise 1.**
Demonstrate the three levels of Unicode string comparison (exact, normalized, fold-equal) by comparing `"Cafe\\u0301"` with `"cafe"` at each level.

---

**Exercise 2.**
Write a function that takes a list of Unicode strings and returns them deduplicated using NFC normalization. For example, `["cafe\\u0301", "caf\\u00e9"]` should return a single entry.

---

**Exercise 3.**
Explain when you would use Level 1 (exact), Level 2 (normalized), and Level 3 (fold-equal) comparison. Give a practical example for each level.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    from unicodedata import normalize

    a = "Cafe\\u0301"
    b = "cafe"

    # Level 1: Exact
    print(a == b)  # False

    # Level 2: Normalized (case-sensitive)
    print(normalize("NFC", a) == normalize("NFC", b))  # False

    # Level 3: Fold-equal (case-insensitive)
    print(normalize("NFC", a).casefold() == normalize("NFC", b).casefold())  # True
    ```

    Level 1 fails because representations differ. Level 2 fails because case differs. Level 3 succeeds by handling both differences.

??? success "Solution to Exercise 2"

    ```python
    from unicodedata import normalize

    def deduplicate(strings):
        seen = set()
        result = []
        for s in strings:
            normalized = normalize("NFC", s)
            if normalized not in seen:
                seen.add(normalized)
                result.append(s)
        return result

    strings = ["cafe\\u0301", "caf\\u00e9", "hello", "cafe\\u0301"]
    print(deduplicate(strings))  # Two unique entries
    ```

    By normalizing strings before adding to the set, visually identical strings with different internal representations are treated as duplicates.

??? success "Solution to Exercise 3"

    Level 1 (exact `==`): comparing strings you control, like dictionary keys that were all created in the same way. Example: checking if a config key matches a known constant.

    Level 2 (normalized): comparing identifiers or filenames from different sources where case matters but representation may vary. Example: matching database keys.

    Level 3 (fold-equal): user-facing search or authentication where both case and representation can vary. Example: searching a user directory by name.
"""

EXERCISES["strings/str_ascii_unicode.md"] = """

---

## Exercises

**Exercise 1.**
Use `ord()` and `chr()` to convert the character `'A'` to its code point and back. Then do the same for a non-ASCII character like `'\\u4e16'` (world in Chinese).

---

**Exercise 2.**
Write a function `char_info(c)` that takes a single character and prints its Unicode code point (decimal and hex), its UTF-8 byte representation, and the number of UTF-8 bytes it uses.

---

**Exercise 3.**
Demonstrate that `len("Hello")` counts characters while `len("Hello".encode("utf-8"))` counts bytes. Then show a string where these two values differ significantly.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    # ASCII character
    print(ord('A'))    # 65
    print(chr(65))     # A

    # Non-ASCII character
    print(ord('\\u4e16'))  # 19990
    print(chr(19990))      # 世
    ```

    `ord()` converts a character to its Unicode code point (an integer). `chr()` converts a code point back to a character.

??? success "Solution to Exercise 2"

    ```python
    def char_info(c):
        code_point = ord(c)
        utf8_bytes = c.encode("utf-8")
        print(f"Character: {c}")
        print(f"Code point: {code_point} (U+{code_point:04X})")
        print(f"UTF-8 bytes: {utf8_bytes}")
        print(f"Byte count: {len(utf8_bytes)}")

    char_info('A')    # 1 byte
    char_info('\\u00f1')  # 2 bytes (ñ)
    char_info('\\u4e16')  # 3 bytes (世)
    char_info('\\U0001F600')  # 4 bytes (emoji)
    ```

    Each character uses 1 to 4 bytes in UTF-8 depending on its code point range.

??? success "Solution to Exercise 3"

    ```python
    s = "Hello"
    print(f"Characters: {len(s)}, Bytes: {len(s.encode('utf-8'))}")
    # Characters: 5, Bytes: 5

    s = "\\u4f60\\u597d\\u4e16\\u754c"  # 你好世界
    print(f"Characters: {len(s)}, Bytes: {len(s.encode('utf-8'))}")
    # Characters: 4, Bytes: 12
    ```

    ASCII characters use 1 byte each in UTF-8, so character count equals byte count. Chinese characters use 3 bytes each, so 4 characters produce 12 bytes.
"""

EXERCISES["strings/fstring_debugging.md"] = """

---

## Exercises

**Exercise 1.**
Use the `=` specifier in an f-string to debug-print the values of `x = 10`, `y = 20`, and their sum `x + y` in a single print statement.

---

**Exercise 2.**
Combine the `=` specifier with a format specifier to print a float variable with 2 decimal places in debug format. For example, `pi = 3.14159` should output something like `pi=3.14`.

---

**Exercise 3.**
Show the difference between `f"{name=}"`, `f"{name=!s}"`, and `f"{name=!r}"` when `name = "Alice"`. Explain when you would use each form.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    x = 10
    y = 20
    print(f"{x=}, {y=}, {x + y=}")
    # x=10, y=20, x + y=30
    ```

    The `=` specifier automatically includes both the expression text and its value, which is ideal for quick debugging.

??? success "Solution to Exercise 2"

    ```python
    pi = 3.14159
    print(f"{pi=:.2f}")
    # pi=3.14
    ```

    The format specifier (`.2f`) is placed after the `=` to control how the value is displayed while still showing the variable name.

??? success "Solution to Exercise 3"

    ```python
    name = "Alice"
    print(f"{name=}")     # name='Alice'  (repr by default)
    print(f"{name=!s}")   # name=Alice    (str conversion)
    print(f"{name=!r}")   # name='Alice'  (explicit repr)
    ```

    By default, `=` uses `repr()`, which adds quotes around strings. Use `!s` for human-readable output (no quotes) and `!r` for unambiguous representation (with quotes).
"""

EXERCISES["strings/str_align_methods.md"] = """

---

## Exercises

**Exercise 1.**
Format a simple table with names left-aligned in a 15-character field and scores right-aligned in a 5-character field. Use `ljust()` and `rjust()`.

---

**Exercise 2.**
Use `zfill()` to format a list of integers `[1, 12, 123, 1234]` as zero-padded 6-digit strings. Show how `zfill()` handles negative numbers.

---

**Exercise 3.**
Recreate the same alignment from Exercise 1 using f-string format specifiers (`<`, `>`) instead of the alignment methods. Show both approaches produce identical output.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    data = [("Alice", 95), ("Bob", 87), ("Carol", 100)]

    for name, score in data:
        print(name.ljust(15) + str(score).rjust(5))
    # Alice              95
    # Bob                87
    # Carol             100
    ```

    `ljust(15)` pads the name with spaces on the right, and `rjust(5)` pads the score with spaces on the left.

??? success "Solution to Exercise 2"

    ```python
    numbers = [1, 12, 123, 1234]
    for n in numbers:
        print(str(n).zfill(6))
    # 000001
    # 000012
    # 000123
    # 001234

    # Handles negative numbers
    print(str(-42).zfill(6))  # -00042
    ```

    `zfill()` inserts zeros between the sign character and the digits, unlike `rjust()` which would pad before the sign.

??? success "Solution to Exercise 3"

    ```python
    data = [("Alice", 95), ("Bob", 87), ("Carol", 100)]

    # Using alignment methods
    for name, score in data:
        print(name.ljust(15) + str(score).rjust(5))

    print()

    # Using f-string format specifiers
    for name, score in data:
        print(f"{name:<15}{score:>5}")
    ```

    Both approaches produce identical output. F-string format specifiers are more concise and commonly preferred for inline formatting.
"""

EXERCISES["strings/str_encode_decode.md"] = """

---

## Exercises

**Exercise 1.**
Encode the string `"Hello, World!"` in UTF-8, then decode it back. Verify that the decoded string equals the original.

---

**Exercise 2.**
Encode the string `"\\u4f60\\u597d"` (Chinese for "hello") in UTF-8 and print the resulting bytes. Then count the number of bytes and compare it to `len()` of the original string.

---

**Exercise 3.**
Demonstrate a `UnicodeEncodeError` by trying to encode a non-ASCII string with the `"ascii"` codec. Then handle the error using the `"replace"` and `"ignore"` error handlers.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    original = "Hello, World!"
    encoded = original.encode("utf-8")
    decoded = encoded.decode("utf-8")

    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Equal: {original == decoded}")  # True
    ```

    `encode()` converts a string to bytes, and `decode()` converts bytes back to a string. The round-trip preserves the original content.

??? success "Solution to Exercise 2"

    ```python
    text = "\\u4f60\\u597d"  # 你好
    encoded = text.encode("utf-8")

    print(f"String: {text}")
    print(f"Bytes: {encoded}")
    print(f"Character count: {len(text)}")  # 2
    print(f"Byte count: {len(encoded)}")    # 6
    ```

    Each Chinese character uses 3 bytes in UTF-8, so 2 characters produce 6 bytes.

??? success "Solution to Exercise 3"

    ```python
    text = "Caf\\u00e9"

    try:
        text.encode("ascii")
    except UnicodeEncodeError as e:
        print(f"Error: {e}")

    print(text.encode("ascii", errors="replace"))  # b'Caf?'
    print(text.encode("ascii", errors="ignore"))   # b'Caf'
    ```

    ASCII cannot represent `\\u00e9` (é). The `"replace"` handler substitutes `?`, and `"ignore"` silently drops the character.
"""

EXERCISES["strings/str_format_specifiers.md"] = """

---

## Exercises

**Exercise 1.**
Format the number `1234567.891` as: (a) a float with 2 decimal places and comma separators, (b) scientific notation with 3 decimal places, and (c) a percentage (treating it as a ratio).

---

**Exercise 2.**
Create a formatted table of 4 items showing a left-aligned name (20 chars), right-aligned price (10 chars, 2 decimal places), and centered status (10 chars). Use f-string format specifiers.

---

**Exercise 3.**
Use the `#` prefix to display the number `255` in binary, octal, and hexadecimal with their respective prefixes (`0b`, `0o`, `0x`).

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    n = 1234567.891

    print(f"{n:,.2f}")     # 1,234,567.89
    print(f"{n:.3e}")      # 1.235e+06
    print(f"{n:.1%}")      # 123456789.1%
    ```

    The `,` flag adds thousand separators, `e` switches to scientific notation, and `%` multiplies by 100 and appends a percent sign.

??? success "Solution to Exercise 2"

    ```python
    items = [
        ("Widget", 19.99, "In Stock"),
        ("Gadget", 149.50, "Low"),
        ("Thingamajig", 5.00, "Out"),
        ("Doohickey", 89.99, "In Stock"),
    ]

    print(f"{'Name':<20}{'Price':>10}{'Status':^10}")
    print("-" * 40)
    for name, price, status in items:
        print(f"{name:<20}{price:>10.2f}{status:^10}")
    ```

    `<` left-aligns, `>` right-aligns, and `^` centers. The width specifies the minimum field size.

??? success "Solution to Exercise 3"

    ```python
    n = 255

    print(f"{n:#b}")   # 0b11111111
    print(f"{n:#o}")   # 0o377
    print(f"{n:#x}")   # 0xff
    print(f"{n:#X}")   # 0XFF
    ```

    The `#` flag adds the base prefix (`0b`, `0o`, `0x`). Using `X` instead of `x` produces uppercase hex digits.
"""

EXERCISES["strings/str_utf8_encoding.md"] = """

---

## Exercises

**Exercise 1.**
Encode the string `"A \\u00f1 \\u4e16 \\U0001F600"` in UTF-8 and print the list of byte values. Identify which bytes belong to each character.

---

**Exercise 2.**
Write a function `utf8_byte_count(s)` that returns a dictionary mapping each character in the string to the number of UTF-8 bytes it uses. Test with a string containing ASCII, European, Asian, and emoji characters.

---

**Exercise 3.**
Demonstrate that an ASCII-encoded file is also valid UTF-8 by encoding `"Hello"` with both `"ascii"` and `"utf-8"` codecs and showing the byte sequences are identical.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    text = "A \\u00f1 \\u4e16 \\U0001F600"
    encoded = text.encode("utf-8")

    print(f"String: {text}")
    print(f"Bytes: {list(encoded)}")
    # A: [65], space: [32], ñ: [195, 177], space: [32],
    # 世: [228, 184, 150], space: [32], 😀: [240, 159, 152, 128]
    ```

    ASCII characters use 1 byte, `\\u00f1` uses 2 bytes, `\\u4e16` uses 3 bytes, and the emoji uses 4 bytes.

??? success "Solution to Exercise 2"

    ```python
    def utf8_byte_count(s):
        return {c: len(c.encode("utf-8")) for c in s}

    result = utf8_byte_count("A\\u00f1\\u4e16\\U0001F600")
    for char, count in result.items():
        print(f"'{char}' (U+{ord(char):04X}): {count} bytes")
    ```

    Each character is encoded individually, and the length of the resulting bytes object gives the UTF-8 byte count.

??? success "Solution to Exercise 3"

    ```python
    text = "Hello"

    ascii_bytes = text.encode("ascii")
    utf8_bytes = text.encode("utf-8")

    print(f"ASCII: {ascii_bytes}")
    print(f"UTF-8: {utf8_bytes}")
    print(f"Identical: {ascii_bytes == utf8_bytes}")  # True
    ```

    UTF-8 was designed so that all ASCII characters (U+0000 to U+007F) are encoded using the exact same single-byte values as ASCII.
"""

# ============================================================================
# TYPING
# ============================================================================

EXERCISES["typing/type_conversion.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `safe_convert(value, target_type)` that attempts to convert `value` to `target_type` (e.g., `int`, `float`, `str`). If conversion fails, return `None` instead of raising an error.

---

**Exercise 2.**
Demonstrate the difference between `int(3.9)` (truncation) and `round(3.9)` (rounding). Then show how to use `math.floor()` and `math.ceil()` for explicit directional conversion.

---

**Exercise 3.**
Convert the list `[1, 2, 2, 3, 3, 3]` to a `set`, then to a sorted `list`, then to a `tuple`. Print the result at each step and explain what each conversion does.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def safe_convert(value, target_type):
        try:
            return target_type(value)
        except (ValueError, TypeError):
            return None

    print(safe_convert("42", int))      # 42
    print(safe_convert("hello", int))   # None
    print(safe_convert("3.14", float))  # 3.14
    print(safe_convert(42, str))        # '42'
    ```

    The `try/except` block catches both `ValueError` (invalid literal) and `TypeError` (unsupported conversion) to provide safe conversion.

??? success "Solution to Exercise 2"

    ```python
    import math

    print(int(3.9))         # 3 (truncates toward zero)
    print(round(3.9))       # 4 (rounds to nearest)
    print(math.floor(3.9))  # 3 (rounds toward -inf)
    print(math.ceil(3.9))   # 4 (rounds toward +inf)

    # Negative number
    print(int(-3.9))         # -3 (truncates toward zero)
    print(math.floor(-3.9))  # -4 (rounds toward -inf)
    ```

    `int()` truncates toward zero, `math.floor()` rounds toward negative infinity, and `math.ceil()` rounds toward positive infinity. The difference is visible with negative numbers.

??? success "Solution to Exercise 3"

    ```python
    original = [1, 2, 2, 3, 3, 3]

    as_set = set(original)
    print(f"Set: {as_set}")          # {1, 2, 3} (duplicates removed)

    as_sorted_list = sorted(as_set)
    print(f"Sorted list: {as_sorted_list}")  # [1, 2, 3]

    as_tuple = tuple(as_sorted_list)
    print(f"Tuple: {as_tuple}")      # (1, 2, 3)
    ```

    `set()` removes duplicates, `sorted()` returns a new sorted list, and `tuple()` converts the list to an immutable tuple.
"""

EXERCISES["typing/type_function.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `type_name(obj)` that returns the name of the object's type as a string (e.g., `"int"`, `"str"`, `"list"`). Test with at least 5 different types.

---

**Exercise 2.**
Demonstrate the difference between `type()` and `isinstance()` with class inheritance. Create a base class `Animal` and a subclass `Dog`, then show how each function behaves when checking a `Dog` instance against `Animal`.

---

**Exercise 3.**
Write a function `describe(obj)` that uses `isinstance()` to return different descriptions based on the object's type: `"number"` for `int` or `float`, `"text"` for `str`, `"collection"` for `list`, `tuple`, or `set`, and `"unknown"` otherwise.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def type_name(obj):
        return type(obj).__name__

    print(type_name(42))         # int
    print(type_name("hello"))    # str
    print(type_name([1, 2]))     # list
    print(type_name((1, 2)))     # tuple
    print(type_name({1: 2}))     # dict
    ```

    `type(obj).__name__` accesses the name attribute of the type object, giving a clean string representation.

??? success "Solution to Exercise 2"

    ```python
    class Animal:
        pass

    class Dog(Animal):
        pass

    dog = Dog()

    # type() checks exact type
    print(type(dog) == Dog)      # True
    print(type(dog) == Animal)   # False

    # isinstance() checks inheritance chain
    print(isinstance(dog, Dog))     # True
    print(isinstance(dog, Animal))  # True
    ```

    `type()` checks the exact type only. `isinstance()` checks the entire inheritance chain, making it the preferred choice for most type checking.

??? success "Solution to Exercise 3"

    ```python
    def describe(obj):
        if isinstance(obj, (int, float)):
            return "number"
        elif isinstance(obj, str):
            return "text"
        elif isinstance(obj, (list, tuple, set)):
            return "collection"
        else:
            return "unknown"

    print(describe(42))          # number
    print(describe("hello"))     # text
    print(describe([1, 2, 3]))   # collection
    print(describe(None))        # unknown
    ```

    Passing a tuple of types to `isinstance()` checks if the object is an instance of any of the listed types.
"""

EXERCISES["typing/static_vs_dynamic.md"] = """

---

## Exercises

**Exercise 1.**
Demonstrate Python's dynamic typing by creating a variable, assigning it an integer, then a string, then a list. Print the type at each step.

---

**Exercise 2.**
Write a function with type hints: `def add(a: int, b: int) -> int`. Show that Python does not enforce the hints at runtime by passing strings instead of integers.

---

**Exercise 3.**
Demonstrate duck typing by writing a function `get_length(obj)` that calls `len()` on its argument. Show that it works with strings, lists, tuples, and dictionaries without any type checking.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    x = 42
    print(f"{x}, type: {type(x)}")   # 42, type: <class 'int'>

    x = "hello"
    print(f"{x}, type: {type(x)}")   # hello, type: <class 'str'>

    x = [1, 2, 3]
    print(f"{x}, type: {type(x)}")   # [1, 2, 3], type: <class 'list'>
    ```

    Python variables are names that can be rebound to objects of any type. The type is determined at runtime based on the current object.

??? success "Solution to Exercise 2"

    ```python
    def add(a: int, b: int) -> int:
        return a + b

    # Works with correct types
    print(add(1, 2))         # 3

    # Also works with strings (no runtime enforcement)
    print(add("Hello", " World"))  # Hello World
    ```

    Type hints are documentation for developers and tools like `mypy`. Python ignores them at runtime, so any type that supports `+` will work.

??? success "Solution to Exercise 3"

    ```python
    def get_length(obj):
        return len(obj)

    print(get_length("hello"))       # 5
    print(get_length([1, 2, 3]))     # 3
    print(get_length((1, 2)))        # 2
    print(get_length({'a': 1}))      # 1
    ```

    Python does not check the type of `obj`. It only checks whether the object supports `len()` (i.e., has a `__len__` method). This is duck typing: if it supports the operation, it works.
"""

EXERCISES["typing/dynamic_typing.md"] = """

---

## Exercises

**Exercise 1.**
Write a function `double(x)` that returns `x * 2`. Show that it works with an integer, a string, and a list, producing different behavior for each type.

---

**Exercise 2.**
Create two classes, `Cat` and `Robot`, each with a `speak()` method. Write a function `make_speak(thing)` that calls `thing.speak()` without checking the type. Demonstrate duck typing.

---

**Exercise 3.**
Show what happens when duck typing fails by calling `len()` on an integer. Catch the `TypeError` and print a meaningful error message.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    def double(x):
        return x * 2

    print(double(5))         # 10
    print(double("hi"))      # hihi
    print(double([1, 2]))    # [1, 2, 1, 2]
    ```

    The `*` operator behaves differently depending on the type: arithmetic multiplication for numbers, repetition for strings and lists.

??? success "Solution to Exercise 2"

    ```python
    class Cat:
        def speak(self):
            return "Meow!"

    class Robot:
        def speak(self):
            return "Beep boop!"

    def make_speak(thing):
        return thing.speak()

    print(make_speak(Cat()))    # Meow!
    print(make_speak(Robot()))  # Beep boop!
    ```

    `make_speak()` does not check the type of its argument. It only requires that the object has a `speak()` method. This is duck typing in action.

??? success "Solution to Exercise 3"

    ```python
    try:
        result = len(42)
    except TypeError as e:
        print(f"TypeError: {e}")
        # TypeError: object of type 'int' has no len()
    ```

    Duck typing fails when the object does not support the required operation. Integers have no `__len__` method, so `len(42)` raises a `TypeError`.
"""

# ============================================================================
# VARIABLES
# ============================================================================

EXERCISES["variables/assignment.md"] = """

---

## Exercises

**Exercise 1.**
Create a variable `x = [1, 2, 3]` and assign `y = x`. Modify `y` by appending `4`. Print both `x` and `y` and explain why `x` also changed.

---

**Exercise 2.**
Use tuple unpacking to swap two variables `a = 10` and `b = 20` without using a temporary variable. Then use starred unpacking to extract the first and last elements from a list of 10 numbers.

---

**Exercise 3.**
Demonstrate the difference between chained assignment (`a = b = [1,2,3]`) and separate assignment (`a = [1,2,3]; b = [1,2,3]`). Show that chained assignment creates shared references while separate assignment creates independent objects.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    x = [1, 2, 3]
    y = x
    y.append(4)
    print(x)  # [1, 2, 3, 4]
    print(y)  # [1, 2, 3, 4]
    ```

    `y = x` does not copy the list. Both `x` and `y` are names pointing to the same object. Modifying through either name affects the shared object.

??? success "Solution to Exercise 2"

    ```python
    a, b = 10, 20
    a, b = b, a
    print(f"{a=}, {b=}")  # a=20, b=10

    numbers = list(range(10))
    first, *middle, last = numbers
    print(f"{first=}, {last=}")  # first=0, last=9
    ```

    Swap works by creating a tuple `(b, a)` on the right side and unpacking it. The starred expression `*middle` collects all elements between first and last.

??? success "Solution to Exercise 3"

    ```python
    # Chained: same object
    a = b = [1, 2, 3]
    a.append(4)
    print(b)  # [1, 2, 3, 4] (shared reference)

    # Separate: different objects
    a = [1, 2, 3]
    b = [1, 2, 3]
    a.append(4)
    print(b)  # [1, 2, 3] (independent)
    ```

    Chained assignment binds all names to the same object. Separate assignments create distinct objects, even if the values are identical.
"""

EXERCISES["variables/shorthand_operators.md"] = """

---

## Exercises

**Exercise 1.**
Show the difference between `+=` and `+` for lists. Create a list, use `+=` to extend it, and show the `id()` does not change. Then use `+` and show the `id()` does change.

---

**Exercise 2.**
Write a loop that computes the sum of squares from 1 to 100 using the `+=` operator. Then show the equivalent one-liner using `sum()` with a generator.

---

**Exercise 3.**
Demonstrate that `+=` on a string creates a new object (since strings are immutable) by checking the `id()` before and after the operation.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    # += modifies in place (same object)
    lst = [1, 2, 3]
    original_id = id(lst)
    lst += [4, 5]
    print(f"Same object: {id(lst) == original_id}")  # True

    # + creates new object
    lst = [1, 2, 3]
    original_id = id(lst)
    lst = lst + [4, 5]
    print(f"Same object: {id(lst) == original_id}")  # False
    ```

    For mutable types like lists, `+=` calls `__iadd__` (in-place addition). The `+` operator calls `__add__` and creates a new list.

??? success "Solution to Exercise 2"

    ```python
    # Using += in a loop
    total = 0
    for i in range(1, 101):
        total += i ** 2
    print(total)  # 338350

    # One-liner equivalent
    print(sum(i ** 2 for i in range(1, 101)))  # 338350
    ```

    Both approaches compute the same result. The `sum()` with generator is more Pythonic and avoids the explicit loop.

??? success "Solution to Exercise 3"

    ```python
    s = "hello"
    original_id = id(s)
    s += " world"
    print(f"Same object: {id(s) == original_id}")  # False
    print(s)  # hello world
    ```

    Strings are immutable, so `+=` cannot modify the original object. Python creates a new string and rebinds the variable to it.
"""

EXERCISES["variables/chained_assignment.md"] = """

---

## Exercises

**Exercise 1.**
Use chained assignment to initialize three counter variables to zero. Increment only one of them and show the others remain unchanged. Explain why this is safe.

---

**Exercise 2.**
Demonstrate the danger of chained assignment with mutable objects. Assign `a = b = c = []`, then append to `a` and show that `b` and `c` are also affected.

---

**Exercise 3.**
Write code that creates three independent empty lists (not sharing references) in a single line without chained assignment. Verify with `is` that they are different objects.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    wins = losses = draws = 0
    wins += 1
    print(f"{wins=}, {losses=}, {draws=}")
    # wins=1, losses=0, draws=0
    ```

    This is safe because integers are immutable. `wins += 1` rebinds `wins` to a new integer object, leaving `losses` and `draws` bound to the original `0`.

??? success "Solution to Exercise 2"

    ```python
    a = b = c = []
    a.append(1)
    print(f"{a=}")  # [1]
    print(f"{b=}")  # [1] (same object!)
    print(f"{c=}")  # [1] (same object!)
    print(a is b is c)  # True
    ```

    All three names point to the same list object. Mutating through any name affects all of them.

??? success "Solution to Exercise 3"

    ```python
    a, b, c = [], [], []
    print(a is b)  # False
    print(b is c)  # False
    ```

    Each `[]` literal creates a new list object. Tuple unpacking assigns each name to a separate object.
"""

EXERCISES["variables/language_comparison.md"] = """

---

## Exercises

**Exercise 1.**
Create a list, assign it to another variable, and modify it through the second variable. Show that the original is also modified. Explain how this differs from C's value semantics.

---

**Exercise 2.**
Write a function that takes a list and appends an element. Show that the caller's list is modified. Then write a version that works on a copy so the caller's list is unchanged.

---

**Exercise 3.**
Use `copy.deepcopy()` to create a completely independent copy of a nested list. Modify the copy and show the original is unchanged.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    x = [1, 2, 3]
    y = x
    y.append(4)
    print(x)  # [1, 2, 3, 4]
    ```

    In Python, `y = x` creates an alias (both refer to the same object). In C, `int y = x` copies the value, so modifications to `y` would not affect `x`.

??? success "Solution to Exercise 2"

    ```python
    def modify_original(lst):
        lst.append(99)

    def modify_copy(lst):
        local = lst.copy()
        local.append(99)
        return local

    data = [1, 2, 3]
    modify_original(data)
    print(data)  # [1, 2, 3, 99]

    data = [1, 2, 3]
    result = modify_copy(data)
    print(data)    # [1, 2, 3] (unchanged)
    print(result)  # [1, 2, 3, 99]
    ```

    Python passes object references to functions. To avoid modifying the caller's data, explicitly copy it with `.copy()`.

??? success "Solution to Exercise 3"

    ```python
    import copy

    original = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original)

    deep[0].append(99)
    print(original)  # [[1, 2], [3, 4]] (unchanged)
    print(deep)      # [[1, 2, 99], [3, 4]]
    ```

    `deepcopy()` recursively copies all nested objects. A shallow copy (`list.copy()`) would only copy the outer list, leaving inner lists shared.
"""

EXERCISES["variables/simultaneous_assignment.md"] = """

---

## Exercises

**Exercise 1.**
Use simultaneous assignment to swap three variables `a = 1, b = 2, c = 3` so that `a` gets `c`'s value, `b` gets `a`'s value, and `c` gets `b`'s value. Do it in one line.

---

**Exercise 2.**
Write a function that returns three values (name, age, city). Use tuple unpacking to capture the results. Then use starred unpacking to capture only the first value and collect the rest.

---

**Exercise 3.**
Demonstrate nested unpacking by extracting values from the structure `((1, 2), (3, 4), (5, 6))` into six separate variables in a single assignment.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    a, b, c = 1, 2, 3
    a, b, c = c, a, b
    print(f"{a=}, {b=}, {c=}")
    # a=3, b=1, c=2
    ```

    The right side creates a tuple `(c, a, b)` = `(3, 1, 2)` before any assignments happen, then unpacks it to the left side.

??? success "Solution to Exercise 2"

    ```python
    def get_info():
        return "Alice", 30, "NYC"

    # Full unpacking
    name, age, city = get_info()
    print(f"{name=}, {age=}, {city=}")

    # Starred unpacking
    name, *rest = get_info()
    print(f"{name=}, {rest=}")  # rest=[30, 'NYC']
    ```

    Python functions return tuples implicitly when using comma-separated values. The caller unpacks them directly.

??? success "Solution to Exercise 3"

    ```python
    data = ((1, 2), (3, 4), (5, 6))
    (a, b), (c, d), (e, f) = data
    print(f"{a=}, {b=}, {c=}, {d=}, {e=}, {f=}")
    # a=1, b=2, c=3, d=4, e=5, f=6
    ```

    Nested parentheses on the left side match the structure of the nested tuples on the right, unpacking each level.
"""

EXERCISES["variables/names_not_containers.md"] = """

---

## Exercises

**Exercise 1.**
Create a list and bind three names to it. Delete one name using `del`. Show that the other two names still work and the list still exists.

---

**Exercise 2.**
Write a function that takes a list, reassigns the parameter to a new list inside the function, and returns nothing. Show that the caller's list is unchanged, demonstrating that reassignment rebinds the local name only.

---

**Exercise 3.**
Demonstrate the difference between mutation (modifying through a name) and reassignment (rebinding a name) by starting with `x = y = [1, 2, 3]`. First mutate through `x`, then reassign `x`, and show the effect on `y` in each case.

---

## Solutions

??? success "Solution to Exercise 1"

    ```python
    lst = [1, 2, 3]
    a = lst
    b = lst
    c = lst

    del a
    print(b)  # [1, 2, 3] (still works)
    print(c)  # [1, 2, 3] (still works)
    # print(a)  # NameError: name 'a' is not defined
    ```

    `del a` removes the name `a` but does not delete the object. The object remains alive as long as at least one name references it.

??? success "Solution to Exercise 2"

    ```python
    def try_reassign(lst):
        lst = [10, 20, 30]  # Rebinds local name only
        print(f"Inside function: {lst}")

    data = [1, 2, 3]
    try_reassign(data)
    print(f"Outside function: {data}")  # [1, 2, 3] (unchanged)
    ```

    Reassignment inside the function creates a new local binding. It does not affect the caller's variable because only the local name is rebound.

??? success "Solution to Exercise 3"

    ```python
    x = y = [1, 2, 3]

    # Mutation: affects both names
    x.append(4)
    print(f"After mutation: {x=}, {y=}")
    # x=[1, 2, 3, 4], y=[1, 2, 3, 4]

    # Reassignment: only affects x
    x = [10, 20]
    print(f"After reassignment: {x=}, {y=}")
    # x=[10, 20], y=[1, 2, 3, 4]
    ```

    Mutation modifies the shared object, so both names see the change. Reassignment makes `x` point to a new object, leaving `y` pointing to the original.
"""


def append_exercises():
    for rel_path, content in EXERCISES.items():
        full_path = os.path.join(BASE, rel_path)
        if not os.path.isfile(full_path):
            print(f"NOT FOUND: {rel_path}")
            continue
        with open(full_path, "r", encoding="utf-8") as f:
            existing = f.read()
        if "## Exercises" in existing:
            print(f"SKIP (already has exercises): {rel_path}")
            continue
        with open(full_path, "a", encoding="utf-8") as f:
            f.write(content)
        print(f"DONE: {rel_path}")


if __name__ == "__main__":
    append_exercises()
