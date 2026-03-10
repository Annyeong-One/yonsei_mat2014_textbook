# Dynamic Typing


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

### 1. No Type Declarations

```python
# No type needed
x = 42
x = "hello"  # Can change type
x = [1, 2, 3]  # Again
```

## Runtime Type Checking

### 1. Type Determined at Runtime

```python
def process(data):
    # Type checked when executed
    return data * 2

print(process(5))      # 10
print(process("hi"))   # "hihi"
```

## Duck Typing

### 1. If It Walks Like Duck

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking!"

def make_it_quack(thing):
    return thing.quack()

# Both work
print(make_it_quack(Duck()))
print(make_it_quack(Person()))
```

## Summary

- Types determined at runtime
- No explicit declarations
- Duck typing philosophy
- Flexible but needs care
