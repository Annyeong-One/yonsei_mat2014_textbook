# Walrus Operator

## Assignment Expression

### 1. Syntax

```python
# := assigns AND returns value
if (n := len(data)) > 10:
    print(f"Long list: {n} items")
```

### 2. Use in Conditions

```python
# Before
data = input()
if len(data) > 5:
    print(f"Long: {len(data)}")

# After
if (n := len(data)) > 5:
    print(f"Long: {n}")
```

## Common Patterns

### 1. While Loops

```python
# Read until empty
while (line := input()) != "":
    process(line)
```

### 2. List Comprehensions

```python
# Reuse computed value
[y for x in data if (y := f(x)) > 0]
```

### 3. If-Elif

```python
if (match := pattern1.search(text)):
    handle(match)
elif (match := pattern2.search(text)):
    handle(match)
```

## Summary

- Syntax: `(name := expr)`
- Assigns and returns value
- Use in conditions
- Available Python 3.8+
