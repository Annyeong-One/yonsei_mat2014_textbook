# `str`: Indexing

Python strings support index-based access to individual characters.

---

## Positive Indexing

### 1. Zero-Based Index

Python uses zero-based indexing:

```python
def main():
    a = "Hello Pi"
    #    01234567
    print(a[0])  # H
    print(a[6])  # P
    print(a[7])  # i

if __name__ == "__main__":
    main()
```

### 2. Index Diagram

```
String:  H   e   l   l   o       P   i
Index:   0   1   2   3   4   5   6   7
```

---

## Negative Indexing

### 1. Counting from End

Negative indices count backward from the end:

```python
def main():
    a = "Hello Pi"
    #   -8-7-6-5-4-3-2-1
    print(a[-1])  # i
    print(a[-2])  # P
    print(a[-3])  # (space)

if __name__ == "__main__":
    main()
```

### 2. Index Diagram

```
String:  H   e   l   l   o       P   i
Pos:     0   1   2   3   4   5   6   7
Neg:    -8  -7  -6  -5  -4  -3  -2  -1
```

### 3. Equivalence

Positive and negative indices access the same positions:

```python
a = "Hello Pi"
print(a[0] == a[-8])  # True (both 'H')
print(a[7] == a[-1])  # True (both 'i')
```

---

## Key Takeaways

- Indexing starts at 0 from the left.
- Negative indices start at -1 from the right.
- `a[0]` is first, `a[-1]` is last character.
