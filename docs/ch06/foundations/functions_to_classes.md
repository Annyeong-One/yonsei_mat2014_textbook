# Functions to Classes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Understanding the evolution from functions → closures → classes reveals Python's design philosophy.

---

## The Evolution

$$\begin{array}{ccccccccccccccc}
\text{Function}&\Rightarrow&\text{Closure}&\Rightarrow&\text{Class}\\
&&\uparrow&&\uparrow&\\
&&\text{Free Variables}&&\text{Attributes}\\
&&&&\text{Methods}\\
\end{array}$$

---

## Functions

### 1. First-Class Objects

Functions can be assigned, passed, and returned.

```python
def square(x):
    return x * x

f = square
print(f(4))  # 16
```

### 2. Stateless

Functions don't retain state between calls.

```python
def add_ten(x):
    return x + 10

result = add_ten(5)  # 15
# No memory of previous calls
```

### 3. Limitations

Cannot encapsulate data with behavior.

---

## Closures

### 1. Capturing Variables

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # factor is captured
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30
```

### 2. Free Variables

`factor` is a **free variable** in `multiply`:
- Used inside the function
- Not defined locally
- Captured from enclosing scope

### 3. State Retention

```python
times3 = make_multiplier(3)
del make_multiplier  # Can delete outer function

print(times3(10))  # 30 - still works!
```

---

## Free Variables

### 1. Definition

A variable that is:
- Referenced in a function
- Not bound (defined) in that function
- Comes from an enclosing scope

### 2. Example

```python
x = 10  # global

def my_function(y):
    return x + y  # x is FREE, y is BOUND
```

### 3. In Closures

```python
def outer(x):
    def inner(y):
        return x + y  # x is FREE in inner
    return inner
```

---

## From Closure to Class

### 1. Closure Version

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30
```

### 2. Class Version

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # attribute instead of free variable
    
    def multiply(self, x):
        return x * self.factor
    
    def __call__(self, x):
        return self.multiply(x)

times3 = Multiplier(3)
print(times3(10))  # 30
```

### 3. Key Differences

- Closure: captures free variables
- Class: stores attributes explicitly

---

## Class Advantages

### 1. Multiple Methods

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1
    
    def reset(self):
        self.count = 0
```

### 2. Named State

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width   # explicit names
        self.height = height
```

### 3. Special Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

---

## Closure Limitations

### 1. Single Function

Closures typically return one function.

### 2. Implicit State

State is captured implicitly through free variables.

### 3. No Introspection

Harder to inspect what's captured.

```python
# What's in times3?
times3 = make_multiplier(3)
# Not obvious from outside
```

---

## Class After Deletion

### 1. Instance Survives

```python
class Multiplier:
    class_var = "I exist"
    
    def __init__(self, factor):
        self.factor = factor

times3 = Multiplier(3)
del Multiplier  # Delete class
```

### 2. Methods Still Work

```python
print(times3.factor)  # ✅ Works: 3
```

### 3. Class Attributes Lost

```python
print(times3.class_var)  # ❌ AttributeError
# new_obj = Multiplier(5)  # ❌ NameError
```

---

## When to Use Each

### 1. Use Functions

Simple, stateless operations.

### 2. Use Closures

Encapsulate simple state with single behavior.

### 3. Use Classes

- Multiple methods needed
- Complex state
- Need inheritance
- Need special methods

---

## Key Takeaways

- Functions → Closures → Classes progression.
- Closures capture free variables.
- Classes provide explicit attributes.
- Classes offer more features (methods, inheritance).
- Choose based on complexity needs.
