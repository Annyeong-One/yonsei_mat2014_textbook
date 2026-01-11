# Generational GC

## Three Generations

### 1. Generation 0

```python
# Young objects
# Collected frequently
x = [1, 2, 3]  # Starts in gen 0
```

### 2. Generation 1

```python
# Survived one collection
# Collected less often
```

### 3. Generation 2

```python
# Survived multiple collections
# Collected rarely
```

## How It Works

### 1. Promotion

```python
# Object created → Gen 0
# Survives collection → Gen 1
# Survives again → Gen 2
```

### 2. Collection Frequency

```python
import gc

# (threshold0, threshold1, threshold2)
print(gc.get_threshold())  # (700, 10, 10)

# Gen 0: every 700 allocations
# Gen 1: every 10 gen-0 collections
# Gen 2: every 10 gen-1 collections
```

## Inspect

### 1. Object Counts

```python
import gc

# Objects in each generation
print(gc.get_count())  # (count0, count1, count2)
```

### 2. Statistics

```python
import gc

stats = gc.get_stats()
for i, stat in enumerate(stats):
    print(f"Gen {i}: {stat}")
```

## Why Generational

### 1. Weak Generational Hypothesis

Most objects die young:

```python
# Typical pattern
def process():
    temp = [1, 2, 3]  # Dies quickly
    return temp[0]

# temp collected in gen-0
```

### 2. Performance

```python
# Check young objects often (cheap)
# Check old objects rarely (expensive)
```

## Summary

- Three generations
- Young collected often
- Old collected rarely
- Based on survival
- Performance optimization
