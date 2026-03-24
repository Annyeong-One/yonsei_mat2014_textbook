# Design Guidelines

Choosing between composition and inheritance is one of the most consequential design decisions in object-oriented programming. The widely cited guideline "favor composition over inheritance" exists because composition generally provides greater flexibility, simpler testing, and fewer surprises as a codebase grows. This page summarizes when each approach is appropriate and why.

## Prefer Composition

### 1. Over Inheritance

Using multiple inheritance to combine unrelated capabilities creates rigid class hierarchies that are difficult to modify. Composition lets you attach capabilities dynamically, keeping each component independent and interchangeable.

```python
# Fragile: combining unrelated capabilities via inheritance
class FlyingDog(Dog, Flying):
    pass

# Flexible: attaching capabilities via composition
class Dog:
    def __init__(self):
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)
```

With the composition approach, you can add or remove abilities at runtime without changing the class hierarchy. The inheritance approach, by contrast, locks the set of capabilities into the class definition.

## When to Use

### 1. Composition

Choose composition when the relationship between objects is best described as "has-a." The following criteria point toward composition.

- **Has-a relationship**: the object contains or uses another object as a part (e.g., a `Car` has an `Engine`).
- **Flexible behavior**: the set of capabilities may change at runtime or vary across instances.
- **Multiple components**: the object is built from several independent parts that can be developed and tested separately.

### 2. Inheritance

Choose inheritance when there is a genuine "is-a" relationship and the subclass truly represents a specialized version of the parent.

- **Is-a relationship**: the subclass is a natural specialization of the parent (e.g., a `SavingsAccount` is a `BankAccount`).
- **Shared interface**: all subclasses need to expose the same set of methods so that client code can treat them interchangeably.
- **Natural hierarchy**: the domain has a clear, shallow hierarchy that is unlikely to change frequently.

## Summary

- Favor composition when you need flexibility, runtime configurability, or when combining unrelated behaviors.
- Use inheritance sparingly and only for genuine is-a relationships with shallow, stable hierarchies.
- Consider the flexibility trade-off: inheritance is simpler for small hierarchies, but composition scales better as requirements grow.
- Think about the relationship first — if "has-a" describes it more accurately than "is-a," composition is almost always the better choice.
