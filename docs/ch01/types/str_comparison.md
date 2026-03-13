
# str Comparison

Strings can be compared for equality and ordering.

Python compares strings **lexicographically**, character by character.

This is similar to dictionary ordering, but it is based on Unicode code points.

```mermaid2
flowchart LR
    A[String A] --> C[character-by-character comparison]
    B[String B] --> C
    C --> D[Boolean result]
````

---

## 1. Equality Comparison

Two strings are equal if they contain exactly the same characters in the same order.

```python
print("cat" == "cat")
print("cat" == "Cat")
```

Output:

```text
True
False
```

String comparison is case-sensitive.

---

## 2. Inequality Comparison

```python
print("cat" != "dog")
```

Output:

```text
True
```

---

## 3. Ordering Comparison

Strings can be ordered with `<`, `>`, `<=`, and `>=`.

```python
print("apple" < "banana")
print("cat" > "car")
```

Output:

```text
True
True
```

Comparison proceeds from left to right until a differing character is found.

---

## 4. Case Matters

Uppercase and lowercase letters have different Unicode values.

```python
print("Z" < "a")
```

This may produce a result that surprises beginners.

For user-facing comparisons, normalization is often needed.

```python
print("Cat".lower() == "cat".lower())
```

Output:

```text
True
```

---

## 5. Prefix Effects

Shorter strings can be smaller when one is a prefix of the other.

```python
print("app" < "apple")
```

Output:

```text
True
```

---

## 6. Worked Examples

### Example 1: exact password check

```python
password = "secret"
print(password == "secret")
```

### Example 2: alphabetical order

```python
print("ant" < "bat")
```

### Example 3: case-insensitive comparison

```python
a = "Python"
b = "python"

print(a.lower() == b.lower())
```

---

## 7. Common Pitfalls

### Assuming comparisons ignore case

They do not unless you normalize explicitly.

### Confusing human alphabetical order with Unicode order

Unicode-based comparison is precise, but not always what human sorting expects.

---

## 8. Summary

Key ideas:

* strings support equality and ordering comparisons
* comparisons are lexicographic
* case affects comparison results
* normalization is often needed for user-oriented comparisons

String comparison is essential in searching, sorting, validation, and conditional logic.