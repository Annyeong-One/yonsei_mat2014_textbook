# Closure Scope Chain

## Nested Scopes

### 1. Multiple Levels

```python
def level1():
    x = 1
    
    def level2():
        y = 2
        
        def level3():
            z = 3
            # Can access x, y, z
            return x + y + z
        
        return level3
    
    return level2

f = level1()()()
print(f)  # 6
```

### 2. Lookup Order

```python
x = "global"

def level1():
    x = "level1"
    
    def level2():
        x = "level2"
        
        def level3():
            # Looks in: level3 -> level2 -> level1 -> global
            print(x)  # "level2"
        
        level3()
    
    level2()
```

## Skip Levels

### 1. Direct to Outer

```python
def outer():
    x = 10
    
    def middle():
        # No x here
        
        def inner():
            return x  # Skips middle, uses outer
        
        return inner
    
    return middle()

f = outer()
print(f())  # 10
```

### 2. Multiple Variables

```python
def level1():
    a = 1
    
    def level2():
        b = 2
        
        def level3():
            c = 3
            # a from level1, b from level2, c local
            return a + b + c
        
        return level3
    
    return level2

f = level1()()
print(f())  # 6
```

## Shadowing

### 1. Inner Shadows Outer

```python
def outer():
    x = "outer"
    
    def middle():
        x = "middle"
        
        def inner():
            print(x)  # "middle"
        
        inner()
    
    middle()

outer()
```

### 2. nonlocal Resolution

```python
def level1():
    x = 1
    
    def level2():
        x = 2
        
        def level3():
            nonlocal x  # Modifies level2's x
            x = 3
        
        level3()
        print(x)  # 3
    
    level2()
    print(x)  # 1 (unchanged)
```

## Complex Example

### 1. Multiple Captured

```python
def create_operations():
    a = 10
    
    def wrapper():
        b = 20
        
        def add():
            return a + b
        
        def multiply():
            return a * b
        
        def power():
            c = 2
            return a ** c
        
        return add, multiply, power
    
    return wrapper

ops = create_operations()()
add, mult, power = ops
print(add())     # 30
print(mult())    # 200
print(power())   # 100
```

## Inspection

### 1. View Chain

```python
import inspect

def outer():
    x = 1
    
    def middle():
        y = 2
        
        def inner():
            z = 3
            frame = inspect.currentframe()
            
            # Walk up frames
            while frame:
                print(frame.f_locals)
                frame = frame.f_back
        
        return inner
    
    return middle

f = outer()()
f()
```

## Summary

### 1. Scope Chain

- Nested function scopes
- Lookup goes inner to outer
- Can skip intermediate levels
- First match wins

### 2. Resolution

- Local -> Enclosing -> Global -> Builtin
- nonlocal affects closest
- Shadowing blocks outer
