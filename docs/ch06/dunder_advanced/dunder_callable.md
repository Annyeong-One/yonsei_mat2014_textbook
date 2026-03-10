# Callable Objects


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Making Objects Callable

### 1. __call__ Method
Allows instances to be called like functions.

### 2. Use Cases
Function-like objects, decorators, state machines.

### 3. Example
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor
```
