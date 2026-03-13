
# Function Examples

This section gathers practical examples showing how functions, parameters, returns, and type hints work together.

---

## 1. Simple Greeting Function

```python
def greet() -> None:
    print("Hello")
````

Call:

```python
greet()
```

Output:

```text
Hello
```

---

## 2. Function with a Parameter

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")
```

Example call:

```python
greet("Alice")
```

Output:

```text
Hello, Alice
```

---

## 3. Function with Return Value

```python
def square(x: int) -> int:
    return x * x

print(square(5))
```

Output:

```text
25
```

---

## 4. Function with Multiple Parameters

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 4))
```

Output:

```text
7
```

---

## 5. Default Parameter Example

```python
def greet(name: str = "guest") -> str:
    return f"Hello, {name}"

print(greet())
print(greet("Sam"))
```

Output:

```text
Hello, guest
Hello, Sam
```

---

## 6. Keyword Argument Example

```python
def power(base: int, exponent: int) -> int:
    return base ** exponent

print(power(exponent=3, base=2))
```

Output:

```text
8
```

---

## 7. Early Return Example

```python
def safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

Output:

```text
5.0
None
```

---

## 8. Nested Function Calls

```python
def double(x: int) -> int:
    return 2 * x

def square(x: int) -> int:
    return x * x

print(square(double(3)))
```

Output:

```text
36
```

This example also illustrates the call stack:

```mermaid2
flowchart TD
    A[square(double(3))] --> B[call double(3)]
    B --> C[return 6]
    C --> D[call square(6)]
    D --> E[return 36]
```

---

## 9. Practical Example: Rectangle Area

```python
def area(length: float, width: float) -> float:
    return length * width

print(area(2.5, 4.0))
```

Output:

```text
10.0
```

---

## 10. Practical Example: Grade Label

```python
def grade_label(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"

print(grade_label(85))
```

Output:

```text
B
```

---

## 11. Summary

These examples show how functions support:

* code reuse
* clearer structure
* parameterized behavior
* reusable computations
* readable interfaces through type hints

Functions are the foundation of modular Python programming.

