# Composition Pattern

## Concept

### 1. Has-A Relationship

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Engine started
```

## Ownership

### 1. Strong Relationship

```python
# Car owns engine
# Engine doesn't exist without car

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def __del__(self):
        # Engine destroyed with car
        del self.engine
```

## Summary

- Has-a relationship
- Component owned
- Strong coupling
- Part of whole
