

# Built-in Usage Examples

This section demonstrates how multiple built-ins combine in real programs.

---

## Example: Average Calculator

```python
numbers = [10,20,30]

avg = sum(numbers)/len(numbers)

print(avg)
````

---

## Example: Zipping Data

```python
names = ["Alice","Bob"]
scores = [90,85]

for name,score in zip(names,scores):
    print(name,score)
```

---

## Example: Filtering Data

```python
values = [0,1,2,3]

print(any(values))
print(all(values))
```

---

## Example: Sorting

```python
numbers = [3,1,4,2]

print(sorted(numbers))
```

## Exercises

**Exercise 1.**
Predict the output of each line, then verify by running the code.

```python
data = [4, 7, 2, 9, 1]
print(min(data), max(data), sum(data))
print(sum(data) / len(data))
print(sorted(data, reverse=True))
```

??? success "Solution to Exercise 1"
    ```
    1 9 23
    4.6
    [9, 7, 4, 2, 1]
    ```

    `min(data)` returns `1`, `max(data)` returns `9`, and `sum(data)` returns `23`. The average is `23 / 5 = 4.6`. `sorted(data, reverse=True)` returns a new list in descending order.

---

**Exercise 2.**
Using `zip` and `sum`, write a one-line expression that computes the dot product of two lists `a = [1, 2, 3]` and `b = [4, 5, 6]`. The dot product is $1 \times 4 + 2 \times 5 + 3 \times 6 = 32$.

??? success "Solution to Exercise 2"
    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    dot = sum(x * y for x, y in zip(a, b))
    print(dot)
    ```

    Output:

    ```
    32
    ```

    `zip(a, b)` pairs corresponding elements: `(1, 4)`, `(2, 5)`, `(3, 6)`. The generator expression multiplies each pair and `sum` adds the products: `4 + 10 + 18 = 32`.

---

**Exercise 3.**
Given the list `values = [0, "", None, 42, "hello", [], True]`, predict the output of `any(values)` and `all(values)`. Explain your reasoning.

??? success "Solution to Exercise 3"
    ```python
    values = [0, "", None, 42, "hello", [], True]
    print(any(values))  # True
    print(all(values))  # False
    ```

    `any(values)` returns `True` because at least one element is truthy (`42`, `"hello"`, and `True` are all truthy).

    `all(values)` returns `False` because several elements are falsy: `0`, `""`, `None`, and `[]` are all falsy in Python. `all` requires every element to be truthy.

---

**Exercise 4.**
Write a program that uses `enumerate` and `zip` together. Given `names = ["Alice", "Bob", "Carol"]` and `scores = [88, 95, 72]`, print each student's rank (starting from 1), name, and score in the format: `1. Alice - 88`.

??? success "Solution to Exercise 4"
    ```python
    names = ["Alice", "Bob", "Carol"]
    scores = [88, 95, 72]

    for i, (name, score) in enumerate(zip(names, scores), start=1):
        print(f"{i}. {name} - {score}")
    ```

    Output:

    ```
    1. Alice - 88
    2. Bob - 95
    3. Carol - 72
    ```

    `zip(names, scores)` pairs each name with its score. `enumerate(..., start=1)` adds a 1-based index. The unpacking `i, (name, score)` extracts the index and the tuple from each iteration.

---

**Exercise 5.**
Explain why `sum(range(1, 101))` returns `5050`. Relate this to a well-known mathematical formula.

??? success "Solution to Exercise 5"
    `range(1, 101)` generates the integers from 1 to 100 inclusive. `sum` adds them all together.

    The result is given by the formula for the sum of the first $n$ natural numbers:

    $$
    \sum_{k=1}^{n} k = \frac{n(n+1)}{2}
    $$

    For $n = 100$:

    $$
    \frac{100 \times 101}{2} = 5050
    $$

    This is the formula famously attributed to Gauss. Python computes the same result by iterating through all 100 values and accumulating their sum.
