
# The Transform Pattern

Think of a factory assembly line: raw materials enter one end and finished products come out the other. Nothing is discarded or selected---every input produces exactly one output. The **transform pattern** works the same way. You start with a collection, apply a function to each element, and produce a new collection of the same length with each element replaced by its transformed version.

This is one of the most common data flow patterns in programming. Whenever you need to convert, format, extract, or reshape every item in a collection, you are applying the transform pattern.

## Mental Model

The key insight is a one-to-one mapping. If you have 10 inputs, you get exactly 10 outputs. The original collection is untouched; a brand-new collection holds the results. This separation between input and output makes transform operations predictable and easy to reason about.

```
input:  [a,    b,    c,    d   ]
         |     |     |     |
         f     f     f     f
         |     |     |     |
output: [f(a), f(b), f(c), f(d)]
```

## List Comprehension

The most Pythonic way to express a transform is a list comprehension. The syntax `[f(x) for x in data]` reads almost like English: "apply f to x for every x in data."

```python
celsius = [0, 20, 37, 100]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]

print(fahrenheit)  # [32.0, 68.0, 98.6, 212.0]
```

The comprehension creates a new list. The original `celsius` list is unchanged.

### Formatting Strings

Transform is not limited to numbers. You can reshape any kind of data.

```python
names = ["alice", "bob", "charlie"]
formatted = [name.capitalize() for name in names]

print(formatted)  # ['Alice', 'Bob', 'Charlie']
```

### Extracting Fields

When working with structured data such as dictionaries, transform lets you pull out specific fields.

```python
records = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

names = [r["name"] for r in records]
print(names)  # ['Alice', 'Bob', 'Charlie']
```

## The map() Function

Python also provides the built-in `map()` function. It takes a function and an iterable and returns a "lazy" iterator of transformed values.

```python
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))

print(fahrenheit)  # [32.0, 68.0, 98.6, 212.0]
```

`map()` returns an iterator, not a list. Wrap it in `list()` when you need all results at once.

### Using Named Functions with map()

When you already have a named function, `map()` can be cleaner than a comprehension.

```python
def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))

print(squared)  # [1, 4, 9, 16, 25]
```

## Building Transformed Lists with a Loop

Before comprehensions existed, the standard approach was an explicit loop with `append()`. This is still useful when the transformation logic is complex enough that a comprehension becomes hard to read.

```python
prices_usd = [10.0, 25.5, 3.99, 47.0]
exchange_rate = 1350.0

prices_krw = []
for price in prices_usd:
    converted = round(price * exchange_rate)
    prices_krw.append(converted)

print(prices_krw)  # [13500, 34425, 5387, 63450]
```

The pattern is always the same: create an empty list, iterate over the source, append the transformed value.

## Choosing Between Approaches

| Approach | Best when |
|---|---|
| List comprehension | Transformation fits in a single expression |
| `map()` | You already have a named function to apply |
| Explicit loop | Logic is multi-step or involves side effects |

All three produce the same result. The choice is about readability.

## Multi-Step Transforms

Transforms can be chained. Each step takes the output of the previous step as input.

```python
raw = ["  Alice  ", "  BOB", "charlie  "]

cleaned = [name.strip() for name in raw]
lowered = [name.lower() for name in cleaned]
titled = [name.title() for name in lowered]

print(titled)  # ['Alice', 'Bob', 'Charlie']
```

You can also collapse multiple steps into a single comprehension when each step is simple.

```python
titled = [name.strip().lower().title() for name in raw]
print(titled)  # ['Alice', 'Bob', 'Charlie']
```

---

## Exercises

**Exercise 1.**
You have a list of file names and need to extract just the extensions. Predict the output:

```python
files = ["report.pdf", "data.csv", "image.png", "notes.txt"]
extensions = [f.split(".")[-1] for f in files]
print(extensions)

upper_ext = list(map(str.upper, extensions))
print(upper_ext)
```

What would happen if one of the file names had no dot, like `"README"`? How would you guard against that case?

??? success "Solution to Exercise 1"
    Output:

    ```text
    ['pdf', 'csv', 'png', 'txt']
    ['PDF', 'CSV', 'PNG', 'TXT']
    ```

    The comprehension splits each file name on `"."` and takes the last piece. `map(str.upper, extensions)` applies the `upper` method to each extension string.

    If a file name has no dot, `"README".split(".")` returns `["README"]`, so `[-1]` gives `"README"` itself---the whole name is treated as the extension. To guard against this, you could check for the presence of a dot:

    ```python
    extensions = [f.split(".")[-1] if "." in f else "" for f in files]
    ```

    Alternatively, use `os.path.splitext()` which returns `("README", "")` for dotless names.

---

**Exercise 2.**
Write a function `apply_discount` that takes a list of prices and a discount percentage, and returns a new list with the discount applied. Use a list comprehension.

```python
def apply_discount(prices, discount_pct):
    # your code here
    pass

original = [100.0, 49.99, 250.0, 15.50]
sale = apply_discount(original, 20)
print(sale)
print(original)  # should be unchanged
```

What should the output look like? Verify that the original list is not modified.

??? success "Solution to Exercise 2"
    ```python
    def apply_discount(prices, discount_pct):
        factor = 1 - discount_pct / 100
        return [round(p * factor, 2) for p in prices]

    original = [100.0, 49.99, 250.0, 15.50]
    sale = apply_discount(original, 20)
    print(sale)
    print(original)
    ```

    Output:

    ```text
    [80.0, 39.99, 200.0, 12.4]
    [100.0, 49.99, 250.0, 15.5]
    ```

    The comprehension creates a new list. Each price is multiplied by `0.8` (a 20% discount). `round(..., 2)` keeps the result to two decimal places. The original list remains untouched because the comprehension never modifies it---it builds a fresh list from scratch.

---

**Exercise 3.**
Consider two approaches to the same transform. Predict the output of both and explain when you would prefer one over the other.

```python
# Approach A: list comprehension
data = [3, 1, 4, 1, 5, 9]
result_a = [x ** 2 + 1 for x in data]
print(result_a)

# Approach B: map with lambda
result_b = list(map(lambda x: x ** 2 + 1, data))
print(result_b)

print(result_a == result_b)
```

In what situation would `map()` be clearly preferable to a list comprehension?

??? success "Solution to Exercise 3"
    Output:

    ```text
    [10, 2, 17, 2, 26, 82]
    [10, 2, 17, 2, 26, 82]
    True
    ```

    Both approaches produce identical results. The comprehension is generally preferred when you have an inline expression because `[x ** 2 + 1 for x in data]` reads more naturally than wrapping the same expression in a `lambda`.

    `map()` becomes clearly preferable when you already have a named function to apply, such as `map(int, strings)` or `map(str.strip, lines)`. In those cases `map()` is shorter and avoids creating a throwaway `lambda` or comprehension variable. The rule of thumb: if a callable already exists, use `map()`; if you need to write a `lambda`, prefer a comprehension.
