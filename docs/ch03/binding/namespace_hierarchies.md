# Namespace Hierarchies


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Four Levels

### 1. LEGB Rule

Lookup order:
1. **L**ocal
2. **E**nclosing
3. **G**lobal
4. **B**uilt-in

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # "local"
    
    inner()

outer()
```

## Local Scope

### 1. Function Local

```python
def function():
    x = 10  # Local scope
    print(x)

function()
# print(x)  # NameError
```

### 2. Method Local

```python
class MyClass:
    def method(self):
        x = 10  # Method local
        print(x)

obj = MyClass()
obj.method()
```

## Enclosing Scope

### 1. Nested Functions

```python
def outer():
    x = 10  # Enclosing for inner
    
    def inner():
        print(x)  # Access enclosing
    
    inner()

outer()  # 10
```

### 2. Multiple Levels

```python
def level1():
    x = 1
    
    def level2():
        # x from level1 is enclosing
        
        def level3():
            print(x)  # Access level1's x
        
        level3()
    
    level2()

level1()  # 1
```

## Global Scope

### 1. Module Level

```python
# Module-level = global
x = 10

def function():
    print(x)  # Access global

function()  # 10
```

### 2. Global Keyword

```python
x = 10

def function():
    global x
    x = 20  # Modify global

function()
print(x)  # 20
```

## Built-in Scope

### 1. Python Built-ins

```python
# Built-in functions
print(len([1, 2, 3]))
print(type(42))

# Always accessible
```

### 2. Shadowing Built-ins

```python
# Can shadow (but don't!)
len = 42

# print(len([1, 2, 3]))  # TypeError

# Restore
del len
print(len([1, 2, 3]))  # 3
```

## Lookup Examples

### 1. All Levels

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        # Local x shadows all
        x = "local"
        print(x)  # "local"
    
    inner()

outer()
```

### 2. Skip Levels

```python
x = "global"

def outer():
    # No x here
    
    def inner():
        print(x)  # Skip enclosing, use global
    
    inner()

outer()  # "global"
```

## Class Namespace

### 1. Separate Hierarchy

```python
class MyClass:
    x = 10  # Class namespace
    
    def method(self):
        # Access via self
        print(self.x)

obj = MyClass()
obj.method()  # 10
```

### 2. Instance vs Class

```python
class MyClass:
    x = "class"
    
    def __init__(self):
        self.x = "instance"

obj = MyClass()
print(obj.x)  # "instance"
print(MyClass.x)  # "class"
```

## Summary

### 1. LEGB Order

```python
x = "builtin (if shadowed)"
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        # Lookup: local → enclosing → global → builtin
```

### 2. Key Points

- Lookup goes L → E → G → B
- First match wins
- Can skip levels
- Classes separate
