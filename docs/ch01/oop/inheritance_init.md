# Initialization Patterns

Proper initialization is critical in inheritance hierarchies. This section covers common patterns and pitfalls.

---

## Missing Child `__init__`

### 1. Hidden Dependency

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    # no __init__ defined
    def speak(self):
        return f"{self.name} says Woof!"
```

The child silently depends on parent's `__init__`.

### 2. Reduced Clarity

```python
dog = Dog("Buddy")
```

Not obvious what attributes `Dog` has.

### 3. Maintenance Risk

If parent `__init__` signature changes, child breaks.

### 4. Better Practice

```python
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
```

Explicit is better than implicit.

---

## Overriding Without `super()`

### 1. Parent Skipped

```python
class Parent:
    def __init__(self, last_name):
        print("Parent init")
        self.last_name = last_name

class Child(Parent):
    def __init__(self, last_name):
        print("Child init")
        self.last_name = last_name  # parent __init__ never runs
```

### 2. Lost Initialization

```python
a = Child("Lee")
# Output: Child init
# Parent init never runs!
```

### 3. Correct Approach

```python
class Child(Parent):
    def __init__(self, last_name):
        super().__init__(last_name)
        print("Child init")
```

---

## Explicit vs `super()`

### 1. Direct Parent Call

```python
class Child(Parent):
    def __init__(self, last_name):
        Parent.__init__(self, last_name)
```

**Pros:**
- Simple and explicit
- Works for single inheritance

**Cons:**
- Hardcoded class name
- Ignores MRO
- Breaks in multiple inheritance

### 2. Using `super()`

```python
class Child(Parent):
    def __init__(self, last_name):
        super().__init__(last_name)  # no self!
```

**Pros:**
- Respects MRO
- Cooperative inheritance
- Future-proof refactoring

**Cons:**
- Slightly less obvious for beginners

---

## Common Mistakes

### 1. Forgetting `super()`

```python
class Child(Parent):
    def __init__(self, name):
        # forgot super().__init__()
        self.child_attr = "value"
```

Parent initialization is lost.

### 2. Passing `self`

```python
# Wrong
super().__init__(self, last_name)

# Correct
super().__init__(last_name)
```

`super()` automatically handles `self`.

### 3. Inconsistent Signatures

```python
class Parent:
    def __init__(self, a, b):
        pass

class Child(Parent):
    def __init__(self, a):  # missing b
        super().__init__(a)  # Error!
```

---

## Best Practices

### 1. Always Define `__init__`

Even if delegating to parent, be explicit.

### 2. Call `super()` Early

```python
def __init__(self, name):
    super().__init__(name)
    # then add child-specific logic
```

### 3. Match Signatures

Ensure child accepts all parent parameters.

---

## Key Takeaways

- Always define `__init__` in child classes.
- Use `super().__init__()` to call parent.
- Never pass `self` to `super()`.
- Explicit initialization prevents bugs.
