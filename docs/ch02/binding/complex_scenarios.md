# Complex Scenarios

## Nested Functions

### 1. Closure Binding

```python
def outer():
    x = 10
    
    def inner():
        return x  # Binds to outer's x
    
    return inner

f = outer()
print(f())  # 10
```

### 2. Multiple Levels

```python
def level1():
    x = 1
    
    def level2():
        x = 2
        
        def level3():
            return x  # Binds to level2's x
        
        return level3()
    
    return level2()

print(level1())  # 2
```

## Class Attributes

### 1. Instance Binding

```python
class MyClass:
    def __init__(self):
        self.x = 10  # Instance attribute

obj = MyClass()
print(obj.x)  # 10
```

### 2. Class Binding

```python
class MyClass:
    x = 10  # Class attribute
    
    def __init__(self):
        self.y = 20  # Instance attribute

obj = MyClass()
print(obj.x)  # 10 (class)
print(obj.y)  # 20 (instance)
```

## Late Binding

### 1. Loop Problem

```python
# Common mistake
funcs = []
for i in range(3):
    funcs.append(lambda: i)

# All return 2!
print([f() for f in funcs])  # [2, 2, 2]
```

### 2. Solution

```python
# Capture with default
funcs = []
for i in range(3):
    funcs.append(lambda x=i: x)

print([f() for f in funcs])  # [0, 1, 2]
```

## Shadowing

### 1. Local Shadows Global

```python
x = 10  # Global

def function():
    x = 20  # Local shadows global
    print(x)  # 20

function()
print(x)  # 10
```

### 2. Parameter Shadowing

```python
x = 10

def function(x):  # Parameter shadows global
    print(x)

function(20)  # 20
```

## Nonlocal Binding

### 1. Modify Enclosing

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
    
    inner()
    print(x)  # 20

outer()
```

### 2. Multiple Levels

```python
def level1():
    x = 1
    
    def level2():
        nonlocal x
        x = 2
        
        def level3():
            nonlocal x
            x = 3
        
        level3()
    
    level2()
    print(x)  # 3

level1()
```

## Comprehensions

### 1. Own Scope

```python
x = 10

# Comprehension has own scope
result = [x for x in range(3)]

print(x)  # 10 (unchanged)
```

### 2. Variable Leak

```python
# In Python 2, leaked
# In Python 3, doesn't leak
[i for i in range(3)]

# print(i)  # NameError in Python 3
```

## Dynamic Binding

### 1. Runtime Creation

```python
# Create binding at runtime
name = "x"
value = 42

globals()[name] = value
print(x)  # 42
```

### 2. exec()

```python
# Dynamic code execution
code = "y = 100"
exec(code)

print(y)  # 100
```

## Summary

### 1. Complex Cases

- Closures
- Class attributes
- Late binding
- Shadowing
- Nonlocal

### 2. Best Practices

- Avoid shadowing
- Use defaults for loops
- Be explicit with nonlocal
- Limit dynamic binding
