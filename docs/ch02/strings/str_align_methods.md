# `str`: Alignment Methods

Python provides string alignment methods that **pad text to a specified width**. These methods are commonly used when formatting:

* tables
* reports
* command-line output
* logs

Alignment methods **do not modify the original string**. Instead, they return a **new padded string**.

```python
s = "Hello"
t = s.ljust(10)

print(s)  # 'Hello'
print(t)  # 'Hello     '
```

---

## Basic Alignment Methods

Python provides three primary alignment methods.

| Method                    | Description      |
| ------------------------- | ---------------- |
| `ljust(width, fillchar)`  | Left-align text  |
| `rjust(width, fillchar)`  | Right-align text |
| `center(width, fillchar)` | Center text      |

If the width is larger than the string length, padding is added.

---

### Left Alignment

`ljust()` pads characters on the **right side**.

```python
s = "Hello"

print(s.ljust(10))       # 'Hello     '
print(s.ljust(10, "-"))  # 'Hello-----'
```

---

### Right Alignment

`rjust()` pads characters on the **left side**.

```python
s = "Hello"

print(s.rjust(10))       # '     Hello'
print(s.rjust(10, "-"))  # '-----Hello'
```

---

### Center Alignment

`center()` pads characters on **both sides**.

```python
s = "Hello"

print(s.center(11))       # '   Hello   '
print(s.center(11, "-"))  # '---Hello---'
```

If padding is uneven, the extra space is placed on the **right side**.

```python
print("Hello".center(10))  # '  Hello   '
```

---

## Width Rules

Alignment methods **never truncate strings**.

If the specified width is smaller than the string length, the original string is returned unchanged.

```python
s = "Hello World"

print(s.ljust(5))   # 'Hello World'
print(s.rjust(5))   # 'Hello World'
print(s.center(5))  # 'Hello World'
```

---

## Zero Padding with `zfill()`

`zfill()` pads a string with leading zeros. It is specialized for **numeric padding**.

```python
s = "42"

print(s.zfill(5))   # '00042'
print(s.zfill(10))  # '0000000042'
```

Unlike `rjust()`, `zfill()` handles numeric signs correctly.

```python
print("-42".zfill(5))  # '-0042'
print("+42".zfill(6))  # '+00042'
```

---

## Practical Examples

### Table Formatting

Alignment methods are useful for formatting columns.

```python
def main():
    data = [
        ("Alice", 95),
        ("Bob", 87),
        ("Carol", 100)
    ]

    for name, score in data:
        print(name.ljust(10) + str(score).rjust(5))

if __name__ == "__main__":
    main()
```

Output:

```
Alice         95
Bob           87
Carol        100
```

---

### File Numbering

Padding ensures consistent filename ordering.

```python
def main():
    files = ["report", "data", "summary"]

    for i, name in enumerate(files, 1):
        filename = f"{str(i).zfill(3)}_{name}.txt"
        print(filename)

if __name__ == "__main__":
    main()
```

Output:

```
001_report.txt
002_data.txt
003_summary.txt
```

---

### Time Formatting

Zero padding is often used when formatting time values.

```python
def main():
    hours, minutes, seconds = 9, 5, 3

    time_str = (
        str(hours).zfill(2) + ":" +
        str(minutes).zfill(2) + ":" +
        str(seconds).zfill(2)
    )

    print(time_str)  # 09:05:03

if __name__ == "__main__":
    main()
```

---

## Alignment vs Format Specifiers

Alignment can also be performed using **format specifiers** in f-strings.

```python
s = "Hi"
width = 10

print(s.ljust(width))    # 'Hi        '
print(s.rjust(width))    # '        Hi'
print(s.center(width))   # '    Hi    '

print(f"{s:<{width}}")   # 'Hi        '
print(f"{s:>{width}}")   # '        Hi'
print(f"{s:^{width}}")   # '    Hi    '
```

Custom fill characters are also supported.

```python
print("Hi".center(10, "*"))  # ****Hi****
print(f"{'Hi':*^10}")        # ****Hi****
```

### When to Use Each

| Approach          | Best Use                            |
| ----------------- | ----------------------------------- |
| Alignment methods | when width is stored in variables   |
| Format specifiers | when formatting output in f-strings |

---

## Key Takeaways

* `ljust()`, `rjust()`, and `center()` align strings within a specified width.
* Alignment methods **return new strings** and never modify the original.
* If the width is smaller than the string length, the string is returned unchanged.
* `zfill()` pads numbers with leading zeros while preserving signs.
* Alignment is commonly used for **tables, filenames, and formatted output**.
* Format specifiers provide an alternative alignment method in f-strings.
