# Aggregation Pattern

## Concept

### 1. Weaker Has-A

```python
class Wheel:
    pass

class Car:
    def __init__(self, wheels):
        self.wheels = wheels  # Aggregation

# Wheels exist independently
wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
car = Car(wheels)
```

## Independence

### 1. Separate Lifetimes

```python
# Wheels can exist without car
del car
# wheels still exist
```

## Summary

- Weaker has-a
- Independent lifetimes
- Shared ownership
- Loose coupling
