# Reference Counting


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

CPython의 기본 메모리 관리 메커니즘입니다.

## CPython Mechanism

### 1. Every Object Has a Reference Count

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 (x + getrefcount's arg)
```

### 2. Increment/Decrement

```python
x = [1, 2, 3]  # refcount = 1
y = x          # refcount = 2
del y          # refcount = 1
del x          # refcount = 0 → freed
```

## Automatic Management

### 1. No Manual Memory Management

```python
def function():
    x = [1, 2, 3]
    # Automatically freed when function returns
    return

# No memory leak
```

## Advantages

### 1. Immediate Deallocation

```python
x = [1, 2, 3]
del x
# Memory freed immediately (deterministic)
```

### 2. Predictable

메모리가 언제 해제되는지 예측 가능합니다.

---

## Limitation: Circular References

참조 카운팅만으로는 순환 참조를 해제할 수 없습니다.

### The Problem

```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a
# Cycle: a → b → a
```

```
     ┌──────────┐
     │  a       │
     │ refcount │──────┐
     │   = 1    │      │
     └──────────┘      ▼
          ▲       ┌──────────┐
          │       │  b       │
          │       │ refcount │
          └───────│   = 1    │
                  └──────────┘
```

`del a, b` 후에도 각 객체의 refcount는 1로 남아있습니다.

### Detection with GC

```python
import gc

# GC finds cycles
gc.collect()
```

### Manual Prevention

```python
# Break cycle manually
a.ref = None
b.ref = None
del a, b  # Now freed
```

## Summary

| Feature | Reference Counting |
|---------|-------------------|
| Speed | Immediate |
| Deterministic | Yes |
| Cycles | Cannot handle |
| Overhead | Per-operation |
