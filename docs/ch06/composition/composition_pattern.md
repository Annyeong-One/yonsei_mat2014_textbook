# Composition Pattern

Composition models a "has-a" relationship where one object owns another as an integral part. The owner creates the part during its own initialization, and the part's lifetime is tied to the owner. When the owner is destroyed, its parts go with it. Composition is often preferred over inheritance for building flexible, modular systems because it avoids the tight coupling that deep class hierarchies introduce.

## What Is Composition

### 1. Has-A Relationship

In composition, the container creates its parts internally during initialization. This establishes exclusive ownership: no outside code holds a reference to the part before the container exists.

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

The `Car` creates its own `Engine` inside `__init__`. Outside code interacts with the engine only through the `Car` interface, which encapsulates the internal part.

## Ownership

### 1. Strong Relationship

Strong ownership means the part's lifetime is tied to the container. The part is created when the container is created, and Python's garbage collector automatically destroys the part when the container is collected. There is no need for manual cleanup.

```python
class Car:
    def __init__(self):
        self.engine = Engine()  # Engine created with Car

# When car goes out of scope and is garbage-collected,
# the Engine is also collected automatically because
# no other references to it exist.
car = Car()
del car  # Engine is cleaned up along with Car
```

Because the `Engine` was created inside `Car.__init__` and no external variable holds a reference to it, deleting the `Car` removes the last reference to the `Engine`, and Python's garbage collector reclaims it.

## Summary

- Composition establishes a has-a relationship where the container creates and owns its parts.
- The owned component shares the lifetime of its container and is destroyed when the container is destroyed.
- This strong coupling between the whole and its parts means the part cannot exist independently.
- Composition promotes modular design by encapsulating implementation details behind the container's interface.
