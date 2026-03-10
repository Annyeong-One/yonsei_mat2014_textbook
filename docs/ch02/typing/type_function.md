# Type Introspection


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## type() Function

### 1. Basic Usage

```python
x = 42
print(type(x))             # <class 'int'>

y = "hello"
print(type(y))             # <class 'str'>
```

### 2. Compare Types

```python
x = 42

if type(x) == int:
    print("x is integer")

if type(x) == str:
    print("Won't print")
```

## isinstance()

### 1. Better Check

```python
x = 42

if isinstance(x, int):
    print("x is int")

# Multiple types
if isinstance(x, (int, float)):
    print("x is number")
```

### 2. Inheritance

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True

print(type(dog) == Dog)         # True
print(type(dog) == Animal)      # False
```

## issubclass()

### 1. Check Hierarchy

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
```

## Callable Check

### 1. Is Callable

```python
def my_func():
    return 42

print(callable(my_func))        # True
print(callable(42))             # False
print(callable(lambda: 1))      # True
```

## hasattr()

### 1. Check Attributes

```python
class MyClass:
    def __init__(self):
        self.value = 42

obj = MyClass()

print(hasattr(obj, 'value'))    # True
print(hasattr(obj, 'missing'))  # False
```

## dir() and vars()

### 1. List Attributes

```python
class MyClass:
    def __init__(self):
        self.x = 1
        self.y = 2

obj = MyClass()

print(dir(obj))                 # All attributes
print(vars(obj))                # {'x': 1, 'y': 2}
```

## Practical Usage

### 1. Type Validation

```python
def validate_int(value):
    if not isinstance(value, int):
        raise TypeError("Must be int")
    return value * 2

print(validate_int(5))          # 10
```

### 2. Dynamic Dispatch

```python
def process(value):
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    return None

print(process(5))               # 10
print(process("hi"))            # "HI"
```
