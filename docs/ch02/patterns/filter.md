
# The Filter Pattern

Imagine sorting mail: you look at each envelope and decide whether it goes into the "keep" pile or the "discard" pile. The **filter pattern** works the same way. You walk through a collection, test each element against a condition, and produce a new collection containing only the elements that passed. Unlike the transform pattern, the output can be shorter than the input---elements are either kept or dropped, never changed.

## Mental Model

Every element faces a yes-or-no question. If the answer is yes (the predicate returns `True`), the element is included in the output. If the answer is no, it is silently skipped.

```
input:  [a,  b,  c,  d,  e ]
         |   |   |   |   |
         T   F   T   T   F    <-- predicate
         |       |   |
output: [a,  c,  d ]
```

The output is always a subsequence of the input: same order, same values, but potentially fewer items.

## List Comprehension with if

The most common way to filter in Python is a list comprehension with an `if` clause.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]

print(evens)  # [2, 4, 6, 8, 10]
```

The `if` clause acts as a gatekeeper: only elements where `n % 2 == 0` evaluates to `True` make it into the new list.

### Selecting Valid Records

Filtering is essential when working with real-world data that may contain incomplete entries.

```python
records = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": ""},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "Diana", "email": None},
]

valid = [r for r in records if r["email"]]
print(valid)
# [{'name': 'Alice', 'email': 'alice@example.com'},
#  {'name': 'Charlie', 'email': 'charlie@example.com'}]
```

Both the empty string `""` and `None` are falsy, so the condition `r["email"]` excludes both.

### Removing None Values

A very common filtering task is cleaning `None` values out of a collection.

```python
data = [1, None, 3, None, 5, None, 7]
cleaned = [x for x in data if x is not None]

print(cleaned)  # [1, 3, 5, 7]
```

Use `is not None` rather than a bare truthiness check when you want to keep falsy values like `0` or `""`.

```python
data = [0, None, "", False, 42]
# Truthiness check removes 0, "", and False too
truthy_only = [x for x in data if x]
print(truthy_only)  # [42]

# None check removes only None
no_none = [x for x in data if x is not None]
print(no_none)  # [0, '', False, 42]
```

## The filter() Function

Python provides a built-in `filter()` function that takes a predicate function and an iterable.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, numbers))

print(evens)  # [2, 4, 6, 8, 10]
```

Like `map()`, `filter()` returns a lazy iterator. Wrap it in `list()` when you need the full result.

### filter with None as Predicate

Passing `None` as the first argument to `filter()` removes all falsy values.

```python
data = [0, 1, "", "hello", None, [], [1, 2]]
cleaned = list(filter(None, data))

print(cleaned)  # [1, 'hello', [1, 2]]
```

This is a compact idiom, but be aware that it removes `0`, `""`, and empty containers along with `None`.

## Common Filtering Idioms

### Filtering by Type

```python
mixed = [1, "two", 3.0, "four", 5]
strings_only = [x for x in mixed if isinstance(x, str)]

print(strings_only)  # ['two', 'four']
```

### Filtering with Multiple Conditions

Combine conditions using `and` or `or` inside the `if` clause.

```python
students = [
    {"name": "Alice", "grade": 92, "active": True},
    {"name": "Bob", "grade": 67, "active": True},
    {"name": "Charlie", "grade": 85, "active": False},
    {"name": "Diana", "grade": 78, "active": True},
]

honor_roll = [
    s["name"] for s in students
    if s["grade"] >= 80 and s["active"]
]

print(honor_roll)  # ['Alice', 'Diana']
```

Note that this combines filtering (the `if` clause) with transformation (extracting just the name). This is a filter-then-transform pattern expressed in a single comprehension.

### Filtering with a Set for Fast Lookup

When checking membership against a large collection, convert it to a set first.

```python
allowed_ids = {101, 205, 308, 412}
requests = [101, 999, 205, 777, 308]

valid_requests = [r for r in requests if r in allowed_ids]
print(valid_requests)  # [101, 205, 308]
```

Set membership testing is O(1) on average, compared to O(n) for lists.

## Choosing Between Approaches

| Approach | Best when |
|---|---|
| List comprehension with `if` | Condition fits in a single expression |
| `filter()` | You already have a named predicate function |
| Explicit loop | Logic is complex or has side effects |

As with transforms, the choice is about clarity. Comprehensions are idiomatic Python for most filtering tasks.

---

## Exercises

**Exercise 1.**
Predict the output of each filtering operation and explain the difference.

```python
values = [0, 1, 2, "", "hello", None, False, True, [], [1]]

truthy = [v for v in values if v]
print(truthy)

not_none = [v for v in values if v is not None]
print(not_none)

print(len(truthy), len(not_none))
```

Why do the two approaches produce different results? When would you choose one over the other?

??? success "Solution to Exercise 1"
    Output:

    ```text
    [1, 2, 'hello', True, [1]]
    [0, 1, 2, '', 'hello', False, True, [], [1]]
    5 9
    ```

    The truthiness check (`if v`) removes every falsy value: `0`, `""`, `None`, `False`, and `[]`. The `is not None` check removes only `None`, keeping all other values including falsy ones like `0`, `""`, `False`, and `[]`.

    Use truthiness filtering when you want to strip out all "empty" or "zero-like" values. Use `is not None` when you specifically need to remove missing/unset values but want to preserve legitimate falsy data like `0` or empty strings. In data processing, `is not None` is usually the safer choice because `0` and `""` are often valid data.

---

**Exercise 2.**
Write a function `filter_by_range` that takes a list of numbers, a minimum, and a maximum, and returns only the numbers within that range (inclusive on both ends).

```python
def filter_by_range(numbers, low, high):
    # your code here
    pass

data = [15, 3, 42, 8, 27, 1, 36, 19]
result = filter_by_range(data, 10, 30)
print(result)
print(data)  # should be unchanged
```

What is the expected output? What happens if `low` is greater than `high`?

??? success "Solution to Exercise 2"
    ```python
    def filter_by_range(numbers, low, high):
        return [n for n in numbers if low <= n <= high]

    data = [15, 3, 42, 8, 27, 1, 36, 19]
    result = filter_by_range(data, 10, 30)
    print(result)
    print(data)
    ```

    Output:

    ```text
    [15, 27, 19]
    [15, 3, 42, 8, 27, 1, 36, 19]
    ```

    Python's chained comparison `low <= n <= high` is both readable and efficient. The original list is not modified because the comprehension builds a new list.

    If `low > high`, the condition `low <= n <= high` can never be `True`, so the function returns an empty list `[]`. You could add a guard at the top of the function to handle this explicitly:

    ```python
    def filter_by_range(numbers, low, high):
        if low > high:
            return []
        return [n for n in numbers if low <= n <= high]
    ```

---

**Exercise 3.**
Consider this code that combines filtering and transformation. Predict the output and then rewrite it using `filter()` and `map()` separately.

```python
words = ["hello", "", "world", " ", "python", "", "code"]
result = [w.upper() for w in words if w.strip()]
print(result)
```

Why does `" "` (a single space) get filtered out even though it is not an empty string?

??? success "Solution to Exercise 3"
    Output:

    ```text
    ['HELLO', 'WORLD', 'PYTHON', 'CODE']
    ```

    The condition `w.strip()` removes leading and trailing whitespace from `w` and then tests the result for truthiness. `" ".strip()` produces `""`, which is falsy, so the space-only string is excluded. Empty strings `""` are also falsy after stripping (they are already empty).

    Rewritten using `filter()` and `map()`:

    ```python
    words = ["hello", "", "world", " ", "python", "", "code"]

    non_blank = filter(lambda w: w.strip(), words)
    result = list(map(str.upper, non_blank))
    print(result)  # ['HELLO', 'WORLD', 'PYTHON', 'CODE']
    ```

    The `filter()` step removes blank/empty strings, and the `map()` step transforms the survivors to uppercase. The comprehension version is more concise because it combines both steps, but the two-step version makes the separate concerns (filtering and transforming) explicit.
