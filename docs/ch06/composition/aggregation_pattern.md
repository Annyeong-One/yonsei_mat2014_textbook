# Aggregation Pattern

Aggregation is a form of "has-a" relationship where the contained objects have independent lifetimes. Unlike composition, the container does not create or destroy its parts. Instead, pre-existing objects are passed into the container, and they survive even if the container is destroyed. This distinction makes aggregation the right choice when objects need to be shared across multiple containers or reused after a container is gone.

## Aggregation as a Has-A Relationship

### 1. Weaker Has-A

In aggregation the container holds references to objects it did not create. This is a "weaker" form of has-a compared to composition, because the container has no control over the lifecycle of its parts.

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

Here, the `Wheel` objects are created before the `Car` exists. The `Car` merely holds a reference to the list that was passed in.

## Independence

### 1. Separate Lifetimes

The defining characteristic of aggregation is that aggregated objects exist before being associated with the container and continue to exist after the container is destroyed.

```python
# Wheels can exist without car
del car
print(len(wheels))  # 4 — wheels still exist
```

Because `wheels` was created outside of `Car`, deleting the `Car` instance has no effect on the `Wheel` objects. They remain accessible through the original `wheels` variable.

## Summary

- Aggregation is a weaker has-a relationship where the container does not own the lifecycle of its parts.
- Contained objects have independent lifetimes and can exist before and after the container.
- Multiple containers can share the same aggregated objects, enabling flexible designs.
- Aggregation produces loose coupling between the container and its parts, making each component easier to test and reuse independently.
