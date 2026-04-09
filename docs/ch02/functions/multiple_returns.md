
# Multiple Return Values

## The Mental Model

A function can only `return` one object. But Python makes it easy to pack multiple values into a single object---a **tuple**---and unpack them on the other side. This creates the appearance of returning multiple values, and it is one of Python's most convenient features.

Think of it this way: a function can only hand you one package. But that package can be a box containing several items. You open the box and lay the items out separately. The "multiple return values" pattern is exactly this: packing items into a tuple on the way out, and unpacking them on the way in.

## Tuple Packing in Return Statements

When a `return` statement has multiple comma-separated values, Python automatically packs them into a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([3, 1, 4, 1, 5, 9])
print(result)       # (1, 9)
print(type(result)) # <class 'tuple'>
```

The `return min(numbers), max(numbers)` is equivalent to `return (min(numbers), max(numbers))`. The parentheses are optional---it is the **comma** that makes a tuple, not the parentheses.

## Tuple Unpacking

The caller can unpack the returned tuple into separate variables:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max([3, 1, 4, 1, 5, 9])
print(smallest)  # 1
print(largest)   # 9
```

The assignment `smallest, largest = min_max(...)` unpacks the two-element tuple into two names. The number of names on the left must match the number of elements in the tuple.

```python
# This raises ValueError: not enough values to unpack
a, b, c = min_max([1, 2, 3])  # tuple has 2 elements, but 3 names
```

## Practical Examples

### Divmod: Quotient and Remainder

```python
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 = 5 * {q} + {r}")  # 17 = 5 * 3 + 2
```

Python has a built-in for this: `divmod(17, 5)` returns `(3, 2)`.

### Splitting Data

```python
def split_first_rest(items):
    return items[0], items[1:]

first, rest = split_first_rest([10, 20, 30, 40])
print(first)  # 10
print(rest)   # [20, 30, 40]
```

### Computing Multiple Statistics

```python
def describe(numbers):
    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    sorted_nums = sorted(numbers)
    median = sorted_nums[n // 2]
    return n, total, mean, median

count, total, average, mid = describe([7, 2, 9, 4, 5])
print(f"Count: {count}, Total: {total}, Mean: {average:.1f}, Median: {mid}")
# Count: 5, Total: 27, Mean: 5.4, Median: 5
```

## Ignoring Unwanted Values

If you only need some of the returned values, use `_` as a convention for discarded values:

```python
_, remainder = divide_with_remainder(17, 5)
print(remainder)  # 2
```

For functions that return many values, you can use extended unpacking:

```python
first, *middle, last = (1, 2, 3, 4, 5)
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

## Named Tuples for Clarity

When a function returns more than two or three values, positional unpacking becomes error-prone. The caller must remember the order:

```python
# Which is which? Easy to confuse.
a, b, c, d = describe([7, 2, 9, 4, 5])
```

**Named tuples** solve this by giving each element a name:

```python
from collections import namedtuple

Stats = namedtuple("Stats", ["count", "total", "mean", "median"])

def describe(numbers):
    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    sorted_nums = sorted(numbers)
    median = sorted_nums[n // 2]
    return Stats(count=n, total=total, mean=mean, median=median)

result = describe([7, 2, 9, 4, 5])
print(result.count)    # 5
print(result.mean)     # 5.4
print(result.median)   # 5
print(result)           # Stats(count=5, total=27, mean=5.4, median=5)
```

Named tuples behave like regular tuples (you can still unpack them) but also support attribute access:

```python
# Both work
count, total, mean, median = describe([7, 2, 9, 4, 5])  # positional
result = describe([7, 2, 9, 4, 5])                        # named access
```

### Using typing.NamedTuple

The modern way to define named tuples uses class syntax with type annotations:

```python
from typing import NamedTuple

class Stats(NamedTuple):
    count: int
    total: float
    mean: float
    median: float

def describe(numbers):
    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    sorted_nums = sorted(numbers)
    median = sorted_nums[n // 2]
    return Stats(count=n, total=total, mean=mean, median=median)
```

This is functionally identical but provides type hints and reads more naturally.

## Returning Dictionaries for Complex Results

When the result has many fields, or the fields vary depending on the input, a dictionary is a flexible alternative:

```python
def analyze_text(text):
    words = text.split()
    return {
        "word_count": len(words),
        "char_count": len(text),
        "unique_words": len(set(words)),
        "average_word_length": sum(len(w) for w in words) / len(words),
    }

stats = analyze_text("the quick brown fox jumps over the lazy dog")
print(stats["word_count"])          # 9
print(stats["unique_words"])        # 8
print(stats["average_word_length"]) # 3.888...
```

### When to Use Each Approach

| Approach | Best for | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Plain tuple | 2-3 related values | Simple, lightweight | Positional --- easy to confuse order |
| Named tuple | Fixed set of fields | Named access, still a tuple | Cannot add fields dynamically |
| Dictionary | Variable/many fields | Flexible, self-documenting keys | No attribute access, no type safety |
| Dataclass | Complex structured data | Type hints, methods, defaults | Heavier than named tuple |

## Common Patterns

### Returning a Value and a Status

```python
def parse_int(text):
    try:
        return int(text), True
    except ValueError:
        return 0, False

value, ok = parse_int("42")
if ok:
    print(f"Parsed: {value}")  # Parsed: 42

value, ok = parse_int("abc")
if ok:
    print(f"Parsed: {value}")
else:
    print("Parse failed")  # Parse failed
```

### Returning Updated State

```python
def next_fibonacci(a, b):
    return b, a + b

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = next_fibonacci(a, b)
# 0 1 1 2 3 5 8 13 21 34
```

The function returns the new state as a tuple, and the caller unpacks it back into the state variables.

### Returning Results with Metadata

```python
import time

def timed_sort(items):
    start = time.time()
    result = sorted(items)
    elapsed = time.time() - start
    return result, elapsed

sorted_data, duration = timed_sort(list(range(100000, 0, -1)))
print(f"Sorted {len(sorted_data)} items in {duration:.4f} seconds")
```

---

## Exercises

**Exercise 1.**
Write a function `statistics(numbers)` that returns the minimum, maximum, mean, and range (max - min) of a list of numbers. Use tuple packing for the return value. Then write caller code that uses tuple unpacking to capture each value.

Next, rewrite the function to return a named tuple instead. What advantage does the named tuple version have when the function is called in a large codebase?

??? success "Solution to Exercise 1"
    **Tuple version:**

    ```python
    def statistics(numbers):
        lo = min(numbers)
        hi = max(numbers)
        mean = sum(numbers) / len(numbers)
        rng = hi - lo
        return lo, hi, mean, rng

    lo, hi, mean, rng = statistics([4, 8, 15, 16, 23, 42])
    print(f"Min: {lo}, Max: {hi}, Mean: {mean:.1f}, Range: {rng}")
    # Min: 4, Max: 42, Mean: 18.0, Range: 38
    ```

    **Named tuple version:**

    ```python
    from typing import NamedTuple

    class Stats(NamedTuple):
        minimum: float
        maximum: float
        mean: float
        range: float

    def statistics(numbers):
        lo = min(numbers)
        hi = max(numbers)
        mean = sum(numbers) / len(numbers)
        rng = hi - lo
        return Stats(minimum=lo, maximum=hi, mean=mean, range=rng)

    result = statistics([4, 8, 15, 16, 23, 42])
    print(f"Min: {result.minimum}, Max: {result.maximum}")
    print(f"Mean: {result.mean:.1f}, Range: {result.range}")
    ```

    In a large codebase, the named tuple version has two major advantages:

    1. **Readability**: `result.mean` is self-documenting. With a plain tuple, `result[2]` tells you nothing about what the value represents, and positional unpacking like `lo, hi, mean, rng = statistics(...)` requires the caller to match the exact order.
    2. **Maintainability**: If you later add a fifth field (e.g., `median`), callers using named access (`result.mean`) are unaffected. Callers using positional unpacking must update every call site.

---

**Exercise 2.**
Consider the following function that returns a value and an error indicator:

```python
def safe_sqrt(x):
    if x < 0:
        return None, "Cannot compute square root of negative number"
    import math
    return math.sqrt(x), None
```

Write caller code that handles both the success and error cases. Then discuss: what are the trade-offs between this "return a pair" pattern and raising an exception? In what situations might you prefer one over the other?

??? success "Solution to Exercise 2"
    ```python
    def safe_sqrt(x):
        if x < 0:
            return None, "Cannot compute square root of negative number"
        import math
        return math.sqrt(x), None

    # Caller code
    value, error = safe_sqrt(25)
    if error is None:
        print(f"sqrt(25) = {value}")  # sqrt(25) = 5.0
    else:
        print(f"Error: {error}")

    value, error = safe_sqrt(-4)
    if error is None:
        print(f"sqrt(-4) = {value}")
    else:
        print(f"Error: {error}")  # Error: Cannot compute square root of negative number
    ```

    **Trade-offs:**

    | Aspect | Return pair (`value, error`) | Exception (`raise ValueError`) |
    | --- | --- | --- |
    | Caller obligation | Must check error on every call | Can ignore if propagation is acceptable |
    | Forgetting to handle | Leads to using `None` as a real value (silent bug) | Leads to unhandled exception (loud failure) |
    | Control flow | Linear --- caller checks after each call | Non-linear --- jumps to `except` block |
    | Composability | Harder to chain (must check between calls) | Easier to chain (wrap entire block in `try`) |

    **Prefer return pairs when:**

    - Errors are expected and common (e.g., parsing user input).
    - You want the caller to explicitly handle every case.
    - You are in a context where exceptions are expensive or discouraged.

    **Prefer exceptions when:**

    - Errors are exceptional (rare, unexpected).
    - You want the error to propagate automatically if unhandled.
    - You want clean, chainable code without checks between every call.

---

**Exercise 3.**
Write a function `parse_name(full_name)` that takes a string like `"Alice Marie Johnson"` and returns a dictionary with keys `"first"`, `"middle"`, and `"last"`. If the name has only two parts, the `"middle"` key should be `None`. If the name has one part, both `"middle"` and `"last"` should be `None`.

Then rewrite the function to return a named tuple instead. Discuss which approach is more appropriate for this use case.

??? success "Solution to Exercise 3"
    **Dictionary version:**

    ```python
    def parse_name(full_name):
        parts = full_name.split()
        if len(parts) == 1:
            return {"first": parts[0], "middle": None, "last": None}
        elif len(parts) == 2:
            return {"first": parts[0], "middle": None, "last": parts[1]}
        else:
            return {"first": parts[0], "middle": " ".join(parts[1:-1]), "last": parts[-1]}

    print(parse_name("Alice Marie Johnson"))
    # {'first': 'Alice', 'middle': 'Marie', 'last': 'Johnson'}

    print(parse_name("Alice Johnson"))
    # {'first': 'Alice', 'middle': None, 'last': 'Johnson'}

    print(parse_name("Alice"))
    # {'first': 'Alice', 'middle': None, 'last': None}

    print(parse_name("Alice Marie Grace Johnson"))
    # {'first': 'Alice', 'middle': 'Marie Grace', 'last': 'Johnson'}
    ```

    **Named tuple version:**

    ```python
    from typing import NamedTuple, Optional

    class Name(NamedTuple):
        first: str
        middle: Optional[str]
        last: Optional[str]

    def parse_name(full_name):
        parts = full_name.split()
        if len(parts) == 1:
            return Name(first=parts[0], middle=None, last=None)
        elif len(parts) == 2:
            return Name(first=parts[0], middle=None, last=parts[1])
        else:
            return Name(first=parts[0], middle=" ".join(parts[1:-1]), last=parts[-1])

    result = parse_name("Alice Marie Johnson")
    print(result.first)   # Alice
    print(result.middle)  # Marie
    print(result.last)    # Johnson
    ```

    **Which is more appropriate?**

    The named tuple is better for this use case because:

    - The fields are **fixed** (first, middle, last) and always present.
    - The caller benefits from **attribute access** (`result.first` vs `result["first"]`).
    - Named tuples are **immutable**, which is appropriate since a parsed name should not change.
    - Named tuples support both positional and named unpacking.

    Dictionaries would be more appropriate if the set of fields were variable (e.g., some names include titles, suffixes, or other optional components that differ from case to case).
