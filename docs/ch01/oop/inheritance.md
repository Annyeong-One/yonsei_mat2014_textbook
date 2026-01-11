# Inheritance Basics

Inheritance allows classes to reuse and extend behavior. `super()` enables cooperative method calls.

---

## Basic Inheritance

```python
class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    def speak(self):
        print("bark")
```

---

## Calling Parent Methods

```python
class LoggedDog(Dog):
    def speak(self):
        super().speak()
        print("logged")
```

`super()` respects the MRO.

---

## Why Use `super()`

### 1. Multiple Inheritance

Enables cooperative inheritance patterns.

### 2. Avoids Hardcoding

No need to hardcode parent class names.

### 3. Extensible Design

Makes refactoring easier and designs more flexible.

---

## Best Practices

### 1. Use `super()` Always

In cooperative hierarchies, always use `super()`.

### 2. Keep Shallow

Prefer shallow inheritance hierarchies.

### 3. Prefer Composition

Use composition when inheritance isn't needed.

---

## Key Takeaways

- Inheritance extends behavior.
- `super()` follows the MRO.
- Proper use enables flexible designs.
