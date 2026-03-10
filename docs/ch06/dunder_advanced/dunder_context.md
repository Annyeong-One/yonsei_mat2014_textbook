# Context Managers


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## With Statement Support

### 1. __enter__ Method
Setup code, returns resource.

### 2. __exit__ Method
Cleanup code, handles exceptions.

### 3. Usage
```python
class File:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```
