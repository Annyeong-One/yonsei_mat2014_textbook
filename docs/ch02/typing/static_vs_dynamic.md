# Static vs Dynamic Typing


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python is **dynamically typed**, while languages like C are **statically typed**. This fundamental difference affects how you write and think about code.

---

## The Key Difference

| Aspect | Static (C) | Dynamic (Python) |
|--------|------------|------------------|
| Type checking | Compile-time | Runtime |
| Variable declaration | Explicit | Implicit |
| Type changes | Not allowed | Allowed |
| Error detection | Earlier | Later |

---

## Static Typing (C)

Types are determined at **compile-time** and cannot change.

### Explicit Declaration Required

```c
int age = 25;           // Must declare type
float price = 19.99;    // Type is fixed
char name[] = "Alice";  // Array of characters
```

### Type Mismatches Caught Early

```c
#include <stdio.h>

int main() {
    int num = 5;
    num = "Hello";      // ❌ Compile error: incompatible types
    printf("%d\n", num);
    return 0;
}
```

The compiler catches the error **before** the program runs.

---

## Dynamic Typing (Python)

Types are determined at **runtime** and can change.

### No Declaration Needed

```python
age = 25              # int (inferred)
price = 19.99         # float (inferred)
name = "Alice"        # str (inferred)
```

### Variables Can Change Type

```python
num = 5               # num is int
print(num, type(num)) # 5 <class 'int'>

num = "Hello"         # num is now str
print(num, type(num)) # Hello <class 'str'>

num = [1, 2, 3]       # num is now list
print(num, type(num)) # [1, 2, 3] <class 'list'>
```

This runs without errors — Python allows type changes at runtime.

---

## Side-by-Side Comparison

### C Version

```c
#include <stdio.h>

int main() {
    int x = 10;
    int y = 20;
    int sum = x + y;
    printf("Sum: %d\n", sum);
    return 0;
}
```

### Python Version

```python
x = 10
y = 20
sum = x + y
print(f"Sum: {sum}")
```

Python is more concise — no type declarations, no semicolons, no `main()`.

---

## Pros and Cons

### Static Typing (C)

**Pros:**
- Errors caught at compile-time
- Better performance (no runtime type checks)
- Self-documenting code (types visible)
- IDE support (autocomplete, refactoring)

**Cons:**
- More verbose
- Less flexible
- Slower development

### Dynamic Typing (Python)

**Pros:**
- Faster development
- More flexible and concise
- Easier prototyping
- No boilerplate

**Cons:**
- Runtime errors (type bugs found later)
- Harder to refactor large codebases
- Performance overhead (runtime type checks)

---

## Python's Type Hints (Best of Both)

Python 3.5+ supports **optional type hints**:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 25
prices: list[float] = [19.99, 29.99, 39.99]
```

Type hints provide:
- Documentation
- IDE autocomplete
- Static analysis (with tools like `mypy`)

But they're **not enforced** at runtime — Python remains dynamically typed.

```python
def add(a: int, b: int) -> int:
    return a + b

# This still works (no runtime error)
result = add("Hello", " World")  # "Hello World"
```

---

## Duck Typing

Python uses "duck typing": if it walks like a duck and quacks like a duck, it's a duck.

```python
def print_length(obj):
    print(len(obj))     # Works if obj has __len__

print_length("hello")   # 5 (string)
print_length([1, 2, 3]) # 3 (list)
print_length((1, 2))    # 2 (tuple)
print_length({1, 2})    # 2 (set)
```

Python doesn't care about the **declared type** — only about **what the object can do**.

---

## When Does It Matter?

### Static Typing Preferred

- Large teams / long-lived projects
- Performance-critical systems
- When bugs are costly (finance, medical)

### Dynamic Typing Preferred

- Rapid prototyping
- Scripts and automation
- Data exploration
- Small projects / solo development

---

## Summary

| Feature | C (Static) | Python (Dynamic) |
|---------|------------|------------------|
| `int x = 5;` | Required | Not needed |
| `x = "hello"` after `x = 5` | ❌ Error | ✅ Allowed |
| Type checked | Compile-time | Runtime |
| Verbosity | Higher | Lower |
| Flexibility | Lower | Higher |
| Type hints | N/A | Optional (3.5+) |

Python's dynamic typing makes it beginner-friendly and great for rapid development, while type hints offer the benefits of static typing when needed.
