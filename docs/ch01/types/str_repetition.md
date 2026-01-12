# `str`: Repetition

The `*` operator repeats a string a specified number of times.

---

## Basic Syntax

### 1. Repeat String

```python
def main():
    print('-' * 50)
    print(50 * '-')  # Order doesn't matter

if __name__ == "__main__":
    main()
```

Output:
```
--------------------------------------------------
--------------------------------------------------
```

### 2. Word Repetition

```python
print("Ha" * 3)   # HaHaHa
print(3 * "Ha")   # HaHaHa
```

---

## Edge Cases

### 1. Zero Multiplier

Multiplying by zero produces empty string:

```python
def main():
    print(0 * 'Jaspreet')  # (empty string)

if __name__ == "__main__":
    main()
```

### 2. Negative Multiplier

Negative values also produce empty string:

```python
def main():
    print(-4 * 'Jaspreet')  # (empty string)

if __name__ == "__main__":
    main()
```

---

## Practical Uses

### 1. Separators

```python
def main():
    print("=" * 40)
    print("Title")
    print("=" * 40)

if __name__ == "__main__":
    main()
```

### 2. Indentation

```python
level = 3
indent = "  " * level
print(indent + "Nested item")  #       Nested item
```

### 3. Padding

```python
width = 20
char = "-"
print(char * width)  # --------------------
```

---

## Key Takeaways

- `*` repeats strings: `"ab" * 3` → `"ababab"`.
- Zero or negative multiplier yields empty string.
- Useful for separators and formatting.
