
# Comprehensions

A **comprehension** is a compact way to build a new collection from an iterable.

Python supports comprehensions for:

- lists — `[expr for x in iterable]`
- sets — `{expr for x in iterable}`
- dictionaries — `{key: value for x in iterable}`
- generator expressions — `(expr for x in iterable)`
- tuples — no comprehension syntax; use `tuple(expr for x in iterable)` instead

They provide a concise alternative to loops. In each case, the pattern is the same: apply an expression to each element and optionally filter with a condition.

---

## 1. List Comprehensions

A list comprehension creates a list.

```python
squares = [x * x for x in range(5)]
print(squares)
```

Output:

```text
[0, 1, 4, 9, 16]
```

The equivalent loop:

```python
squares = []
for x in range(5):
    squares.append(x * x)
```

Throughout this page, the loop equivalent is shown only for list comprehensions. The same expansion applies to set, dict, and generator forms.

---

## 2. Filtering in Comprehensions

A condition at the end filters which elements are included.

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

Output:

```text
[0, 2, 4, 6, 8]
```

### Ternary expression vs filter

The `if` at the end *filters*. An `if`/`else` in the expression *transforms*.

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)
```

Output:

```text
['even', 'odd', 'even', 'odd', 'even']
```

Note the position: `if`/`else` before `for` transforms every element; `if` after `for` selects which elements to include.

---

## 3. Set Comprehensions

A set comprehension creates a set. Duplicates are removed automatically.

```python
lengths = {len(word) for word in ["cat", "dog", "elephant", "ant"]}
print(lengths)
```

Output:

```text
{3, 8}
```

`"cat"`, `"dog"`, and `"ant"` all have length 3 — the set keeps only one.

---

## 4. Dictionary Comprehensions

A dictionary comprehension creates a mapping.

```python
squares = {x: x * x for x in range(5)}
print(squares)
```

Output:

```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 5. Generator Expressions

A similar syntax with parentheses creates a **generator expression** — a lazy sequence that computes values on demand rather than building the full collection in memory.

```python
total = sum(x * x for x in range(5))
print(total)
```

Output:

```text
30
```

When passed directly as a function argument, the outer parentheses of the generator expression are shared with the function call. Generators are preferred over list comprehensions when the full list is not needed.

There is no tuple comprehension syntax. Parentheses create a generator expression,
not a tuple. To build a tuple from a comprehension-like expression, wrap explicitly:

```python
squares_tuple = tuple(x * x for x in range(5))
print(squares_tuple)
print(type(squares_tuple))
```

Output:
```text
(0, 1, 4, 9, 16)
<class 'tuple'>
```

This is a deliberate Python design choice. Tuples represent fixed-size records — a
coordinate `(x, y)`, a person `("Alice", 25)`, a return value — where the number of
elements and their positions carry meaning. A comprehension generates an arbitrary
number of values from a transformation, which is conceptually the job of a list, not
a tuple. Python therefore provides no tuple comprehension syntax, making the
distinction explicit: if you are generating a collection of uniform values, you
probably want a list; if you happen to need a tuple for a specific API or performance
reason, wrap a generator explicitly with `tuple()`.

---

## 6. Nested Comprehensions

Comprehensions can iterate over multiple sequences.

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

The order reads left to right: the outer `for` comes first, then the inner `for`.

---

## 7. When to Use Comprehensions

A comprehension that fits comfortably on one line is usually appropriate. Once it requires a nested loop with a condition, consider a regular loop instead.

```python
# this comprehension is too complex — use a loop
result = [f(x, y) for x in range(10) for y in range(10) if x != y and g(x, y)]
```

Comprehensions are generally preferred over `map()` and `filter()` in modern Python for readability.

---

## 8. Worked Examples

### Example 1: uppercase words

```python
words = ["python", "is", "fun"]
upper_words = [w.upper() for w in words]
print(upper_words)
```

Output:

```text
['PYTHON', 'IS', 'FUN']
```

### Example 2: positive numbers only

```python
nums = [-2, -1, 0, 1, 2]
positive = [x for x in nums if x > 0]
print(positive)
```

Output:

```text
[1, 2]
```

### Example 3: word lengths

```python
length_map = {word: len(word) for word in ["cat", "horse"]}
print(length_map)
```

Output:

```text
{'cat': 3, 'horse': 5}
```

---

## 9. Common Pitfalls

### Making comprehensions too complex

Readability matters more than compactness. If a comprehension is hard to read, use a loop.

### Confusing set and dictionary comprehension syntax

Braces create either a set or a dictionary depending on the presence of `:`.

```python
a = {x for x in range(3)}
b = {x: x for x in range(3)}

print(a)
print(b)
```

Output:

```text
{0, 1, 2}
{0: 0, 1: 1, 2: 2}
```

### Expecting comprehension variables to leak

In Python 3, comprehension variables do not leak into the enclosing scope. This is different from regular `for` loops.

```python
squares = [x for x in range(5)]
# x is not defined here — unlike a regular for loop
```

---

## 10. Summary

Key ideas:

- comprehensions create collections concisely
- list, set, dictionary, and generator forms all follow the same pattern
- filtering with `if` selects elements; `if`/`else` in the expression transforms elements
- generator expressions are lazy and memory-efficient
- keep comprehensions simple — use a loop when they become hard to read

Comprehensions are one of Python's most expressive tools for transforming data. They build on [Lists](lists.md), [Sets](sets.md), and [Dictionaries](dictionaries.md) covered earlier in this section. For deeper coverage of how these collections work internally, see [Hashing and Hash Tables](../../ch02/composites/hashing_deep_dive.md).
