# `str`: Concatenation

The `+` operator joins strings together to create a new string.

---

## Plus Operator

### 1. Basic Joining

```python
def main():
    print('Hello' + 'Bob')  # HelloBob

if __name__ == "__main__":
    main()
```

### 2. With Space

```python
string = "Hello"
new_string = string + " World"

print("Original:", string)      # Hello
print("Modified:", new_string)  # Hello World
```

---

## Common Pitfall

### 1. String vs Integer

`"1" + "1"` concatenates, not adds:

```python
def main():
    print("1" + "1")  # 11 (not 2)

if __name__ == "__main__":
    main()
```

### 2. Type Matters

```python
print(1 + 1)      # 2 (integer addition)
print("1" + "1")  # 11 (string concatenation)
```

---

## With Slicing

### 1. Character Replace

Combine slicing and concatenation:

```python
a = "Hello Pi"
a = a[:1] + "E" + a[2:]
print(a)  # HEllo Pi
```

### 2. Insert Text

```python
s = "HelloWorld"
s = s[:5] + " " + s[5:]
print(s)  # Hello World
```

---

## Key Takeaways

- `+` joins strings into a new string.
- String `"1" + "1"` yields `"11"`, not `2`.
- Combine with slicing for insertions.
