# First-Class Functions

## Functions as Objects

### 1. Assign to Variable

```python
def greet():
    return "Hello"

f = greet  # Assign function
print(f())  # "Hello"
```

### 2. Pass as Argument

```python
def apply(func, value):
    return func(value)

def square(x):
    return x ** 2

result = apply(square, 5)  # 25
```

### 3. Return from Function

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(5))  # 10
```

## Store in Structures

### 1. Lists

```python
operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]

for op in operations:
    print(op(5))
```

### 2. Dictionaries

```python
commands = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b
}

print(commands['add'](10, 5))  # 15
```

## Higher-Order Functions

### 1. Map

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
```

### 2. Filter

```python
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

## Summary

- Functions are objects
- Can assign, pass, return
- Store in collections
- Enable functional programming
