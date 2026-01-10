# Inheritance and `super()`

Inheritance allows classes to reuse and extend behavior. `super()` enables cooperative method calls.

---

## 1. Basic inheritance

```python
class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    def speak(self):
        print("bark")
```

---

## 2. Calling parent methods

```python
class LoggedDog(Dog):
    def speak(self):
        super().speak()
        print("logged")
```

`super()` respects the MRO.

---

## 3. Why `super()` matters

- Enables multiple inheritance
- Avoids hardcoding parent class names
- Produces extensible designs

---

## 4. Best practices

- Always use `super()` in cooperative hierarchies
- Keep inheritance shallow
- Prefer composition when possible

---

## Key takeaways

- Inheritance extends behavior.
- `super()` follows the MRO.
- Proper use enables flexible designs.
