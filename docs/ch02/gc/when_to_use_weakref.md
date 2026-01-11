# When to Use Weakref

## Use Cases

### 1. Caches

When cache shouldn't prevent GC

### 2. Observers

When observers can disappear

### 3. Parent-Child

When need back reference

## Don't Use When

### 1. Need Guaranteed Access

Strong references better

## Summary

- Caches: yes
- Callbacks: yes
- Critical data: no
