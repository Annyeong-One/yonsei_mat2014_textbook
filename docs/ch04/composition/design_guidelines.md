# Design Guidelines

## Prefer Composition

### 1. Over Inheritance

```python
# Bad: inheritance
class FlyingDog(Dog, Flying):
    pass

# Good: composition
class Dog:
    def __init__(self):
        self.abilities = []
    
    def add_ability(self, ability):
        self.abilities.append(ability)
```

## When to Use

### 1. Composition

- Has-a relationship
- Flexible behavior
- Multiple components

### 2. Inheritance

- Is-a relationship
- Shared interface
- Natural hierarchy

## Summary

- Favor composition
- Use inheritance sparingly
- Consider flexibility
- Think relationships
