
# str Split, Join, and Modify

Strings often need to be broken apart, recombined, or cleaned up.

This section covers:

- `split()`
- `join()`
- common modification methods

```mermaid
flowchart LR
    A[String] --> B[split()]
    C[List of strings] --> D[join()]
    A --> E[strip/replace methods]
````

---

## 1. split()

`split()` breaks a string into parts.

```python
text = "red green blue"
parts = text.split()

print(parts)
```

Output:

```text
['red', 'green', 'blue']
```

A separator can also be specified.

```python
data = "a,b,c"
print(data.split(","))
```

Output:

```text
['a', 'b', 'c']
```

---

## 2. join()

`join()` combines a sequence of strings into one string.

```python
words = ["red", "green", "blue"]
result = " ".join(words)

print(result)
```

Output:

```text
red green blue
```

The separator is the string before `.join()`.

```python
print("-".join(words))
```

Output:

```text
red-green-blue
```

---

## 3. strip()

`strip()` removes leading and trailing whitespace.

```python
text = "   hello   "
print(text.strip())
```

You can also use:

* `lstrip()`
* `rstrip()`

---

## 4. replace()

`replace()` substitutes one substring with another.

```python
text = "I like cats"
print(text.replace("cats", "dogs"))
```

Output:

```text
I like dogs
```

---

## 5. Worked Examples

### Example 1: parse CSV-like input

```python
line = "Alice,Bob,Charlie"
names = line.split(",")
print(names)
```

### Example 2: rebuild sentence

```python
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)
```

### Example 3: clean input

```python
raw = "   data   "
clean = raw.strip()
print(clean)
```

---

## 6. Common Pitfalls

### Joining non-strings

`join()` requires strings.

```python
# ",".join([1, 2, 3])   # TypeError
```

Convert first if necessary.

### Expecting `split()` to preserve exact formatting

Whitespace splitting collapses runs of spaces when no separator is specified.

---

## 7. Summary

Key ideas:

* `split()` breaks strings into lists
* `join()` combines lists of strings into one string
* `strip()` removes outer whitespace
* `replace()` substitutes text

These methods are central to practical string processing.