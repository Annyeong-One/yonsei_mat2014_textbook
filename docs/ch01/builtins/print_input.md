# `print()` and

Two of the most commonly used built-in functions in Python are `print()` (for output) and `input()` (for interactive user input). You’ll use them constantly when learning and when building small tools.

---

## `print()`

### 1. Basic usage

```python
print("Hello, world!")
print(123)
print(3.14)
```

`print()` converts its arguments to strings and writes them to standard output.

### 2. Printing multiple

```python
name = "Alice"
age = 30
print(name, age)          # Alice 30
print(name, "is", age)    # Alice is 30
```

By default, values are separated by a single space.

### 3. `sep` and `end`

- `sep` controls the separator between values.
- `end` controls what is printed at the end (newline by default).

```python
print("A", "B", "C", sep=",")      # A,B,C
print("no newline", end="")        # stays on same line
print(" -> next print continues")  # appended after end=""
```

### 4. f-strings

Use f-strings to format text cleanly:

```python
pi = 3.14159
print(f"pi ≈ {pi:.2f}")  # pi ≈ 3.14
```

---

## `input()`

### 1. Basic usage

`input()` reads a line of text from the user and **returns a string**:

```python
name = input("Your name? ")
print(f"Hi, {name}!")
```

### 2. Converting types

Because `input()` returns a string, you often need to convert to `int` or `float`:

```python
age_str = input("Your age? ")
age = int(age_str)
print(f"Next year you’ll be {age + 1}.")
```

Or in one line:

```python
x = float(input("Enter a number: "))
print(x * 2)
```

### 3. Handling invalid

Users can type anything, so conversions can fail:

```python
s = input("Enter an integer: ")
try:
    n = int(s)
    print("ok:", n)
except ValueError:
    print("That was not an integer.")
```

---

## Mini example

```python
price = float(input("Price: "))
qty = int(input("Quantity: "))
total = price * qty
print(f"Total cost: {total:.2f}")
```

---

## Key takeaways

- `print()` displays values; customize it with `sep` and `end`.
- `input()` reads user input **as a string**.
- Convert input to numeric types with `int()` / `float()`.
- Use `try/except` for robust interactive programs.
