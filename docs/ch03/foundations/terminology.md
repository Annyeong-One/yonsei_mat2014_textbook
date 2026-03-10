# Key Terms


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Core Concepts

### 1. Binding

**Definition**: The association of a name with an object in a namespace

```python
x = 42  # Binds name 'x' to integer object 42
```

**Key Properties**:
- Names stored in namespaces (dictionaries)
- Objects stored in heap memory
- Multiple names can bind to same object

### 2. Namespace

**Definition**: A mapping from names to objects (implemented as dictionaries)

```python
# Module namespace
globals()  # Returns global namespace dict

# Function namespace
def f():
    x = 1
    return locals()  # Returns local namespace dict
```

**Types**:
- **Local**: Function/method scope
- **Enclosing**: Nested function scopes
- **Global**: Module level
- **Built-in**: Python built-ins

### 3. Closure

**Definition**: A function that captures variables from its enclosing scope

```python
def outer():
    x = 10
    def inner():
        return x  # Captures 'x' from outer
    return inner

f = outer()
print(f())  # 10 - closure remembers x
```

### 4. Frame Object

**Definition**: Runtime structure containing execution context and local variables

```python
import inspect

def example():
    frame = inspect.currentframe()
    print(frame.f_locals)  # Local namespace
    print(frame.f_globals)  # Global namespace

example()
```

## Memory Management

### 1. Interning

**Definition**: Optimization where identical immutable objects share memory

```python
# String interning
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True - same object

# Integer caching (CPython: -5 to 256)
a = 42
b = 42
print(a is b)  # True - cached
```

### 2. Reference Count

**Definition**: Number of names/variables pointing to an object

```python
import sys

x = [1, 2, 3]
y = x
print(sys.getrefcount(x))  # 3 (x, y, temp in getrefcount)
```

### 3. GC Generation

**Definition**: Age-based grouping for garbage collection efficiency

```python
import gc

# CPython uses generational GC
# Generation 0: Young objects
# Generation 1: Survived one collection
# Generation 2: Long-lived objects

print(gc.get_count())  # (count0, count1, count2)
```

### 4. Environment

**Definition**: Formal term for namespace context in language semantics

In formal semantics:
- Environment: Γ (gamma)
- Binding: Γ[x ↦ v] means "bind x to value v in Γ"

## Object Model

### 1. Identity

**Definition**: Unique identifier for object's memory location

```python
x = [1, 2, 3]
print(id(x))  # Object identity (address in CPython)
```

### 2. Type

**Definition**: Determines operations on the object

```python
x = 42
print(type(x))  # <class 'int'>
```

### 3. Value

**Definition**: The actual data stored in the object

```python
x = [1, 2, 3]
# Identity: id(x)
# Type: list
# Value: [1, 2, 3]
```

## Scoping Terms

### 1. Free Variable

**Definition**: Variable referenced in function but not defined locally

```python
x = 10
def f():
    return x  # x is free variable
```

### 2. Cell Object

**Definition**: CPython structure storing values for free variables

```python
def outer():
    x = 42
    def inner():
        return x
    print(inner.__closure__[0].cell_contents)  # 42
    return inner
```

### 3. LEGB

**Definition**: Scope resolution order: Local, Enclosing, Global, Built-in

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # "local" (finds in Local first)
    inner()

outer()
```

## Quick Reference

| Term | One-Line Definition |
|------|-------------------|
| **Binding** | Name → Object association |
| **Namespace** | Name → Object mapping |
| **Closure** | Function + captured vars |
| **Frame** | Execution context |
| **Interning** | Sharing immutables |
| **Refcount** | # of refs to object |
| **Environment** | Formal namespace |
| **Free Variable** | Non-local variable |
| **Cell** | Closure var container |
| **LEGB** | Scope lookup order |
