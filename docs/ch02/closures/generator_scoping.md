# Generator Scoping

## Generators and Closures

### 1. Generator Functions

```python
def make_counter(start):
    count = start
    
    def counter():
        nonlocal count
        while True:
            count += 1
            yield count
    
    return counter()

gen = make_counter(0)
print(next(gen))  # 1
print(next(gen))  # 2
```

## Generator Expressions

### 1. Scope Isolation

```python
x = 10
gen = (x for x in range(3))

print(x)  # 10 (unchanged)
print(list(gen))  # [0, 1, 2]
```

## Summary

- Generators can close over variables
- Generator expressions have own scope
- Similar to comprehensions
