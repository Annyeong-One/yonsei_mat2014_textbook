# Getter Setter Deleter


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Property Decorator

### 1. Getter

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

c = Circle(5)
print(c.radius)  # 5
```

### 2. Setter

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Negative radius")
        self._radius = value

c = Circle(5)
c.radius = 10  # OK
```

### 3. Deleter

```python
    @radius.deleter
    def radius(self):
        del self._radius
```

## Summary

- @property for getter
- @prop.setter for setter
- @prop.deleter for deleter
- Clean interface
